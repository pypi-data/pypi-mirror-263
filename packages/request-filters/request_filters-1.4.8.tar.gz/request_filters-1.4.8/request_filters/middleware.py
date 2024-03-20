
from django.apps import apps
from django.core.exceptions import PermissionDenied
from typing import TYPE_CHECKING
import time

if TYPE_CHECKING:
    from .models import Filter, FilterSettings

from . import log, VERSION
from .util import get_ip_address, skip_logging
from .models import FilteredRequest
from .signals import (
    request_started,
    request_finished,
)
from .options import (
    RequestFilters,
)


FilterSettingsModel: "FilterSettings" = apps.get_model(
    "request_filters",
    "FilterSettings",
    require_ready=False,
)

def bulk_create_filtered_requests(requests: list[dict]):
    """
        Create FilteredRequest instances in bulk.
    """
    requests = filter(None, requests)
    FilteredRequest.objects.bulk_create([FilteredRequest(**kwgs) for kwgs in requests])

class RequestFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the request is excluded, return the response.
        # Useful for making sure the site will remain accessible for administrators.
        if RequestFilters.request_is_excluded(request):
            log(f"({self.__class__.__name__} / {get_ip_address(request)}) Request was excluded from filtering: {request.path}", log.DEBUG)
            response = self.get_response(request)
            if RequestFilters.ADD_FILTER_HEADERS:
                response["X-Request-Filters"] = "false"
                response["X-Request-Filters-Excluded"] = "true"
            return response

        filter_start_time = time.time()
        ip_addr = get_ip_address(request)

        # Load the filters and settings from the cache.
        settings: "FilterSettings" = FilterSettingsModel.load_from_cache(request)
        filters:  list["Filter"]   = settings.get_filters()

        if not filters:
            response = self.get_response(request)
            if RequestFilters.ADD_FILTER_HEADERS:
                response["X-Request-Filters"] = "false"
                response["X-Request-Filters-Empty"] = "true"
            return response

        # Broadcast the request_started signal.
        request_started.send(sender=self, request=request, settings=settings, filters=filters)

        # Execute the filters and return the response if a filter matches,
        # otherwise return the response from get_response.
        response, passed_filters = self.execute_filters(settings, request, filters)

        # Broadcast the request_finished signal.
        request_finished.send(sender=self, request=request, settings=settings, filters=filters, response=response)

        if RequestFilters.ADD_FILTER_HEADERS:
            # Set headers to indicate that the request was filtered.
            response["X-Request-Filters"]           = "true"
            response["X-Request-Filters-Pass"]      = "true" if passed_filters else "false"
            response["X-Request-Filters-Duration"]  = str(time.time() - filter_start_time)
            response["X-Request-Filters-Version"]   = VERSION
            
        log(f"({self.__class__.__name__}) Filtering request ({ip_addr}) with {len(filters)} filters took {time.time() - filter_start_time} seconds", log.DEBUG)
        
        return response
    

    def execute_filters(self, settings: "FilterSettings", request, filters: list["Filter"]):
        """
            Execute the filters and return the response if a filter matches.
        """

        # Filter.passes_test checks if the request fits the 'shape' of the filter.
        # For example, if the type is IP, it checks if the request IP is in the filter.filter_value's CIDR range.
        # It returns true if the value is a match and thus should be filtered.
        # log_request(commit=False) returns a dictionary of kwargs to be used to create a FilteredRequest instance.
        # If commit is True, the FilteredRequest instance will be created and saved to the database; the instance will be returned.
        # This means we must manually create the FilteredRequest instances in bulk at the end of the function (when returning, raising etc...)
        requests = []
        for idx, filter in enumerate(filters):
            if filter.passes_test(settings, request):
                
                # Log and respond if filter matches.
                try:
                    response = filter.execute_action(settings, request, self.get_response)

                # Log then re-raise PermissionDenied
                except PermissionDenied as e:
                    kwgs = FilteredRequest.log_request(request, filter=filter, filter_index=idx, fail_silently=True, commit=False)
                    if kwgs:
                        requests.append(kwgs)
                    bulk_create_filtered_requests(requests)
                    raise e
                
                # Log the request/response.
                else:
                    # Filters may return none to allow for the next filter to be executed.
                    kwgs = FilteredRequest.log_request(request, filter=filter, response=response, filter_index=idx, fail_silently=True, commit=False)
                    if kwgs:
                        requests.append(kwgs)
                        
                    if response is not None:
                        bulk_create_filtered_requests(requests)
                        return response, False
                
        # No filters matched
        response = self.get_response(request)

        if RequestFilters.LOG_HAPPY_PATH:
            skip_logging(request, False)
            kwgs = FilteredRequest.log_request(request, filter=None, response=response, fail_silently=True, commit=False)
            if kwgs:
                requests.append(kwgs)

        bulk_create_filtered_requests(requests)

        return response, True
    
