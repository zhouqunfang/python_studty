# format()
content = """
你好啊{0}，
{1}年大吉
""".format("小明",'兔')


content = """
你好啊{name}，
{year}年大吉
""".format(name="小子",year="虎")


# f-字符串
name="小方"
year="虎"
content = f"""
你好{name}
{year}年大吉
"""
print(content,'content')

list={'小米':"虎","小方":"兔"}
for name,year in list.items():
    print(f"{name}你好，{year}年快乐")

# .2f保留两位小小数
list={'小米':3.2221,"小方":5.8273}
for name,year in list.items():
    print("{0:.2f}".format(year))