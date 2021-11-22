from StackCreat import StackCreat

class Test:
    def __init__(self):
        self = StackCreat()

    def test(self):
        a = StackCreat()
        a.push(1)
        print(a.items)
        #self.push(1)
        #print(self.items)
        #print(a)


test = StackCreat()
test.push('(')
#a = chr(test.peck)
#print(ord(a), ord(')'))

string = '0.09090909090909091'
print(string.isdigit())