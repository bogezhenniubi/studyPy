#coding=utf-8
import os
import random

print("Welcome to the kingdom of '井'")
border = [
    ' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',
    ' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',
    ' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '
]
flag = True
def drawBorder():
# 打印棋盘
    print(border[:11])
    print('*** *** ***')
    print(border[:22])
    print('*** *** ***')
    print(border[:33])

# 选择棋子
role = ''
while not (role == 'x' or role == 'o'):
    role = input('Do you want to be x or o?')
    if role == 'x':
        crole = '0'
    else:
        crole = 'x'

def priority():
# 随机决定优先落子方
    return (random.randint(0, 1)) 

def playerStep(p):
# 玩家下棋  
        border[p] = role
        os.system('cls')
        print(drawBorder())
        for x in range(len(figures)):
        # 删除已被选择的位置
            if figures[x] == player:
                del figures[x]
        print('Waitting for computer choosing:')

def computerStep(c):        
        border[c] = crole
        os.system('cls')
        print(drawBorder())
        for j in range(len(figures)):
        # 删除已被选择的位置
            if figures[j] == computer:
                del figures[j]

def equ(obj,a,b,c):
    if (obj[a]==obj[b] and obj[b]==obj[c] and obj[a]==obj[c]):
        return True
    else:
        return False

def referee(b):
# 判断胜利者 equ(b[1::4])
    if (equ(b,1,5,9) or equ(b,12,16,20) or equ(b,23,27,31) or
    equ(b,1,16,31) or equ(b,9,16,23)):
        return 1

figures = [1,5,9,12,16,20,23,27,31]
print('There are nine figures(1,5,9,12,16,20,23,27,31) you can choose,every figure is allowes to be chosen only once.')

while flag:
    if priority():
        player = int(input('Please choose your fortuate number:'))
        playerStep(player)
        if (referee(border)):
            print('Oh yeah!You have won the game~')
            break
        computer = random.sample(figures,1)[0]
        computerStep(computer)
        if (referee(border)):
            print("It's a pity!You lost.")
            break
    else:
        computer = random.sample(figures,1)[0]
        computerStep(computer)
        if (referee(border)):
            print("It's a pity!You lost.")
            break
        player = int(input('Please choose your fortuate number:'))
        playerStep(player)
        if (referee(border)):
            print('Oh yeah!You have won the game~')
            break
        