# @Time: 2019/3/1-9:45
# @Author: wangyun


# hello = type("Hello", (object,), {"name": "Hero"})
#
#
# def hi(self):
#     if self.name == "Hero":
#         return "Hi  Hero"
#     else:
#         return "what is you name?"
#
#
# setattr(hello, "hi", hi)
#
# print(hello().hi())


# class Hello:
#     def __init__(self):
#         name = "Hero"
#
#
# a = Hello()
# a.name = "haha"
# print(a.name)
#
# b = Hello()
# print(b.name)

class Hello:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Hello, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

    def __eq__(self, other):
        return type(self) == type(other)


h1 = Hello()
h2 = Hello()

print(h1 is h2)
