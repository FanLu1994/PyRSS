# @Time    : 2022/3/10 20:54
# @Author  : fanlu
from db.db import engine
from model.model import Base

Base.metadata.create_all(engine)


