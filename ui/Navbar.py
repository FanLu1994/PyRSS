# @Time    : 2022/3/7 9:10
# @Author  : fanlu
import sys
from typing import List

from PyQt5.QtGui import QFont, QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, \
    QListView, QVBoxLayout, QPushButton, QMessageBox, QAbstractItemView
from qt_material import apply_stylesheet
from model.model import RssSubInfo, Article
from ui.AddBlogDialog import AddBlogDialog

class Navbar(QWidget):
    def __init__(self):
        super(Navbar, self).__init__()
        self.addButton = QPushButton("添加订阅")
        self.cancleSubButton = QPushButton("取消订阅")
        self.collectButton = QPushButton("收藏")
        self.shareButton = QPushButton("分享")
        self._initButton()
        self._initUI()

    def _initButton(self):
        self.addButton = QPushButton(QIcon("assets/add.png"),"添加订阅")
        self.collectButton = QPushButton(QIcon("assets/collect.png"),"收藏")
        self.shareButton = QPushButton(QIcon("assets/share.png"),"分享")
        self.cancleSubButton = QPushButton(QIcon("assets/cancle.png"),"取消订阅")
        self.addButton.setFixedHeight(20)
        self.collectButton.setFixedHeight(20)
        self.shareButton.setFixedHeight(20)
        self.cancleSubButton.setFixedHeight(20)

    def _initUI(self):
        self.resize(200,640)

        vLayout = QVBoxLayout()

        self.blogSelector = QComboBox(self)
        self.blogSelector.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLength)

        self.blogList = QListView(self)
        self.blogList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.blogList.setSpacing(1)

        vLayout.addWidget(self.blogSelector)
        vLayout.addWidget(self.blogList)
        vLayout.addWidget(self.addButton)
        vLayout.addWidget(self.collectButton)
        vLayout.addWidget(self.shareButton)
        vLayout.addWidget(self.cancleSubButton)
        vLayout.setContentsMargins(2,2,2,2)

        self.setLayout(vLayout)
        # self.show()

    # 更新博客列表
    def updateBlogList(self, blogList: List[RssSubInfo]):
        blogNames = []
        for blog in blogList:
            blogNames.append(blog.title)
        self.blogSelector.clear()
        self.blogSelector.addItems(blogNames)

    # 更新文章列表
    def updateArticleList(self,articleList:List[Article]):
        articleNames = QStandardItemModel()
        for article in articleList:
            articleNames.appendRow(QStandardItem(article.title))

        self.blogList.setModel(articleNames)

    # 列表添加点击事件
    def setClickedFunction(self,func):
        self.blogSelector.activated.connect(func)

    # 博客点击事件
    def setArticleSelectFunction(self,func):
        self.blogList.clicked.connect(func)

    # 删除订阅点击事件
    def setCancleSubButtonClickFunction(self,func):
        self.cancleSubButton.clicked.connect(func)

    # 分享事件
    def setShareButtonClickFunction(self,func):
        self.shareButton.clicked.connect(func)

    # 收藏点击事件
    def setCollectButtonClickFunction(self,func):
        self.collectButton.clicked.connect(func)

    # 添加点击事件
    def setAddButtonClickFunction(self,func):
        self.addButton.clicked.connect(func)

    # 设置当前选项
    def setCurrentBlog(self,index):
        self.blogSelector.setCurrentIndex(index)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    window = Navbar()
    window.setFont(QFont("SimHei",30,18,False))
    window.show()
    sys.exit(app.exec_())