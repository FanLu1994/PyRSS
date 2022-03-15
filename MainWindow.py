# @Time    : 2022/3/5 22:03
# @Author  : fanlu
#  客户端主窗口定义
import sys
from typing import List

import feedparser
import requests
from PyQt5.QtCore import QUrl, Qt, QModelIndex
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, \
    QComboBox, QListView, QApplication, QDesktopWidget, \
    QPushButton, QWidget, QAction, QMenu, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon, QClipboard, QGuiApplication
from PyQt5 import QtWidgets, QtGui
from qt_material import apply_stylesheet
import traceback

from model.model import RssSubInfo, RssArticle
from service.ArticleService import ArticleService
from ui.BlogContent import BlogContent
from ui.Navbar import Navbar
from ui.AddBlogDialog import AddBlogDialog
from service.RssService import RssService

rssService = RssService()
articleService = ArticleService()


class PyRSSMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.blogList = []
        self.articleList = []

        self.centerWidget = QWidget()
        self.addBlogDialog = AddBlogDialog()
        self.currentArticle = ''
        self.currentArticleInfo = RssArticle()
        self._initUI()
        self._initBlogList()

    def _initUI(self):
        # 左侧导航
        self.navBar = Navbar()

        self.blogContent = BlogContent()

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.navBar)
        mainLayout.addWidget(self.blogContent)

        self.navBar.setAddButtonClickFunction(self._addBlog)
        self.navBar.setShareButtonClickFunction(self._shareArticle)
        self.navBar.setCollectButtonClickFunction(self._collectArticle)
        self.navBar.setClickedFunction(self._onSelectBlog)
        self.navBar.setArticleSelectFunction(self._onSelectArticle)
        self.navBar.setCancleSubButtonClickFunction(self._onClickCancelSub)
        self.addBlogDialog.setConfirmButtonClickFunction(self._onClickAddSubConfirmButton)

        mainLayout.setStretch(0, 1)
        mainLayout.setStretch(1, 3)
        mainLayout.setSpacing(5)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        self.centerWidget.setLayout(mainLayout)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setCentralWidget(self.centerWidget)
        self.resize(1320, 640)
        self._center()
        self.setWindowIcon(QIcon("assets/read.png"))
        self.setWindowTitle("PyRSS")

    # 暂时关闭
    def _setMenu(self):
        addAction = QAction(QIcon("assets/add.png"), '&添加订阅', self)
        addAction.triggered.connect(self._addBlog)
        collectAction = QAction(QIcon("assets/add.png"), '&添加订阅', self)
        menuBar = self.menuBar()
        menuBar.addAction(addAction)

    def _center(self):
        qr = self.frameGeometry()  # 获得主窗口所在框架
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器中间点位置
        qr.moveCenter(cp)
        self.move(qr.topLeft())  # 把主窗口左上角移动到框架的左上角

    # 初始化文章列表
    def _initBlogList(self):
        try:
            self.blogList = rssService.QueryAllRss()
            self.navBar.updateBlogList(self.blogList)
            if len(self.blogList) > 0:
                self._onSelectBlog(0)
        except Exception as e:
            self.navBar.updateBlogList([])
            print(e)

    # 收藏博客
    def _collectArticle(self):
        articleService.AddArticle(self.currentArticle,
                                  self.currentArticleInfo.title,
                                  '')
        QMessageBox.information(self, "提示", "收藏成功")



    def _shareArticle(self):
        try:
            QGuiApplication.clipboard().setText( f"{self.currentArticle} \n分享来自PyRSS", mode=QClipboard.Clipboard)
            QMessageBox.information(self, "提示", "已复制到剪贴板")
        except Exception as e:
            print(e)
            traceback.print_exc()
            QMessageBox.about(self, "提示", "分享失败")

    # 博客选择回调事件
    def _onSelectBlog(self, index):
        self.currentBlog = self.blogList[index]
        try:
            articleList = rssService.GetArticles(self.blogList[index])
            self.articleList = articleList
            self.navBar.updateArticleList(self.articleList)
            if len(self.articleList) > 0:
                self.currentArticle = self.articleList[0].url
                self.blogContent.setUrl(self.currentArticle)
        except Exception as e:
            self.navBar.updateArticleList([])
            print(e)

    # 添加博客事件
    def _addBlog(self):
        self.addBlogDialog.resize(640, 320)
        self.addBlogDialog.show()

    # 文章列表点击事件
    def _onSelectArticle(self, index: QModelIndex):
        # self.currentArticle = self.articleList[index.row()].summary
        self.currentArticleInfo = self.articleList[index.row()]
        self.currentArticle = self.articleList[index.row()].url
        self.blogContent.setUrl(self.currentArticle)

    # 删除订阅响应事件
    def _onClickCancelSub(self):
        result = QMessageBox.warning(self, "提示", "确定取消订阅？", QMessageBox.Yes, QMessageBox.No)
        if result == QMessageBox.Yes:
            rssService.DelRss(self.currentBlog)
            self._initBlogList()

    # 添加订阅按钮响应事件
    def _onClickAddSubConfirmButton(self):
        # 获取输入内容
        rssUrl = self.addBlogDialog.getInputContent()
        print(rssUrl)
        # 检查输入内容
        try:
            requestSession = requests.Session()
            requestSession.trust_env = False
            result = requestSession.get(rssUrl, verify=False, timeout=5).text
            dom = feedparser.parse(result)
            self.addBlogDialog.setConfirmResult(isSuccess=True)
            rssService.AddRss(dom['feed']['title'],url=rssUrl)
            self._initBlogList()
            self.navBar.setCurrentBlog(len(self.blogList)-1)
            self._onSelectBlog(len(self.blogList)-1)
        except Exception as e:
            print(e)
            self.addBlogDialog.setConfirmResult(isSuccess=False)


if __name__ == '__main__':
    extra = {
        'font_family': 'Roboto',
        'font_size': 15,
    }

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml', extra=extra)

    window = PyRSSMainWindow()
    window.show()
    sys.exit(app.exec_())
