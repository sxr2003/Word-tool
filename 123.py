import random
import requests
import random
from hashlib import md5
import time
print("欢迎使用本系统！")
print("正在初始化，请稍后...")
time.sleep(0.5)
file = open('使用文档.txt',"r",encoding="utf-8")
sy = file.read()
file.close()
print(sy)
# Set your own appid/appkey.
appid = 'your appid'
appkey = 'your appkey'

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = 'en'
to_lang =  'zh'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path
# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def fanyi(query):
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    r = requests.post(url, params=payload, headers=headers)
    
    return  r.json()["trans_result"][0]["dst"]
# Send request

a = input("学习内容： 1 新单词训练 2 复习 3 综合训练\n")
if '1' == a:
    file = open('today.txt',"r")
    list1 = list(file.read().split("\n"))
    file.close()
if '2' == a:
    file = open('old.txt',"r")
    list1 = list(file.read().split("\n"))
    file.close()
if '3' == a:
    file = open('today.txt',"r")
    list1 = list(file.read().split("\n"))
    file.close()
    file = open('old.txt',"r")
    templist1 = list(file.read().split("\n"))
    file.close()
    list1.extend(templist1)
list2 = []
if input("修改过单词 y/n") == "y":
    print("正在翻译请稍后，翻译结束后会出现题目！")
    file = open('temp.txt','w')
    for i in list1:
        temp1 = fanyi(i)
        file.write(temp1+"\n")
        list2.append (temp1) 
        time.sleep(0.1)
    file.close()    
else :
    file = open('temp.txt',"r")
    list2 = list(file.read().split("\n"))
    file.close()
list4 = []
sun = 0
T  = 0
da = 0
time1 = time.time()
while da != 248:
    sun += 1
    # for i in list1[15:]:
    #     print(i)
    data = random.randint(0,len(list1)-1)
    
    data2 = random.randint(0,len(list1)-1)
    while data == data2:
        data2 = random.randint(0,len(list1)-1)
    data3 = random.randint(0,len(list1)-1)
    while data == data3:
        data3 = random.randint(0,len(list1)-1)
    data4 = random.randint(0,len(list1)-1)
    while data == data4:
        data4 = random.randint(0,len(list1)-1)

    print(list1[data])
    list3 = [list2[data2],list2[data3],list2[data4]]
    temp = random.randint(0,3)
    list3.insert(temp,list2[data])
    print(list3)
    time2 = time.time()
    da = int(input())
    if da < 5:
        if da == temp+1:
            T += 1
            print("正确！",end=" ")
        else:
            if not(list1[data] in list4):
                list4.append(list1[data])
            print("错误！",end=" ")
            print("答案:",list2[data],end=" ")
        print("准确率:",T/sun,end=" ")
        print("提问个数:",sun,end=" ")
        print("单题用时:",time.time()-time2,end=" ")
        print("总用时:",time.time()-time1,)
        
print("错词表:",list4)
input("按下回车结束！")
