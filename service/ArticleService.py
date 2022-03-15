# @Time    : 2022/3/11 8:54
# @Author  : fanlu
from datetime import datetime

from model.model import RssArticle
from db.db import session, engine


class ArticleService:

    # 添加收藏文章
    def AddArticle(self, url, title, text):
        newRssArticle = RssArticle()

        newRssArticle.url = url
        newRssArticle.title = title
        newRssArticle.text = text
        now = datetime.now()
        newRssArticle.updateAt = now
        newRssArticle.createAt = now

        try:
            session.add(newRssArticle)
            session.commit()
        except Exception as e:
            print(e)

    # 获取所有rss
    def QueryAllArticles(self):
        return session.query(RssArticle).all()