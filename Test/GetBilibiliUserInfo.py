from os import name
import re
import time
import json
import requests
from requests.api import patch


def getUserInfoText(mid):
    try:
        jsconnect = requests.session().get(
            'https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp' % mid
        ).text
        return jsconnect
    except ConnectionError:
        return False

def getUserFollowText(mid):
    try:
        jsconnect = requests.session().get(
            'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % mid
        ).text
        return jsconnect
    except ConnectionError:
        return False

def getUserInfo(mid):
    time1 = time.time()
    print('开始获取https://space.bilibili.com/%s用户数据' % mid)
    #连接bilibili网站获取用户信息
    userInfoText = getUserInfoText(mid)
    if userInfoText == False:
        print("连接失败")
        return False
    #获取用户关注数及粉丝数信息
    userFollowText = getUserFollowText(mid)
    if userFollowText == False:
        print("连接失败")
        return False

    try:
        #卸载用户信息数据
        jsDict = json.loads(userInfoText)
        userInfo = {}   
        #用户状态码 0：正常 -404：封禁
        userInfo['userStatue'] = jsDict['code']
        if userInfo['userStatue'] == 0:
            jsData = jsDict['data']
            #用户编号
            userInfo['userNO'] = jsData['mid']
            #姓名
            userInfo['name'] = jsData['name']
            #性别
            userInfo['sex'] = jsData['sex']
            #等级
            userInfo['level'] = jsData['level']
            #头像地址
            userInfo['facePicture'] = jsData['face']
            #签名
            if jsData['sign'] != '':
                userInfo['sign'] = jsData['sign']
            else:
                userInfo['sign'] = 'null'
            #注册时间，如果为0则赋值null
            regtimestamp = jsData['jointime']
            if regtimestamp == 0:
                userInfo['regtime'] = 'null'
            else:
                regtime_local = time.localtime(regtimestamp)
                userInfo['regtime'] = time.strftime("%Y-%m-%d %H:%M:%S", regtime_local)  
            #生日
            if jsData['birthday'] != '':
                userInfo['birthday'] = jsData['birthday']
            else:
                userInfo['birthday'] = 'null'

            #卸载用户关注数据及粉丝数据
            jsDict = json.loads(userFollowText)
            if userInfo['userStatue'] == 0:
                #关注人数
                userInfo['follows'] = jsDict['data']['following']
                #被关注人数
                userInfo['fans'] = jsDict['data']['follower']
            
            time2 = time.time()
            print("已获取数据，用时" + str(format(time2-time1, '2f')) + "秒")

        elif userInfo['code'] == -404:
            #用户编号
            userInfo['userNO'] = jsDict['data']['mid']
            #姓名
            userInfo['name'] = jsDict['data']['name']
            print("该用户已被封禁")

            time2 = time.time()
            print("已获取数据，用时" + str(format(time2-time1, '2f')) + "秒")
        else:
            print('没有此用户')



        return userInfo

    except Exception:
        print(Exception)

 



if __name__ == '__main__':
    for i in range(210400000, 210500000):
        print(getUserInfo(i))


