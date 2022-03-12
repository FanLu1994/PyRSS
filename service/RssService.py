# @Time    : 2022/3/10 20:25
# @Author  : fanlu
import feedparser
import requests

from model.model import RssSubInfo, Article
from db.db import session, engine
from datetime import datetime
import string

requestSession = requests.Session()
requestSession.trust_env = False

class RssService:

    # 添加rss
    def AddRss(self,title: string, url: string):
        newRssRecord = RssSubInfo()
        newRssRecord.title = title
        newRssRecord.url = url
        now = datetime.now()
        newRssRecord.updateAt = now
        newRssRecord.createAt = now
        newRssRecord.unreadCount = 0
        session.add(newRssRecord)
        session.commit()


    # 更新rss未读情况、更新时间
    def UpdateRss(self):
        pass


    # 删除rss
    def DelRss(self):
        pass


    # 获取所有rss
    def QueryAllRss(self):
        return session.query(RssSubInfo).all()


    def GetArticles(self,rss:RssSubInfo):
        articleList = []
        res = requestSession.get(rss.url, verify=False, timeout=5).text
        print(rss.url)
        print(res)
        dom = feedparser.parse(res)
        print(dom)
        for item in dom.get('entries'):
            a = Article(title=item['title_detail']['value'],
                                  url=item['link'],
                                  summary=item.get('summary_detail').get('value'))
            articleList.append(a)

        return articleList