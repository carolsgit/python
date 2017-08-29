import urllib.request
page=urllib.request.urlopen("http://www.lookinfo.com.cn/do/alonepage.php?id=2")
text=page.read().decode("gb2312")
a=text[900:1000]

print(a)
