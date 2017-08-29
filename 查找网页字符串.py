import urllib.request
page=urllib.request.urlopen("http://www.lookinfo.com.cn/do/alonepage.php?id=2")
text=page.read().decode("gb2312")
a=text[900:1000]

info=a.find("鲁科")
#start=info
#end=start+1000

#name=text[start:end]
#print(name)


print(a)
print(text[info:info+500])
