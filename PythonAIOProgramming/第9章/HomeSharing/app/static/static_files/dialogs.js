//第9章/HomeSharing/app/static/static_files/dialogs.js
(function () {
    window.dialogs = window.dialogs || {};

    /**
     * 呈现正在加载中对话框，该功能运行需要 Bootstrap
     * @param {*} msg 
     */
    dialogs.showLoading = function (msg) {
        return $(`<div class="modal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <div class="spinner-border" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>
      <div class="modal-body">
        <p>${msg}</p>
      </div>
    </div>
  </div>
</div>`).modal({
            keyboard: false,
            backdrop: "static",
        }).appendTo(document.body).on("hide.bs.modal", function (e) {
            $(this).remove();
        });
    };


    /**
     * 呈现一个消息对话框，该功能运行需要 Bootstrap
     */
    dialogs.showMessageDialog = function (msg, title = "", closeCallback, closeBtnClass = "btn-danger") {
        return $(`<div class="modal fade" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">${title}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        ${msg}
      </div>
      <div class="modal-footer">
        <button type="button" class="btn ${closeBtnClass}" data-dismiss="modal">关闭</button>
      </div>
    </div>
  </div>
</div>`).modal({
            keyboard: true,
            backdrop: true,
        }).appendTo(document.body).on("hide.bs.modal", function (e) {
            $(this).remove();
            if (closeCallback) {
                closeCallback();
            }
        });
    };
})();