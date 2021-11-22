#创建栈
#具体包括方法：isEmpty 判断空； push 入栈； pop 出栈； peck 返回栈顶值； 

#定义类
class StackCreat:
    #创建基础列表
    def __init__(self):
        self.items = []
    
    #定义判断空方法
    def isEmpty(self):
        #如果列表等于[]说明为空
        return self.items == []
    
    #入栈方法
    def push(self, item):
        self.items.append(item)

    #出栈方法
    def pop(self):
        self.items.pop()
    
    #返回栈顶方法
    def peck(self):
        return self.items[len(self.items) - 1]