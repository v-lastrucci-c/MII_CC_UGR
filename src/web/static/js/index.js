const output = document.getElementById('output');
const userInput = document.getElementById('user-input');
const submitBtn = document.getElementById('submit-btn');

// Logger básico
function logger(level, message) {
    const timestamp = new Date().toISOString();
    console[level](`[${timestamp}] ${level.toUpperCase()}: ${message}`);
}

function addMessage(message, isUser = false) {
    logger("info", `Adding message: ${message}`, { isUser });
    const messageElement = document.createElement('div');
    messageElement.textContent = isUser ? `> ${message}` : message;
    output.appendChild(messageElement);
    output.scrollTop = output.scrollHeight;
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (message) {
        addMessage(message, true);
        logger("info", "User message sent", { message });
        userInput.value = '';
    }

    const apiEndpoint = `${apiBaseUrl}/api/v1/health`;

    try {
        logger("info", "Sending message to API", { url: apiEndpoint, message });
        const response = await fetch(apiEndpoint,
            // {
            //     method: 'GET', // Cambiado a POST
            //     headers: {
            //         'Content-Type': 'application/json',
            //     },
            //     body: JSON.stringify({ message }),
            // }
        );

        if (response.ok) {
            const data = await response.json();
            logger("info", "Received response from API", { response: data });
            addMessage(data.message); // Mostrar la respuesta recibida de la API
        } else {
            logger("error", "Failed to get response from API", { status: response.status });
            addMessage('Error: Unable to get response from API');
        }
    } catch (error) {
        logger("error", "Error during API call", { error: error.message });
        addMessage("La API no está disponible en este momento, pruebe de nuevo más tarde.");
    }
}

submitBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        logger("info", "Enter key pressed");
        sendMessage();
    }
});

// Initial welcome message
logger("info", "Initializing application");
addMessage("Welcome to the Matrix Terminal. Type your message and press Enter.");

function toggleLogoutForm() {
    var logoutForm = document.getElementById('logout-form-container');
    const isHidden = logoutForm.style.display === 'none';
    logoutForm.style.display = isHidden ? 'block' : 'none';
    logger("info", `Toggled logout form`, { isHidden });
}

// Close the logout form if clicked outside
document.addEventListener('click', function (event) {
    var logoBtn = document.getElementById('logo-btn');
    var logoutForm = document.getElementById('logout-form-container');
    if (!logoBtn.contains(event.target) && !logoutForm.contains(event.target)) {
        logoutForm.style.display = 'none';
        logger("info", "Closed logout form due to outside click");
    }
});
