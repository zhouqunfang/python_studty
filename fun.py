# 定义函数
from six import print_


def sum_fun(a,b):
      sum = a+b
      return sum
print(sum_fun(1,2))

# python内置函数 https://docs.python.org/zh-cn/3/library/functions.html -常用函数

#引入python其他模块函数
# 比如 statistics --- 数字统计函数 模块 https://docs.python.org/zh-cn/3/library/statistics.html
import  statistics
print(statistics.median([11,22,33]))

#匿名函数
lambda num1,num2: num1 + num2
(lambda num1,num2: num1 + num2)(2,3)
print((lambda num1,num2: num1 + num2)(2,3))
