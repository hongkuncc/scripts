# -*- coding: utf-8 -*-
from wxpy import *

image_path = "./IMG20170224133007.jpg"
bot = Bot()

# #搜索名称含有""好友
# my_friend = bot.friends().search('陈飞',sex =MALE)[0]
# #发送消息
# my_friend.send('这是由python自动发送的消息！哈哈')
# my_friend.send_image(image_path)
# my_friend.send('@img@IMG20170224133007.jpg')
# embed()
friends = ['陈宏坤','曾美芳']
def send_to_friends(friends):
    for friend in friends:
        friend_search = bot.friends().search(friend)
        if (len(friend_search) ==1):
            friend_search[0].send_image(image_path)
        else:
            print("发生失败！"+friend)
send_to_friends(friends)
