# @Time    : 2022/3/10 20:24
# @Author  : fanlu
import string

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime


Base = declarative_base()

class RssSubInfo(Base):
    __tablename__ = 'rss_sub_info'

    id = Column(Integer,primary_key=True)
    url = Column(String(50))
    title = Column(String(50))
    unreadCount = Column(Integer)
    updateAt = Column(DateTime)
    createAt = Column(DateTime)


    def __repr__(self):
        return "<RssSubInfo(id='%s', url='%s', title='%s',unreadCount='%s')>" % (
                   self.id, self.url, self.title,self.unreadCount)


class RssArticle(Base):
    __tablename__ = 'rss_article'

    id = Column(Integer, primary_key=True)
    rssId = Column(Integer)
    url = Column(String(50))
    title = Column(String(50))
    text = Column(String(50))

    def __repr__(self):
        return "<RssArticle(id='%s',rssId='%s', url='%s', title='%s',text='%s')>" % (
                   self.id, self.rssID,self.url,self.title,self.text)


class Article:
    def __init__(self,title:string,url:string,summary:string):
        self.title=title
        self.url = url
        self.summary = summary