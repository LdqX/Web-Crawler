from bs4 import BeautifulSoup
from urllib import request
import requests

#定点网站图片爬取,输入图片尺寸，返回猫图片
#获取网站信息
class Graph_downloader():
    def __init__(self):
        self.hei=input("请输入想要的图片长度\n")
        self.wid=input("请输入想要的图片高度\n")
        self.url="http://placekitten.com/"+self.hei+"/"+self.wid

    def get_img(self):
        req=request.Request(self.url)
        response=request.urlopen(req)
        cat_img = response.read()
        graph_path="../Out/Graph/"+self.wid+"_"+self.hei+".jpg"
        #print(graph_path)
        with open(graph_path, "wb")as f:
            #以二进制方式写入600.jpg文件(在当前文件夹生成)
            f.write(cat_img);
            print("下载完成\n")
