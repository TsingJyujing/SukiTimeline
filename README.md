# SukiTimeline
## 简介
Suki(好き)Timeline是一款时间轴Web工具，可以展示一条你定义的时间轴，使用Django(Python3)+SQLite3做到快速部署。
向你喜欢的人展示你们之间的故事吧！作为一名程序员只能帮我的同行兄弟们到这里了。
文档我会尽可能写全面一点的，如果你不会Python，那就去学吧！
如果你连学习Python这么简单的语言的勇气都没有，你凭什么喜欢那个姑娘？

## 快速上手
首先你需要一台 Linux 系统的主机，安装好 pip3。

随后安装以下依赖：

- itchat
- django
- pillow（PIL）
- imagehash

随后使用 `python3 manage.py runserver 0.0.0.0:8086` 即可运行程序。

使用以下账号登录管理界面：
- 地址：http://你的IP/admin
- 账号：admin
- 密码：sukitimeline

可以用来管理账号密码

## 启用微信快速加图功能
修改昵称范围之后，启动`wechat_loader.py`，按照指示登录，可以将收到的图片全部保存。注意发送的时候选择`原图`。

