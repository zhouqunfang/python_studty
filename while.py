#for 循环适合有明确循环对象或次数
#while 循环适合循环次数未知

print("哈喽呀 我是一个求平均值的程序")
user_input = input("请输入数字（完成所有输入后，输入q终止程序）")
averageValue = 0
averageArray = []
while user_input != "q":
    input_num = float(user_input)
    averageArray.append(input_num)
    user_input = input("请输入数字（完成所有输入后，输入q终止程序）")
if sum(averageArray) == 0:
    averageValue = 0
else:
    averageValue = sum(averageArray)/ len(averageArray)

print(str(averageValue),"平均值")



