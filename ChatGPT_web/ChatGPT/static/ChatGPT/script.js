const form = document.getElementById("userInput");
const input = document.getElementById("textInput");
const messages = document.getElementById("chatbox");

form.addEventListener("submit", async(e) =>{
    e.preventDefault();
    const message = input.value;
    input.value = "";
    messages.innerHTML += `<div class="message userMessage">
    <img src="${userImg}">
        <span>${message}</span>
    </div>`

    let chatbotResponse = 'no';
    try {
        const response = await axios.post('/chatbot_response/',{
            message: message,
        },
        {
            headers: {
              "Content-Type": "application/json",
            },
        });
        chatbotResponse = response.data.chatbotResponse;
    } catch (error) {
        console.error(error);
    }

    messages.innerHTML += `<div class="message botMessage">
    <img src="${botImg}">
        <span>${chatbotResponse}</span>
    </div>`;
})
