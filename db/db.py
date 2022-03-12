# @Time    : 2022/3/10 20:23
# @Author  : fanlu

import sqlite3
from sqlalchemy import create_engine
from model.model import RssSubInfo,Base
from sqlalchemy.orm import relationship, sessionmaker, backref
from datetime import datetime

engine = create_engine('sqlite:///app.db', echo=True)
session = sessionmaker(engine)()


def testInsert():
    rssinfo = RssSubInfo()
    rssinfo.unreadCount = 10
    rssinfo.createAt = datetime.now()
    rssinfo.updateAt = datetime.now()
    rssinfo.url = "haha"
    rssinfo.title = "test"
    session.add(rssinfo)
    session.commit()


if __name__ == '__main__':
    testInsert()