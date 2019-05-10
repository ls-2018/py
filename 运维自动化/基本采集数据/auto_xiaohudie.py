# 学校小蝴蝶网络断开，自动重连
# import os
# import win32gui
#
#
# def findAppHandle():
#     appNmae = '宽带认证客户端(32位)'
#     hwnd = win32gui.FindWindow(None, appNmae)
#     print(hwnd)
#
#
# findAppHandle()
from pywinauto import Desktop, Application

Application().start('C:\Program Files (x86)\校园网认证客户端\supplicant.exe')
""
# connect to another process spawned by explorer.exe
# Note: make sure the script is running as Administrator!
app = Application(backend="uia").connect(path="explorer.exe", title="Program Files")

app.ProgramFiles.set_focus()
common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
common_files.right_click_input()
app.ContextMenu.Properties.invoke()

# this dialog is open in another process (Desktop object doesn't rely on any process id)
Properties = Desktop(backend='uia').Common_Files_Properties
Properties.print_control_identifiers()
Properties.Cancel.click()
Properties.wait_not('visible')  # make sure the dialog is closed
