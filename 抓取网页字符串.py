import urllib.request
def lookinfo():
    page=urllib.request.urlopen("http://www.lookinfo.com.cn/do/alonepage.php?id=2") #urllib.request.urlopen抓取网页
    text=page.read().decode("gb2312")        #抓取内容赋值给text，并转码成gb2312格式便于阅读

# a=text[3000:3500] #抓取text中3000到3500之前的内容赋值给a
    start=text.find("海南")
    end=start+12
    name=text[start:end]
    print(name)
print(lookinfo())
