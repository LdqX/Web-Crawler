#-*- coding:UTF-8 -*-
import requests,re, json, sys, webbrowser as WEB, time
from bs4 import BeautifulSoup
from urllib import request

class video_downloader():
# 初始化视频下载器
    def __init__(self):
        url = input("请输入要解析的视频地址\n")
        #http://www.sonimei.cn/?url=https://
        self.server = 'http://www.sonimei.cn/'
        #self.server = 'http://api.xfsub.com'
        #self.api = 'http://api.xfsub.com/xfsub_api/?url='
        self.api='http://www.sonimei.cn/?url='
        #self.get_url_api = 'http://api.xfsub.com/xfsub_api/url.php'
        self.url = url.split('#')[0]
        self.target = self.api + self.url
        self.s = requests.session()


    def get_key(self):
        req = self.s.get(url=self.target)
        req.encoding = 'utf-8'
        temp=re.findall('"url.php",\ (.+),',req.text)
        self.Watch_online()
        #使用正则表达式匹配结果，将匹配的结果存入info变量中

    #获取视频地址
    def get_url(self):
        data = {'time':self.info['time'],
            'key':self.info['key'],
            'url':self.info['url'],
            'type':''}
        req = self.s.post(url=self.get_url_api,data=data)
        url = self.server + json.loads(req.text)['url']
        req = self.s.get(url)
        bf = BeautifulSoup(req.text,'xml')                                        #因为文件是xml格式的，所以要进行xml解析。
        video_url = bf.find('file').string                                        #匹配到视频地址
        return video_url


    #回调函数，打印下载进度
    def Schedule(self, a, b, c):
        per = 100.0*a*b/c
        if per > 100 :
            per = 1
        sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per,a*b,c) + '\r')
        sys.stdout.flush()
    def video_download(self, url, filename):
        request.urlretrieve(url=url,filename=filename,reporthook=self.Schedule)


    def Watch_online(self):
        for i in range(3):
            count=3-i
            print("暂时不支持视频下载，将在{0}秒后尝试在线播放".format(count))
            time.sleep(1)
        WEB.open(self.target)

    def get_video(self):
        self.get_key()
        # filename = '加勒比海盗5'
        # print("%s开始下载", filename)
        # video_url = self.get_url()
        # print('获取地址成功:%s' % video_url)
        # video_download(video_url, filename + '.mp4')
        # print('\n下载完成！')

"""
if __name__ == '__main__':
    #url = 'http://www.iqiyi.com/v_19rr7qhfg0.html#vfrm=19-9-0-1'
    #url = 'https://www.iqiyi.com/v_19rr503d0g.html'
    print("由于接口功能问题，地址可能解析失败")
    url=input("请输入视频地址\n")
    vd = video_downloader(url)
    vd.Watch_online()


    filename = '加勒比海盗5'
    print("%s开始下载",filename)
    vd.get_key()
    video_url = vd.get_url()
    print('  获取地址成功:%s' % video_url)
    vd.video_download(video_url, filename+'.mp4')
    print('\n下载完成！')
    
"""