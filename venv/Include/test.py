from Include.Novel import novel as No
from Include.Video import video as Vi
from Include.Graph import graph as Gr

if __name__=="__main__":
    inputType=input("请输入想要下载的类型（小说/视频/图片)\n")
    inputType=inputType.rstrip()
    if inputType=="小说" :
        #print("暂时仅支持笔趣阁http://www.biquge.com.tw")
        pass
    # target = "http://www.biquge.com.tw/18_18820/"
        nd=No.novel_downloader()
        nd.get_novel()

    elif inputType=="视频":
        #url = 'http://www.iqiyi.com/v_19rr7qhfg0.html#vfrm=19-9-0-1'
        vd = Vi.video_downloader()
        vd.get_video()

    elif inputType=="图片":
        gd=Gr.Graph_downloader()
        gd.get_img()
