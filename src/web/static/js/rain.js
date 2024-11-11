const digitalRain = document.getElementById('digital-rain');

function createRainColumn() {
    const column = document.createElement('div');
    column.className = 'rain-column';
    column.style.left = `${Math.random() * 100}%`;
    column.style.animationDuration = `${5 + Math.random() * 10}s`;

    for (let i = 0; i < 20; i++) {
        const char = String.fromCharCode(33 + Math.floor(Math.random() * 94));
        column.innerHTML += char + '<br>';
    }

    digitalRain.appendChild(column);

    setTimeout(() => {
        column.remove();
        createRainColumn();
    }, 10000);
}

function startDigitalRain() {
    for (let i = 0; i < 25; i++) {
        setTimeout(createRainColumn, i * 200);
    }
}

startDigitalRain();