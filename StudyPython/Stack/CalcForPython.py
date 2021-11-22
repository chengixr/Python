#使用Python写一个计算器
from StackCreat import StackCreat

class Calc:
    def __init__(self):
        pass

    def calc(self, string):
        stringStack = StackCreat()
        calcString = ""
        for sym in string:
            if sym.isdigit():
                if not stringStack.isEmpty() and stringStack.peck().replace(".", "").isdigit():
                    number = stringStack.peck() + sym
                    stringStack.pop()
                    stringStack.push(number)
                else:
                    stringStack.push(sym)
            elif sym == '.':
                if not stringStack.peck().isdigit():
                    print("小数点位置不正确，请重新输入")
                    return None
                elif '.' in stringStack.peck():
                    print("单个数据存在多个小数点，请重新输入")
                    return None
                number = stringStack.peck() + '.'
                stringStack.pop()
                stringStack.push(number) 
            elif sym == '*' or sym == '/' or sym == '+' or sym == '-' or sym == '(':
                stringStack.push(sym)
            elif sym == ')':
                calcString = ""
                while stringStack.peck() != '(':
                    if stringStack.isEmpty():
                        print("缺少左括号，请重新输入")
                        return None
                    calcString = stringStack.peck() + calcString
                    stringStack.pop()   
                    if stringStack.isEmpty():
                        print("缺少左括号，请重新输入")
                        return None
                calcStack = Calc()
                calcResult = calcStack.calc(calcString) #calc(calcString)
                stringStack.pop()
                stringStack.push(calcResult)
            else:
                print("未识别的字符，请输入正确的公式")
                return None
        
        numberStack = StackCreat()
        symStack = StackCreat()
        while not stringStack.isEmpty():
            if stringStack.peck().replace(".", "").isdigit():
                numberStack.push(stringStack.peck())
                stringStack.pop()
            elif stringStack.peck() == '*' or stringStack.peck() == '/':
                sym = stringStack.peck()
                stringStack.pop()
                if stringStack.isEmpty() or not stringStack.peck().replace(".", "").isdigit():
                    print("识别到符号未按照规则输入，请重新输入")
                    return None
                if sym == '*':
                    number = float(stringStack.peck()) * float(numberStack.peck())
                else:
                    number = int(stringStack.peck()) / int(numberStack.peck())
                numberStack.pop()
                stringStack.pop()
                numberStack.push(str(number))
            elif stringStack.peck() == '+' or stringStack.peck() == '-':
                symStack.push(stringStack.peck())
                stringStack.pop()
                if stringStack.isEmpty() or not stringStack.peck().replace(".", "").isdigit():
                    print("识别到符号未按照规则输入，请重新输入")
                    return None
            else:
                print("缺少右括号，请重新输入")
                return None
        
        while not symStack.isEmpty():
            number = float(numberStack.peck())
            numberStack.pop()
            if numberStack.isEmpty():
                print("公式输入错误，请重新输入")
                return None
            if symStack.peck() == "gtd+":
                number = number + float(numberStack.peck())
            else:
                number = number - float(numberStack.peck())
            numberStack.pop()
            numberStack.push(str(number))
            symStack.pop()
        return numberStack.peck()

if __name__ == '__main__':
    test = Calc()
    string = "3+0.2*(2/2)-2/1+5)"
    print(test.calc(string))
        