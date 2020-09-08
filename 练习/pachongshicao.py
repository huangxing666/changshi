from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3


def main():
    baseurl='https://movie.douban.com/top250?start='
    datalist=getData(baseurl)
    savepath='.\\豆瓣电影.xls'
    # askURL(baseurl)
    saveData(datalist,savepath)
    




#找到电影链接
findLink=re.compile(r'<a href="(.*?)">')   #创建正则表达式对象，设定规则
#找到电影图片
findImgSrc=re.compile(r'<img.*src="(.*?)" width="100"/>',re.S)  #re.S让换行符也能匹配
#找到电影标题
findTitle=re.compile(r'<span class="title">(.*?)</span>')
#找到电影评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到电影评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到电影简介
findInq=re.compile(r'<span class="inq">(.*)</span>')
#找到电影作者主演
findBd=re.compile(r'<p class="">(.*)</p>.*<div class="star">',re.S)





#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):           #调用获取页面信息的函数
        url=baseurl+str(i*25)
        html=askURL(url)
        
        #2.逐一解析数据
        soup=BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_="item"):    #查找符合要求的字符串    

            
            data=[]     #保存一部电影的所有信息
            item=str(item)
            link=re.findall(findLink,item)[0]       #通过正则表达式查找指定字符串
            data.append(link)
            
            ImgSrc=re.findall(findImgSrc,item)[0]
            data.append(ImgSrc)

            Title=re.findall(findTitle,item)
            if(len(Title)==2):
                ctitle=Title[0]
                data.append(ctitle)
                otitle=Title[1].replace('/','')
                data.append(otitle)
            else:
                data.append(Title[0])
                data.append(' ')

            rating=re.findall(findRating,item)[0]
            data.append(rating)

            judge=re.findall(findJudge,item)[0]
            data.append(judge)

            inq=re.findall(findInq,item)
            if len(inq)!=0:
                inq=inq[0].replace('。','')
                data.append(inq)
            else:
                data.append(' ')

            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?','',bd)    #去掉<br/>
            bd=re.sub('/','',bd)    #替换/
            data.append(bd.strip()) #去掉前后空格
            datalist.append(data)   #把处理好的一部电影信息放入datalist

    # print(datalist)
    return datalist                 #保存获取到的网页源码


def askURL(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf8')

    req=urllib.request.Request(url,data=data,headers=headers)
    response=urllib.request.urlopen(req)
    html=(response.read().decode('utf8'))
    # print(html)
    return html









#保存数据
def saveData(datalist,savepath):
    workbook=xlwt.Workbook(encoding='utf-8',style_compression=0)
    worksheet=workbook.add_sheet('电影Top250',cell_overwrite_ok=True)
    # col=('电影详情链接','电影图片','电影名称','电影外文名','评分','评价人数','概况','相关信息')
    # for i in range(0,8):
    #     worksheet.write(0,i,col[i])     #设置列名
    
    a=0
    b=0
    j=0
    for i in datalist:
        for c in i:
            worksheet.write(a,b,c)
            j+=1
            if j<8:
                b=b+1
            else:
                a+=1
                b=0
                j=0

    workbook.save(savepath)



if __name__=='__main__':   #程序开始位置
    main()                 #调用函数

