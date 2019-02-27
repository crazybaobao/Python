from time import sleep

import win32com
from win32com import client


def word(person):
    words = win32com.client.Dispatch('Word.Application')
    doc = words.Documents.Add()
    words.Visible = True
    sleep(1)

    rng = doc.Range(0, 0)
    rng.InsertAfter(u'尊敬的%s:\n' % person)
    rng.InsertAfter(u'诚邀您加入我公司。')
    sleep(1)

    filename = name + ".doc"
    doc.SaveAs(filename)

    doc.Close(False)
    words.Application.Quit()


if __name__ == '__main__':
    names = ["tony", "peter", "jack"]
    for name in names:
        word(name)
