year = int(input('请输入年份:'))
if(year % 100 == 0):
    if(year % 400 == 0):
        print(year,'年是闰年')
    else:
        print(year,'年不是闰年')
else:
    if(year % 4 == 0):
        print(year,'年是闰年')
    else:
        print(year,'年不是闰年')