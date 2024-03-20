const HSLToRGB = (h, s, l) => {
    l /= 100;
    const a = s * Math.min(l, 1 - l) / 100;
    const f = n => {
        const k = (n + h / 30) % 12;
        const color = l - a * Math.max(-1, Math.min(k - 3, 9 - k, 1));
        return Math.round(255 * color);
    };
    return [f(0), f(8), f(4)];
};


function colorWithOpacity(color, opacity) {
    if (color.startsWith('#')) {
        let r = 0, g = 0, b = 0;
        if (color.length === 4) {
            r = parseInt(color[1] + color[1], 16);
            g = parseInt(color[2] + color[2], 16);
            b = parseInt(color[3] + color[3], 16);
        } else if (color.length === 7) {
            r = parseInt(color[1] + color[2], 16);
            g = parseInt(color[3] + color[4], 16);
            b = parseInt(color[5] + color[6], 16);
        }
        return `rgba(${r}, ${g}, ${b}, ${opacity})`;
    }

    if (color.startsWith('rgb(')) {
        return color.replace('rgb', 'rgba').replace(')', `, ${opacity})`);
    }
    
    if (color.startsWith('rgba(')) {
        return color.replace(/[\d\.]+\)$/g, `${opacity})`);
    }
    
    if (color.startsWith('hsl(')) {
        const [h, s, l] = color.match(/\d+\.?\d*/g).map(Number);
        const [r, g, b] = HSLToRGB(h, s, l);
        return `rgba(${r}, ${g}, ${b}, ${opacity})`;
    }
    
    if (color.startsWith('hsla(')) {
        const [h, s, l, a] = color.match(/\d+\.?\d*/g).map(Number);
        const [r, g, b] = HSLToRGB(h, s, l);
        return `rgba(${r}, ${g}, ${b}, opacity)`;
    }
    
    return color;
}

document.addEventListener('DOMContentLoaded', () => {

    const chartDataScript = document.getElementById('chart_data');
    const chartData = JSON.parse(chartDataScript.textContent);
    const labels = chartData.labels;
    const datasets = chartData.datasets;
    const docStyle = getComputedStyle(document.documentElement);
    const gridColor = docStyle.getPropertyValue('--grid-color');
    const chartColor = docStyle.getPropertyValue('--w-color-secondary');
    const criticalColor = docStyle.getPropertyValue('--w-color-critical-200');
    const warningColor = docStyle.getPropertyValue('--w-color-warning-100');
    const infoColor = docStyle.getPropertyValue('--w-color-info-100');
    const colors = [
        chartColor,
        criticalColor,
        warningColor,
        infoColor,
    ];

    datasets.forEach((dataset, index) => {
        dataset.borderColor = colors[index % colors.length];
        dataset.pointBackgroundColor = colors[index % colors.length];
        dataset.backgroundColor = colors[index % colors.length];
    });

    const canvas = document.getElementById('filter-chart');
    const ctx = canvas.getContext('2d');
    const filterChart = new Chart(ctx, {
        type: canvas.dataset.chartType || 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            aspectRatio: 1.8,
            plugins: {
                legend: {
                    align: 'start',
                    position: 'bottom',
                },
            },
            scales: {
                x: {
                    grid: {
                        color: gridColor,
                    }
                },
                y: {
                    grid: {
                        color: gridColor,
                    }
                } 
            }
        }
    });

});