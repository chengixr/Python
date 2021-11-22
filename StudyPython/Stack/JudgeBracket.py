#使用栈方法判断输入的字符串是否符合括号条件
from StackCreat import StackCreat

class JudgeBracket:
    def __init__(self):
        pass
    
    def judgeBracket(self, bracketString):
        #self.items = list(bracketString)
        bracketStack = StackCreat()
        for symbol in bracketString:
            if symbol == '(':
                bracketStack.push(symbol)
            # elif ord(bracketStack.peck) == ord(symbol) - 1 or ord(bracketStack.peck) == ord(symbol) - 2:
            #     bracketStack.pop()
            elif bracketStack.isEmpty():
                return False
            elif bracketStack.peck() == '(':
                bracketStack.pop()
            else:
                return False
        if bracketStack.isEmpty():
            return True
        else:
            return False

test = JudgeBracket()

print(test.judgeBracket("(()"))
