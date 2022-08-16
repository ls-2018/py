// 第7章/chatroom/static/app.js

(function () {

    let input, output, btnSend;
    let socket;

    function findElements() {
        input = document.querySelector("#input");
        output = document.querySelector("#output");
        btnSend = document.querySelector("#btn-send");
    }

    function tryToSendMsg() {
        let msg = input.value;
        if (msg) {
            // 向服务器发送消息
            socket.emit("msg", msg);
            // 清空输入框
            input.value = "";
        }
    }

    function btnSend_clickedHandler() {
        tryToSendMsg();
    }

    function input_keyupHandler(e) {
        // 按下回车键时发送数据
        if (e.key == "Enter") {
            tryToSendMsg();
        }
    }

    /**
     * 处理 msg 事件
     * @param {*} msg 服务器发来的消息
     */
    function socket_msgHandler(msg) {
        output.innerHTML += `${msg.from}: ${msg.content}<br>`;

        // 将文字滚动到底端
        output.scrollTop = output.scrollHeight;
    }

    function addListeners() {
        btnSend.onclick = btnSend_clickedHandler;
        input.onkeyup = input_keyupHandler;

        // 侦听服务器发来的 msg 事件
        socket.on("msg", socket_msgHandler);
    }

    function connectServer() {
        /* 
        连接服务器， Socket.IO默认连接的路径是 /socket.io，可通过
        io({path:"/rt"}) 这种方式修改要连接的路径，则对应的服务器
        端也应该将服务器启动在 /rt 路径上，则对应的 Python ASGI应用
        代码类似 app = socketio.ASGIApp(sio,socketio_path="/rt")
        */ 
        socket = io();
    }

    function main() {
        findElements();
        connectServer();
        addListeners();
    };

    main();
})();