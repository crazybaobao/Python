# @Time: 2019/2/26-16:13
# @Author: wangyun

import win32com
from win32com import client


def outlook(name):
    outlook = win32com.client.Dispatch('Outlook.Application')
    mail = outlook.createItem(0)
    mail.Recipients.Add('94291333@qq.com')
    mail.Subject = u'邀请函'
    body = u'尊敬的%s:\n' % name
    # body.append(u'诚邀您加入我公司。')

    mail.Body = body
    mail.Send()

    outlook.Quit()


if __name__ == '__main__':
    names = ["tony", "peter", "jack"]
    for name in names:
        outlook(name)
