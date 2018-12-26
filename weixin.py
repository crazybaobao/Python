# 微信自动回复

from wxpy import *

bot = Bot(cache_path=True)
myFriend = Bot.friends()


@bot.register(Friend)
def print_message(msg):
    print(msg.sender, msg.text)
    return '我正在忙，稍后回复'


embed()
