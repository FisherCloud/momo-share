#encoding: utf8
import re
import sys
import time
import random
import aiohttp
import asyncio
import datetime
import requests
import threading
from termcolor import colored
from bs4 import BeautifulSoup


class momo_share:
    def __init__(self, url='', TargetNum=20, proxynum=100):
        super().__init__()
        # self.header = ""
        # self.proxies = []
        # self.ProxyList = []
        # self.proxynum = proxynum
        # self.TargetNum = TargetNum
        # self.url = url
        # self.completion = 0
        pass

    # ----------------------------------------------------------------------------------------------------------------------
    # 返回一个随机的请求头 headers
    def getheaders(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        UserAgent = random.choice(user_agent_list)
        headers = {'User-Agent': UserAgent}
        return headers

    # def getProxy(self):
    #     if self.completion >= self.TargetNum:
    #         return 0
    #     # print('[+] %s' % colored('get proxy...', 'blue', attrs=['bold']), end='')

    #     while 1:
    #         try:
    #             purl = 'http://www.89ip.cn/tqdl.html?num=%s' % self.proxynum
    #             resp = requests.get(purl, headers=self.header)
    #             html = resp.text

    #             self.proxies = set(re.findall(
    #                 r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]+", html)) - set(self.ProxyList)

    #             if not len(self.proxies):
    #                 # print('\n  [-]Waiting')
    #                 time.sleep(1)
    #                 continue

    #             # print(colored('[%d]' % len(self.proxies), 'yellow', attrs=['bold']), '%s' % (colored('Done!', 'green', attrs=['bold'])))
    #             return 1
    #         except Exception as e:
    #             # print('\n  [-]Error: ' + str(e))
    #             time.sleep(random(1, 3))
    #             pass

    # async def autoVisit(self, proxy, sem):
    #     async with sem:
    #         async with aiohttp.ClientSession() as session:
    #             try:
    #                 async with session.get(url=url, proxy='http://' + proxy, timeout=5) as resp:
    #                     # print('[%s]' % colored(proxy, 'cyan', attrs=['bold']), colored('Successfully!', 'green', attrs=['bold']), '[%s]' % colored(self.completion+1, 'blue', attrs=['bold']))
    #                     pass
    #                 self.ProxyList.append(proxy)
    #                 self.completion += 1
    #             except Exception as e:
    #                 pass
    #                 # print('[%s]' % proxy, colored('Failed!', 'red', attrs=['bold']))

    # def run(self):
    #     if '' != self.url:
    #         self.header = self.getheaders()  # 获取一个请求头
    #         loop = asyncio.get_event_loop()
    #         sem = asyncio.Semaphore(self.proxynum)
    #         while self.getProxy():
    #             tasks = [asyncio.ensure_future(
    #                 self.autoVisit(i, sem)) for i in self.proxies]
    #             loop.run_until_complete(asyncio.wait(tasks))
    #         loop.close()
    #         # print(colored(self.completion, 'yellow', attrs=['bold']))
    #         pass
    #     else:
    #         # print('error')
    #         pass

    # def getCompletionNumber(self):
    #     return self.completion

# ---------------------------------------------------------------------------------

    # 写入文档
    def write(self, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.writelines(text)
            f.write('\n')
            f.close()

    # 清空文档
    def truncatefile(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            f.truncate()

    # 读取文档
    def read(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            txt = []
            for s in f.readlines():
                txt.append(s.strip())
        return txt

# ---------------------------------------------------------------------------------

    # 计算时间差,格式: 时分秒
    def gettimediff(self, start, end):
        seconds = (end - start).seconds
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        diff = ("%02d:%02d:%02d" % (h, m, s))
        return diff

    # 检查ip是否可用
    def checkip(self, ip, targeturl="https://www.maimemo.com/"):
        headers = self.getheaders()  # 定制请求头

        proxies = {"http": "http://" + ip, "https": "https://" + ip}  # 代理ip

        print("check ip: [%s]" % ip)

        try:
            response = requests.get(
                url=targeturl, proxies=proxies, headers=headers, timeout=5).status_code
            if response == 200:
                return True
            else:
                return False
        except:
            return False

    # 查找ip
    def findip(self, type, pagenum, targeturl="https://www.maimemo.com/", path="ip.txt"):  # ip类型,条数,目标url,存放ip的路径
        list = {
            '1': 'http://www.xicidaili.com/wn/',  # xicidaili国内https代理
            '2': 'http://www.xicidaili.com/nn/',  # xicidaili国内高匿代理
            '3': 'http://www.xicidaili.com/nt/',  # xicidaili国内普通代理
            '4': 'http://www.xicidaili.com/wt/'   # xicidaili国外http代理
        }
        url = list[str(type)] + str(pagenum)  # 配置url
        # print("url:", url)

        headers = self.getheaders()  # 定制请求头
        # print("get header %s" % datetime.datetime.now().__str__())

        rs = requests.get(url=url, headers=headers)
        html = rs.text

        # print("html:", html)
        soup = BeautifulSoup(html, 'lxml')
        all = soup.find_all('tr', class_='odd')
        for i in all:
            t = i.find_all('td')
            ip = t[1].text + ':' + t[2].text
            is_avail = self.checkip(ip=ip, targeturl=targeturl)
            if is_avail == True:
                self.write(path=path, text=ip)
                print(ip)

    # 从ip代理网站获取ip，并保存到文件中
    def getProxyIpFromWeb(self, targeturl="https://www.maimemo.com/", path="ip.txt"):
        self.truncatefile(path)  # 爬取前清空文档

        start = datetime.datetime.now()  # 开始时间

        threads = []
        for type in range(4):  # 四种类型ip,每种类型取前100,共400条线程
            for pagenum in range(200):
                t = threading.Thread(target=self.findip, args=(
                    type + 1, pagenum + 1, targeturl, path))
                threads.append(t)

        print('starting get ip proxy......')

        for s in threads:  # 开启多线程爬取
            s.start()

        for e in threads:  # 等待所有线程结束
            e.join()

        print('Get ip proxy success.')

        end = datetime.datetime.now()  # 结束时间

        diff = self.gettimediff(start, end)  # 计算耗时

        ips = self.read(path)  # 读取爬到的ip数量
        print('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))
        for ip in ips:
            print("[%s]" % ip.__str__())
            pass

# ---------------------------------------------------------------------------------

    # 从文件加载ip
    def getProxyIpFromFile(self, url="", path="ip.txt"):
        ips = read(path)
        threads = []
        for ip in ips:
            t = threading.Thread(target=self.check, args=(ip, url))
            threads.append(t)
            pass

        for thread in threads:
            thread.start()
            pass

        for thread in threads:
            thread.join()
            pass

        pass


if __name__ == "__main__":
    # how many proxies you want to
    # get in one request of free proxy site
    # proxynum = 100
    # how many visition your want to get, great or equal TargetNum what you set
    # TargetNum = 20

    try:
        # # get argv
        # from sys import argv
        # print(argv)
        # if 4 == argv.__len__():
        #     filename, url, proxynum, targetnum = argv
        #     momo = momo_share(url=url, TargetNum=int(
        #         targetnum), proxynum=int(proxynum))
        # elif 3 == argv.__len__():
        #     filename, url, targetnum = argv
        #     momo = momo_share(url=url, TargetNum=int(targetnum))
        # elif 2 == argv.__len__():
        #     filename, url = argv
        #     momo = momo_share(url)
        # else:
        #     print(
        #         "python -u momo-share.py url [targetnum] [proxynum]\ndefault: targetnum = 20, proxynum = 100")
        #     sys.exit(0)

        # # run
        # momo.run()
        # print("succed:[%d]" % momo.getCompletionNumber())
        # pass
        momo = momo_share()
        momo.getProxyIpFromWeb(targeturl="https://www.maimemo.com/")
        pass
    except KeyboardInterrupt:
        # print("exit")
        pass
    else:
        # print("success")
        pass
