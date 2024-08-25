moodIndex = int(input("请输入对象的心情指数"))
if moodIndex > 60:
    print('对象很开心')
else:
    print("对象很生气")


user_weight = float(input("请输入您的体重"))
user_height = float(input("请输入您的身高"))
user_BMI = user_weight / (user_height ** 2)
print("您的BMI值为:" + str(user_BMI))

user_exe = input("您的性别是:")
if user_BMI <= 18.5:
    if user_exe == 'boy':
        print("正常")
    else:
        print("偏瘦")
elif  18.5<user_BMI <= 25:
    print("正常")
elif 25 < user_BMI <= 30:
    print("偏胖")
else:
    print("偏胖")