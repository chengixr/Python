# 创建阶乘函数计算C(m,n)

"""
def func(m):
    if m == 1:
        return 1
    return m * func(m - 1)

m = int(input('m='))
n = int(input('n='))
print(func(m) // func(n) // func(m - n))

from math import factorial as f

print(f(m) // f(n) // f(m - n))
"""

# 函数参数列表中设置强制位置参数:/，用*设置命名关键字参数。
# 所谓强制位置参数，就是调用函数时只能按照参数位置来接收参数值的参数；而命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数
"""
def make_judgement(a, b, c, /):
    # 判断三边是否能构成三角形
    return a+b>c and a+c>b and b+c>a

print(make_judgement(4, 3, 5))

def make_judgement_1(*, a, b, c):
    return a+b>c and a+c>b and b+c>a

print(make_judgement_1(a=3, b=4, c=5))
"""


# 可变参数，指的是在调用函数时，可以向函数传入0个或任意多个参数。
# 调用函数时传入的参数会保存到一个元组，通过对该元组的遍历，可以获取传入函数的参数。
"""
def add(*args):
    total = 0
    for arg in args:
        if type(arg) in (int, float):
            total += arg
    return total

print(add(1, 2, 3, 4))
print(add(1, 2, 3.1415926, 'hello', 3))
"""

# 字典通过“参数名=参数值”的形式接受参数，如果一个关键字参数都没有传入，那么kwargs会是一个空字典
"""
def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(1, 2, 3, 4)
foo(1, 2, 3, name='hello', age=27)
"""


def foo():
    print('hello')

def foo():
    print('goodbye')

foo()