import random
import time
import os
print("你好，现在你有10秒的时间记忆下列物品及其编号")
things=["草方块","土豆","原石","水晶","体力药水","扩充补给卡","家园补给卡","精准补给卡","黑曜石","基岩"]
for i in range(10):
    print(i,":",things[i])   #在屏幕上显示物品及其编号
time.sleep(10)               #延时10秒
os.system("cls")             #清屏
n=0                          #记录答对的题数，初值为0
t2=random.sample(things,5)   #随机抽出五个物品
for i in t2:                 #出5题
    ans=int(input(i + "的编号是："))#输入编号答题
    if i==things[ans]:
        n=n+1                #如果回答正确，答对的题数加1
print("\n你一共答对了",n,"次")#屏幕显示答对的题数
input("\n按回车键结束程序")
