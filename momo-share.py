#encoding: utf8
import aiohttp
import asyncio
from termcolor import colored
import requests
import re
import time
import random


class momo_share:
    def __init__(self, url, TargetNum=30, proxynum=120):
        super().__init__()
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
        self.proxies = []
        self.ProxyList = []
        self.proxynum = proxynum
        self.TargetNum = TargetNum
        self.url = url
        self.completion = 0
        pass

    def getProxy(self):
        if self.completion >= self.TargetNum:
            return 0
        print('[+] %s' % colored('get proxy...', 'blue', attrs=['bold']), end='')

        while 1:
            try:
                purl = 'http://www.89ip.cn/tqdl.html?num=%s' % self.proxynum
                resp = requests.get(purl, headers=self.header)
                html = resp.text

                self.proxies = set(re.findall(
                    r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]+", html)) - set(self.ProxyList)

                if not len(self.proxies):
                    print('\n  [-]Waiting')
                    time.sleep(random(0, 3))
                    continue

                print(colored('[%d]' % len(self.proxies), 'yellow', attrs=['bold']), '%s' % (
                    colored('Done!', 'green', attrs=['bold'])))
                return 1
            except Exception as e:
                print('\n  [-]Error: ' + str(e))
                time.sleep(random(1, 6))
                pass

    async def autoVisit(self, proxy, sem):
        async with sem:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(url=url, proxy='http://' + proxy, timeout=5) as resp:
                        print('[%s]' % colored(proxy, 'cyan', attrs=['bold']),
                              colored('Successfully!', 'green', attrs=['bold']))
                    self.ProxyList.append(proxy)
                    self.completion += 1
                except Exception as e:
                    print('[%s]' % proxy, colored(
                        'Failed!', 'red', attrs=['bold']))

    def run(self):
        if '' != url:
            loop = asyncio.get_event_loop()
            sem = asyncio.Semaphore(self.proxynum)
            while self.getProxy():
                tasks = [asyncio.ensure_future(
                    self.autoVisit(i, sem)) for i in self.proxies]
                loop.run_until_complete(asyncio.wait(tasks))
            loop.close()
            print(colored(self.completion, 'yellow',
                          attrs=['bold']))
        else:
            print('error')
            pass


if __name__ == "__main__":
    # how many proxies you want to
    # get in one request of free proxy site
    # proxynum = 100
    # how many visition your want to get, great or equal TargetNum what you set
    # TargetNum = 25

    # get argv
    from sys import argv
    print(argv)
    if 4 == argv.__len__():
        filename, url, proxynum, targetnum = argv
        momo = momo_share(url=url, TargetNum=int(
            targetnum), proxynum=int(proxynum))
    elif 3 == argv.__len__():
        filename, url, targetnum = argv
        momo = momo_share(url=url, TargetNum=int(targetnum))
    elif 2 == argv.__len__():
        filename, url = argv
        momo = momo_share(url)
    else:
        print("python -u MoMo-aiohttp.py 'url' 'targetnum' 'proxynum'")
        exit(-1)

    # run
    momo.run()
