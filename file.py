# 文件操作
# open()打开文件 close()关闭文件释放资源

## 读取文件,返回一个文件对象 r:读取模式 w:写入模式 a:附加模式 r+：同时支持读写操作
f = open("file_test.txt","r",encoding="utf-8")

#1. read
# 会读全部的文件内容，读完后，如果再读取，打印为空
print(f.read())
# 会读第1-10个字节的文件内容，并打印
print(f.read(10))

#2. readline 读一行文件内容
print(f.readline())
print(f.readline())

#3. readlines 把每行内容存储到列表里
lines = f.readlines()
for line in lines:
    print(line)
# 关闭文件
f.close()

## 读取完文件后会自动关闭释放内存
with open("file_test.txt",'r',encoding="utf-8") as f2:
    print(f2.read())


## 写文件
with open("./data.txt",'w',encoding="utf-8") as f3:
    f3.write("hello\n")
    f3.write("haha")

with open("./data.txt",'a',encoding="utf-8") as f4:
    f4.write('附加')

with open("./data.txt",'r+',encoding="utf-8") as f5:
    f5.write('附加1111\n')
    f5.write('最后一行')
    print(f5.read())

