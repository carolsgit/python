#猜数字游戏
print("welcome!")
g = input("guess the number:")
guess=int(g)
if guess == 5:
  print("you win!")
else: 
  print("you lose...")
print("game over!") 


#输出输入数字
print("请输入一个数字：")
x=input()
number=int(x)
print("你输入的是：" ,number)



#输入输出文本
print("请输入一个汉字：")
x=input()
number=str(x)
print("你输入的是：" ,number)


#带提示的猜数字
print("welcome!")
x=input("请输入一个数字[1-100]：")
num=int(x)
if num==66:
  print("你猜对了！")
else:
   if num>66:
     print("太大了！")
   else:
     print("太小了！")
print("GAME OVER")  

#while循环实例
print("welcome") 

x=input("do you love me?")              #用户输入x
guess=str(x)                            #把输入字符赋值给guess

while guess=="no" or guess=="NO":       #循环条件
    print("you get a change agine:")    #循环体
    guess=input()                       #防止死循环

print("I LOVE YOU TOO!")                #guess值不为no时，结束循环




#带while循环 和分支的猜数字
print("welcome")
guess=0
while guess!=5:

	g=input("输入一个数字：")

	guess=int(g)


	if guess==5:
		print("你赢了")
	
	else:
		if guess>5:
			print("太大了")

		else:
			print("太小了")

print("game over!")
    
#猜数字，随机数字
print("welcome")
guess=0
from random import randint     #定义随机数字
secret=randint(1,10)           #把随机数字1-10中的一个 ，赋值给secret

while guess!=secret:
     g=input("输入一个数字：")
     guess=int(g)

     if guess==secret:
         print("你赢了")
    
     else:
         if guess>secret:
             print("太大了")
         else:
             print("太小了")

print("game over!")



#导入网页并获得一段字符串
import urllib.request
page=urllib.request.urlopen("http://www.lookinfo.com.cn/do/alonepage.php?id=2")
text=page.read().decode("gb2312")
a=text[900:1000]

print(a)


#搜索网页字符串并打印显示
import urllib.request
page=urllib.request.urlopen("http://www.lookinfo.com.cn/do/alonepage.php?id=2")
text=page.read().decode("gb2312")
#a=text[900:1000]
start=text.find("海南")
end=start+12
print(text[start:end])


#循环打印
i=0                      #确保运行第一次
while i<=10:             #循环条件
    i=i+1                #每次循环加1，第一次为0+1
    a="hello world!"  
    print(a.upper(),i)   #upper()函索将字符转换为大写，lower()相反
print("game over!!!")

