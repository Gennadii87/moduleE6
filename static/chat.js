const chatSocket = new WebSocket('ws/chat/');  //  'some_path' ваш путь WebSocket

chatSocket.onmessage = function(event) {
    const message = JSON.parse(event.data);
    const messageList = document.getElementById('message-list');
    const newMessage = document.createElement('li');
    newMessage.textContent = `${message.user.display_name}: ${message.content}`;
    messageList.appendChild(newMessage);
};

document.querySelector('#message-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const messageInputDom = document.getElementById('message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
});