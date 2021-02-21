line = int(input('please input the line that you want to print:'))

for x in range(1,line + 1):
    for j in range(line - x):
        print(' ',end='')
    for z in range(1,2 * x - 1):
        print('*',end='')
    print()



