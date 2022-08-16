//第9章/HomeSharing/app/static/static_files/admin_groups.js
(function () {

    /**
     * 呈现添加组对话框
     * @param {*} group_id 
     * @param {*} description 
     */
    function showAddGroupDialog() {
        var d = $(`<div class="modal fade" tabindex="-1" role="dialog">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">编辑组介绍</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
          <table class="table table-borderless">
            <tbody>
              <tr>
                <td>组名</td>
                <td><input name="role" class="form-control"></td>
              </tr>
              <tr>
                <td>说明</td>
                <td>
                  <textarea rows="5" name="description" 
                    class="form-control"></textarea>
                </td>
              </tr>
            </tbody>
          </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
        <button type="button" class="btn btn-primary btn-save">保存</button>
      </div>
    </div>
  </div>
</div>`).modal({
            keyboard: true,
            backdrop: true,
        }).appendTo(document.body).on("hide.bs.modal", function (e) {
            $(this).remove();
        });

        let descriptionInput = d.find("textarea[name='description']");
        let roleInput = d.find("input[name='role']");

        function addListeners() {
            d.find(".btn-save").click(function () {
                let description = descriptionInput.val();
                let role = roleInput.val();

                if (!role) {
                    dialogs.showMessageDialog("请填写组名");
                    return;
                }

                $.post(
                    "/admin/edit_group",
                    { role: role, description: description }
                ).done(data => {
                    if (data == "ok") {
                        location.reload();
                    } else {
                        dialogs.showMessageDialog("编辑失败", "提示");
                    }
                }).fail(e => {
                    dialogs.showMessageDialog("连接服务器失败", "提示");
                });
            });
        }

        function init() {
            addListeners();
        }

        init();
        return d;
    }

    /**
     * 呈现编辑组信息对话框
     * @param {*} group_id 
     * @param {*} description 
     */
    function showEditGroupDialog(group_id, description) {
        var d = $(`<div class="modal fade" tabindex="-1" role="dialog">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">编辑组介绍</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
          <textarea rows="5" name="description" 
              class="form-control">${description}</textarea>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
        <button type="button" class="btn btn-primary btn-save">保存</button>
      </div>
    </div>
  </div>
</div>`).modal({
            keyboard: true,
            backdrop: true,
        }).appendTo(document.body).on("hide.bs.modal", function (e) {
            $(this).remove();
        });

        let contentInput = d.find("textarea[name='description']");


        function addListeners() {
            d.find(".btn-save").click(function () {
                $.post(
                    "/admin/edit_group",
                    { group_id: group_id, description: contentInput.val() }
                ).done(data => {
                    if (data == "ok") {
                        location.reload();
                    } else {
                        dialogs.showMessageDialog("编辑失败", "提示");
                    }
                }).fail(e => {
                    dialogs.showMessageDialog("连接服务器失败", "提示");
                });
            });
        }

        function init() {
            addListeners();
        }

        init();
        return d;
    }

    function setStyles() {
        $(".table").addClass("table-bordered");
    }

    function addListeners() {
        $(".btn-add-group").click(showAddGroupDialog);
        $(".btn-edit-group").click(e => {
            showEditGroupDialog(
                $(e.target).data("group_id"),
                $(e.target).data("group_description")
            );
        });
    }

    function main() {
        setStyles();
        addListeners();
    }

    main();
})();