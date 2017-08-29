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
    

