const output = document.getElementById('output');
const userInput = document.getElementById('user-input');
const submitBtn = document.getElementById('submit-btn');

function addMessage(message, isUser = false) {
    const messageElement = document.createElement('div');
    messageElement.textContent = isUser ? `> ${message}` : message;
    output.appendChild(messageElement);
    output.scrollTop = output.scrollHeight;
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (message) {
        addMessage(message, true);
        userInput.value = '';
    }

    try {
        const response = await fetch('http://localhost:8000/api/root', {
            method: 'POST',  // Cambiado a POST
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),  // Enviar el mensaje en el cuerpo
        });

        if (response.ok) {
            const data = await response.json();
            addMessage(data.message);  // Mostrar la respuesta recibida de la API
        } else {
            addMessage('Error: Unable to get response from API');
        }
    } catch (error) {
        addMessage('Error: ' + error.message);
    }
}

submitBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Initial welcome message
addMessage("Welcome to the Matrix Terminal. Type your message and press Enter.");

function toggleLogoutForm() {
    var logoutForm = document.getElementById('logout-form-container');
    logoutForm.style.display = logoutForm.style.display === 'none' ? 'block' : 'none';
}

// Close the logout form if clicked outside
document.addEventListener('click', function(event) {
    var logoBtn = document.getElementById('logo-btn');
    var logoutForm = document.getElementById('logout-form-container');
    if (!logoBtn.contains(event.target) && !logoutForm.contains(event.target)) {
        logoutForm.style.display = 'none';
    }
});

