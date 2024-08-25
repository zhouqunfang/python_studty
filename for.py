from copyreg import constructor

numArray = [1,2,3,4,5]
for item in numArray:
    if item>3:
        print("大于3的数字")
    else:
        print('小于3')


num_dict = {"a":1,"b":2,"c":3}
print(num_dict.keys(),'所有key')
print(num_dict.values(),"所有value")
print(num_dict.items(),"所有键值对")

for item in num_dict:
    print(item,'item==')

for id,item in num_dict.items():
    print(id,'id')
    print(item,'item')

for item in num_dict.items():
    print(item[0],'==0')
    print(item[1],'==1')


# range 表示整数序列
#range(5,10,2) 第一个表示起始值 第二个表示结束值 第三个值步长
for num in range(1,10,2):
    print(num,'range')

total = 0
for num in range(1,101):
    total = total + num
print(total,"1到100的和")