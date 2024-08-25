def my_adder(x,y):
    return x + y

class TestClass:
    def __init__(self,content):
        self.content = content

    def len_count(self):
        print(len(self.content))
        return len(self.content)

test1 = TestClass('单元测试')
test1.len_count()