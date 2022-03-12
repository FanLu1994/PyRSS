# @Time    : 2022/3/7 21:42
# @Author  : fanlu


import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, \
    QListView,QVBoxLayout,QHBoxLayout,QPushButton
from qt_material import apply_stylesheet




class BlogContent(QWidget):
    def __init__(self):
        super(BlogContent, self).__init__()
        self._initUI()


    def _initUI(self):
        vLayout = QVBoxLayout()

        toolBarLayout = QHBoxLayout()
        self.content = QWebEngineView()
        self.content.setUrl(QUrl("https://www.baidu.com"))

        vLayout.addLayout(toolBarLayout)
        vLayout.addWidget(self.content)
        vLayout.setSpacing(0)
        vLayout.setContentsMargins(0,0,0,0)

        self.setLayout(vLayout)
        # self.show()

    def setHtml(self,html):
        self.content.setHtml(html)

    def setUrl(self, url):
        self.content.setUrl(QUrl(url))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    window = BlogContent()
    window.setFont(QFont("SimHei",30,18,False))
    window.show()
    sys.exit(app.exec_())