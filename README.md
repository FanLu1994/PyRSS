# PyRSS
Build  rss reader with  PyQt

# look like this

![软件截图](https://github.com/FanLu1994/PyRSS/blob/main/screenshot/Snipaste_2022-03-15_21-14-18.png)


> 本来的想法是用PyQt实现一个蚁阅那样的一个rss阅读器。一方面做一个PyQt的练习，一方面现在的rss阅读器客户端不太好用。


使用到的技术

- pyqt
- sqlalchemy
- sqlite
- qt_material
- feedparser

## 源码地址

[https://github.com/FanLu1994/PyRSS](https://github.com/FanLu1994/PyRSS)

## 下载地址

[https://github.com/FanLu1994/PyRSS/releases/download/v0.0.2/PyRss.exe](https://github.com/FanLu1994/PyRSS/releases/download/v0.0.2/PyRss.exe)

## 页面设计

页面主要分成两大块，一个是左边的导航部分，一个是右边的展示部分

导航分为：博客选择框；文章列表；功能按钮

展示部分是一个QWebEngineView，用来作为url或者html的展示容器

还有一个小组件，是添加订阅的一个弹窗。

- 主界面将导航和展示部分引入，使用QHboxLayout() 水平布局,设置左右两边宽度比为1：3

```Python
 mainLayout.setStretch(0, 1)
 mainLayout.setStretch(1, 3)
```


- 去除边框

```Python
 mainLayout.setContentsMargins(0, 0, 0, 0)
```


- 打开主页面时居中

```Python
  def _center(self):
      qr = self.frameGeometry()  # 获得主窗口所在框架
      cp = QDesktopWidget().availableGeometry().center()  # 获取显示器中间点位置
      qr.moveCenter(cp)
      self.move(qr.topLeft())  # 把主窗口左上角移动到框架的左上角
```




原生的pyqt UI挺丑的，因此选择使用了一个qt_material的ui库，并且支持自定义的一些样式

```Python
extra = {
  'font_family': 'Roboto',
  'font_size': 15,
}

app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_blue.xml', extra=extra)
```




## 主要功能

- 打开时默认选中第一条博客、第一篇文章
- 选择博客后，默认打开第一篇文章
- 点击文章，在右边显示
- 收藏当前文章
- 添加订阅
- 删除当前订阅
- 分享-复制当前的文章地址

## 遇到的问题

1. request 被本地挂的梯子影响

   ```Python
   requestSession = requests.Session()
   requestSession.trust_env = False
   res = requestSession.get(rss.url, verify=False, timeout=5).text
   ```

2. 弹窗的显示
   参考： [https://blog.csdn.net/weixin_40520077/article/details/104040414](https://blog.csdn.net/weixin_40520077/article/details/104040414)

## 打包

- 使用pyinstaller进行打包
- 打包后图片资源找不到了，解决办法是将图片转换为base64放在py代码中，用到的地方再将其转换成QPixmap



