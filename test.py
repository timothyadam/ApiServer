class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。%d kg" % (self.name, self.age,self.__weight))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


s = student('ken', 10, 60, 3)
p = people('david', 10, 60)
s.speak()
p.speak()
