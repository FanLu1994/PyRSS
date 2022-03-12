# @Time    : 2022/3/9 8:14
# @Author  : fanlu
# 添加新博客的弹窗

import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, \
    QComboBox, QListView,QVBoxLayout,QLineEdit,QGridLayout,QPushButton,QLabel

from qt_material import apply_stylesheet


class AddBlogDialog(QWidget):
    def __init__(self):
        super(AddBlogDialog, self).__init__()
        self._initUI()

    def _initUI(self):

        gLayout = QGridLayout()
        gLayout.setColumnStretch(0,1)
        gLayout.setColumnStretch(1,1)
        gLayout.setColumnStretch(2,1)
        gLayout.setColumnStretch(3,1)
        gLayout.setColumnStretch(4,1)

        gLayout.setRowStretch(0,1)
        gLayout.setRowStretch(1,1)
        gLayout.setRowStretch(2,1)
        gLayout.setRowStretch(3,1)
        gLayout.setRowStretch(4,1)

        urlInputBox = QLineEdit()
        confirmBtn = QPushButton("确认")
        quitButton = QPushButton(QIcon("../assets/quit.png"),"")

        quitButton.clicked.connect(self.close)
        quitButton.setFlat(True)
        # quitButton.setMaximumSize(QSize(50,50))

        resultLabel = QLabel("success")

        gLayout.addWidget(quitButton,0,4,)
        gLayout.addWidget(urlInputBox,2,1,1,3)
        gLayout.addWidget(resultLabel,3,1,1,1)
        gLayout.addWidget(confirmBtn,3,3,1,1)
        gLayout.setContentsMargins(2,2,2,2)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setLayout(gLayout)
        self.setWindowTitle("添加订阅")
        self.setWindowIcon(QIcon("../assets/add.png"))

    def _checkUrl(self):
        pass


    def _setResult(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    window = AddBlogDialog()
    window.resize(640,320)
    window.show()
    sys.exit(app.exec_())