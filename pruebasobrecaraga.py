class Vector2D:
    __x = 0.0
    __y = 0.0

    def __init__(self, x=-1, y=-1):
        self.__x = x
        self.__y = y
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
    def __str__(self):
        return '<{},{}>'.format(self.__x,self.__y)


    def __add__(self,otrovector):
        return Vector2D(self.__x + otrovector.getx(),self.__y + otrovector.gety())

if __name__=='__main__':
    a = Vector2D(4,2)
    b = Vector2D(2,2)
    a = a + b
    print (a)