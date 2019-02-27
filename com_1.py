# @Time: 2019/2/22-17:30
# @Author: wangyun

import pythoncom
from win32com import client


class PythonUtilities(object):
    _public_methods_ = ['SplitString']
    _reg_progid_ = "Python.Utilities"
    _reg_clsid_ = str(pythoncom.CreateGuid())

    def SplitString(self, val):
        return ("hello" + str(val))


print("正在注册COM服务……")
import win32com.server.register

win32com.server.register.UseCommandLine(PythonUtilities)

s = win32com.client.Dispatch("Python.Utilities")
print(s)
print(s.SplitString("Hello World"))
