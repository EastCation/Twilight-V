for i in range(1,10):
    for j in range(1,i+1):
        print("{0:1}*{1:1}={2:2} ".format(j,i,j*i),end="")
    print()
input("按回车键结束程序")
