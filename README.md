# momo-share

## 简介

最近在用`墨墨背单词`这个单词软件，各方面做的都很好。可惜存在单词上限，每背一个单词，就少一个，如果没有任何增加单词上限的途径的话，只能背500个单词你就可以删软件了。。

除了签到以及印章连连看的方式之外，还有没有增加上限的途径呢？是有的，就是每次打完卡之后可以对当日的学习情况进行分享。这个页面一旦被浏览过一次，你的单词上限就会+1（当然，一个ip只算一次），每日上限20个。于是我就写了一个自动刷访问量的脚本，原本是单线程的，很慢，后来再修改了一下弄成多线程的了。大体思路是：

1. 去免费代理ip网站爬代理
2. 利用代理访问文章
3. 增加访问量

多线程利用的自然是生产者-消费者模型。实现得有点简陋，正好最近在线程进程这边补缺补漏，就当练手了吧。

在linux下运行（unix或许也行

需要安装：

`pip3 install termcolor`

 MoMo-aiohttp.py在Py3.x下运行，需要安装aiohttp

`pip3 install aiohttp`

### 程序

`MoMo-aiohttp.py` 利用aiohttp实现的协程访问

## 运行示例

```bash
python3 -u MoMo-aiohttp.py ‘url‘
```

或者

```bash
./momo.sh ‘url’
```

 url需要改，怎么获得这个呢？首先你打卡之后，要分享到空间去，然后点开这个分享，转发链接到“我的电脑“，然后你就能看到这个url，大概是这样：
 https://www.maimemo.com/share/page/?uid=XXXXXXX&pid=1181&tid=2346527
 其中pid是每天都+1的，uid就是你的墨墨UID，在“我的设置“中可以看到
 设置好了之后再跑跑看

## 声明

本项目仅用于个人学习测试使用，勿用于非法用途，由于其他用途所产生的一切不良后果本人概不负责。

## 错误处理

如果出现以下报错，请关闭系统的代理再试一下。

```bash
» python MoMo-aiohttp.py
[+] get proxy...
  [-]Error: HTTPConnectionPool(host='127.0.0.1', port=7890): Max retries exceeded with url: http://www.89ip.cn/tqdl.html?num=100 (Caused by ProxyError('Cannot connect to proxy.', RemoteDisconnected('Remote end closed connection without response',)))
```

## 感谢

参考大佬![Macr0phag3](https://github.com/Macr0phag3/MoMo)的脚本改写和封装
