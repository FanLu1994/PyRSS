# @Time    : 2022/3/14 12:55
# @Author  : fanlu
import feedparser
import requests


headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5'
}
result = requests.get("http://feed.smzdm.com/",headers=headers).text
print(result)
dom = feedparser.parse(result)
print(dom)