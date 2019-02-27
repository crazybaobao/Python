# @Time: 2019/2/26-15:56
# @Author: wangyun

from time import sleep
import win32com
from win32com import client


def powerpoint(name):
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    pres = ppt.Presentations.Add()
    ppt.Visible = True
    sleep(1)

    s1 = pres.Slides.Add(1, 1)
    s1_0 = s1.Shapes[0].TextFrame.TextRange
    s1_0.Text = u'尊敬的%s:\n' % name
    s1_1 = s1.Shapes[1].TextFrame.TextRange
    s1_1.InsertAfter(u'诚邀您加入我公司。')

    filename = name + ".pptx"
    pres.SaveAs(filename)

    pres.Close(False)
    ppt.Application.Quit()


if __name__ == '__main__':
    names = ["tony", "peter", "jack"]
    for name in names:
        powerpoint(name)
