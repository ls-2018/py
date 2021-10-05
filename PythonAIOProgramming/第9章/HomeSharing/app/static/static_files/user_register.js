// 第9章/HomeSharing/app/static/static_files/user_register.js

(function () {

    var alertMsgDiv = document.querySelector("#form-register .alert-msg");

    document.querySelector("#form-register").onsubmit = function (e) {
        if (this['password_confirm'].value != this['password'].value) {
            e.preventDefault();
            alertMsgDiv.innerHTML = "确认密码不一致";
        }
    };
})();