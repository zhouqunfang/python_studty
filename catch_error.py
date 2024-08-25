# 捕捉异常
try:
    user_weight = float(input("请入输入你的体重"))
    user_height = float(input("请入输入你的身高"))
    user_BMI = user_weight / user_height ** 2
except ValueError:
    print("输入不为合理数字")
except ZeroDivisionError:
    print("身高不能为0")
except:
    print('发生了错误')
else:
    # 没有错误时会运行
    print("您的BMI值为：" + str(user_BMI))
finally:
    print("程序结束时运行")