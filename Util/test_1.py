# @Time: 2019/2/26-10:50
# @Author: wangyun
# Windows下的Python开发
import time

from win32com import client

word = client.Dispatch("Word.Application")
print(word)

doc = word.Documents.Add()
print(doc)

word.Visible = True
time.sleep(5)
word.Visible = False
word = None


class Test(object):
    def __init__(self, val):
        self.val = val

    def split_string(self, sep=None):
        if sep is not None:
            sep = str(sep)
        return self.val.split(sep)


res = Test("Hello World").split_string()
print(res)
