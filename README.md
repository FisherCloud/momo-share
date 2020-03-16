# momo-share

## 简介

最近在用`墨墨背单词`这个单词软件，各方面做的都很好。可惜存在单词上限，每背一个单词，就少一个，如果没有任何增加单词上限的途径的话，只能背500个单词你就可以删软件了。。

除了签到以及印章连连看的方式之外，还有没有增加上限的途径呢？是有的，就是每次打完卡之后可以对当日的学习情况进行分享。这个页面一旦被浏览过一次，你的单词上限就会+1（当然，一个ip只算一次），每日上限20个。

程序大体思路是：

1. 去免费代理ip网站爬代理
2. 利用代理访问文章
3. 增加访问量

在linux下运行，我用的Windows的Linux子系统（Ubuntu18.04）（Windows和Unix或许也行）

使用python3，需要安装：

`pip3 install termcolor`

`pip3 install aiohttp`利用aiohttp实现的协程访问（只适用于python3）

`pip3 install requests`

`pip3 install bs4`

## 运行示例

```bash
python3 -u momo-share.py
```

## 声明

本项目仅用于个人学习测试使用，勿用于非法用途，由于其他用途所产生的一切不良后果本人概不负责。

## 感谢

参考大佬[Macr0phag3](https://github.com/Macr0phag3/MoMo)的脚本改写和封装

## 2019-11-30

发现大量的代理ip不能够访问，已添加ip-proxy.py用于爬取可用代理ip，但还未重新修改momo-share.py。（待抽空再改）

## 2020-03-16

已更新，`momo-share.py`，由于爬取ip代理测试过多，导致我MAC被封了，暂时没有测试，`momo-share-bak.py`只做了简单修改，使用以往一样
