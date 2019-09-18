import urllib.request
import requests
from bs4 import BeautifulSoup


class novel_downloader():

    def __init__(self):
        #target = "http://www.biquge.com.tw/18_18820/"
        #print("本软件暂时仅支持笔趣阁www.biquge.com.tw")
        self.target=input("请输入小说Url\n")
        self.target="http://www.biquge.com.tw/0_748"

    def get_novel(self):
        # 获取服务地址：笔趣阁
        temp_server=self.target.replace("//","@")
        server=temp_server[0:temp_server.index("/")]
        server=server.replace("@","//")
        # 获取HTML页面，并寻找内容
        res = requests.get(self.target)
        html = res.content

        #寻找可到达的跳转标签（章节）放置在aSet集合中
        bt_all = BeautifulSoup(html, "html.parser")
        titleSet = bt_all.find_all("div", id="list")
        bt_titles = BeautifulSoup(str(titleSet[0]), "html.parser")
        aSet = bt_titles.find_all("a")

        #获取小说名和输出目录
        novel_name_set = bt_all.find_all("div", id="info")
        novel_name_bt = BeautifulSoup(str(novel_name_set[0]), "html.parser")
        novel_name = novel_name_bt.find_all("h1")
        file_name = str(novel_name[0])
        file_name= file_name.replace("<h1>",'')
        file_name= file_name.replace("</h1>",'')
        file_path="../Out/Novel/"+file_name+".txt"
        print("准备下载小说《%s》"%file_name)

        #写入文字
        with open(file_path, "w+")as f:
            f.write(file_name+"\n")
            j = 0
            for i in aSet:
                j = j + 1
                #if j>5: break
                titleName = str(i.string)
                f.write(titleName + "\n\n")
                targetI = server + i.get("href")
                res_i = requests.get(targetI)
                
                html_i = res_i.content
                bt_all_i = BeautifulSoup(html_i, "html.parser")
                con_allSet = bt_all_i.find_all("div", id="content")
                con_i = con_allSet[0].text.replace(u'\xa0', u' ')

                f.write(con_i)
                f.write("\n\n\n")
                print("第{0}章下载成功".format(j))
            else:
                print("全书下载完毕,共{0}章".format(j))
#
# if __name__=="__main__":
#      target = "http://www.biquge.com.tw/18_18820/"
#      n=novel_downloader()
#      n.get_novel()
