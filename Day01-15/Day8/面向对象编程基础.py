import math


class Student(object):
    # python 创建对象
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        # 在python中以__两个下划线开头的变量为私有变量，但是其实也是可以访问到的，只需要访问_Student__age
        # We are all consenting adults here
        # 所以我们一般约定以一个下划线开头的变量为私有成员，更多时候它是一种暗示或者隐喻

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))


# 练习： 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        # 更换位置
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance_to(self, x, y):
        return math.sqrt((self._x - x)**2 + (self._y - y)**2)


def main():
    # stu1 = Student('azoux', 19)
    # stu1.study('python')
    # print(stu1.age)  私有

    p1 = Point(2, 5)
    p1.move_by(2, 5)
    print(p1.distance_to(-120, -10))

    pass


if __name__ == "__main__":
    main()
