# @Time: 2019/2/26-15:43
# @Author: wangyun

from time import sleep
import win32com
from win32com import client


def excel(name):
    ex = win32com.client.Dispatch('Excel.Application')
    wk = ex.Workbooks.Add()
    nwk = wk.ActiveSheet
    ex.Visible = True
    sleep(1)

    nwk.Cells(1, 1).value = u'尊敬的%s:\n' % name
    nwk.Cells(1, 2).value = u'诚邀您加入我公司。'

    filename = name + ".xlsx"
    wk.SaveAs(filename)

    wk.Close(False)
    ex.Application.Quit()


if __name__ == '__main__':
    names = ["tony", "peter", "jack"]
    for name in names:
        excel(name)
