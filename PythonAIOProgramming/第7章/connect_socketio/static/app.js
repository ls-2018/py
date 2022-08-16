// 第7章/connect_socketio/static/app.js

(function () {
    let socket = io();

    let output = document.querySelector("#output");

    // 侦听服务器端的 my_event_callback 事件
    socket.on("my_event_callback", e => {
        output.innerHTML += `[${Date.now()}] my_event_callback from server<br>`;
    });

    document.querySelector(".btn_my_event").onclick = e => {
        // 向服务器派发 my_event 事件
        socket.emit("my_event");
    };

    document.querySelector(".btn_login").onclick = e => {
        // 向服务器发送登录事件，并将回调函作为最后一个参数
        socket.emit("login", { name: "yunp" }, result => {
            output.innerHTML += `[${Date.now()}] ${result}<br>`;
        });
    };
})();