def xunhuan():           #定义函数xunhuan，注意()的：不能省略
    i=0                          #确保运行第一次
    while i<=10:           #循环条件
       i=i+1                    #每次循环加1，第一次为0+1
       a="hello world!"
       print(a.upper(),i)   #upper()函索将字符转换为大写，lower()相反
    print("game over!!!")
xunhuan()
