from abc import ABCMeta, abstractmethod


class _property():
    # __slot__魔法
    __slots__ = ('_name', '_age')  # 限定对象只能绑定这两个属性

    # 装饰器

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器：get方法
    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self._age = age

    @staticmethod  # 静态方法
    def IamStatic():
        print('I am  static method')

    @classmethod  # 类方法
    def class_method(cls):
        temp = cls('azoux-in-class', 20)
        print(temp.name)


class Person(object, metaclass=ABCMeta):
    # 人
    def __init__(self, age, name):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @abstractmethod
    def go_out(self):

        pass


class Student(Person):
    # 学生
    def __init__(self, age, name, grade):
        super().__init__(age, name)
        self._grade = grade

    def showInfo(self):
        print(self._grade)

    def go_out(self):
        print('stu')
        pass


def main():
    # p1 = _property('azoux', 19)
    # p1.age = 20
    # print(p1.age)
    # p1.IamStatic()
    # _property.IamStatic()
    # _property.class_method()

    # 继承多态
    stu1 = Student(19, 'azoux', 'python')
    stu1.showInfo()
    print(stu1._age)
    stu1.go_out()
    pass


if __name__ == "__main__":
    main()
    pass
