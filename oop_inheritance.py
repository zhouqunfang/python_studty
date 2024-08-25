# 面向对象编程
#继承

# 父类
class Mammal:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

#子类
# 继承父类
class Cat(Mammal):
    def __init__(self,name,sex):
        # super() 调用父类的构造函数
        super().__init__(name,sex)
        self.hasTail = True
    def scratch_sofa(self):
        print('抓沙发')

class Human(Mammal):
    def __init__(self,name,sex):
        # super() 调用父类的构造函数
        super().__init__(name,sex)
        self.hasTail = True
    def read(self):
        print('阅读')

cat1 = Cat('肥牛','公')
print(cat1.hasTail)
cat1.scratch_sofa()