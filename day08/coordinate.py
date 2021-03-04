from math import sqrt

class Point(object):
    def __init__(self,x=0,y=0):
    # 初始化坐标
        self.x = x
        self.y = y
    
    def specify(self,x,y):
    # 指定坐标
        self.x = x
        self.y = y
    
    def move(self,a,b):
    # 移动增量
        self.x += a
        self.y += b
    
    def distance(self,another):
    # 计算与另一个点的距离
        dx = self.x - another.x
        dy = self.y - another.y
        return sqrt(dx**2 + dy**2)
    def _str_(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

A = Point()
B = Point()
B.move(3,4)
print(B)
print(A.distance(B))