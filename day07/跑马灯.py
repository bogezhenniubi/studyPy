#coding=utf-8
import os

led = '      我是跑马灯'
for x in range(6):
    print(led[x:11],end='')
    # 清屏,cmd实现了，编译软件不行？
    os.system('cls')    
    


