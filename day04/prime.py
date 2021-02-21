num = int(input('pleasr input a positive integer:'))
while(num <= 0):
    num = int(input('please input the right integer:'))

flag = 1

for x in range(2,num):
    if num % x == 0:
        flag = 0
        break

if flag == 1:
    print('%d is a prime' % num)
else:
    print('%d is not a prime' % num)