# 面向对象编程  类 对象
from traceback import print_tb


# 创建一个类
# 变量名 使用 下划线命名
# 类名 使用 Pascal命名
class CatClass:
    # 构造函数
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
#     定义方法
    def speak(self):
        print("喵"* self.age)
    def think(self,content):
        print(f"小猫在思考{content}...")
# 实例化对象
cat1 = CatClass('肥牛',"公",3)
print(cat1)
print(cat1.name)
cat1.speak()
cat1.think('什么时候有猫条吃')


class StudentClass :
    def __init__(self,name,num):
        self.grades = {"yuwen":0,"shuxue":0,"yingyu":0}
        self.name = name
        self.num = num
    # 设置成绩
    def set_grade(self):
        start_set = input("是否继续设置成绩")
        while start_set != 'p':
            course_name = input("设置的科目")
            grade = input("设置对应科目的成绩")
            if course_name in self.grades:
                self.grades[course_name] = grade
            start_set = input("是否继续设置成绩")

    # 打印成绩
    def print_grade(self):
        print(f"学生名字{self.name}，学号为{self.num},成绩为：")
        for item in self.grades.items():
            print(f"{item[0]}成绩{item[1]}")

student1 = StudentClass("小芳",1)
student1.set_grade()
student1.print_grade()


