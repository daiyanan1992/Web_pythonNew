# import win32gui
# import win32con
#
# #谷歌流量器上传文件操作
#
# def upload_file(filepath):
#     dialog = win32gui.FindWindow('#32770','打开') #一级窗口
#     comboxex32 = win32gui.FindWindowEx(dialog,0,'ComboBoxEX32',None)#二级窗口
#     combox = win32gui.FindWindowEx(comboxex32,0,'ComboBox',None)
#     edit = win32gui.FindWindowEx(combox,0,'Edit',None)
#
#     button = win32gui.FindWindowEx(dialog,0,'Button','打开(&0)')
#
#     #输入文件地址
#     win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)
#
#     #点击 打开按钮 提交文件
#     win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,)
import random

num = random.randint
print(num)