#629. K个逆序对数组

'''
给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。

由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。
'''

def test(n, k):
    if k == 0 or n == 1 or n == k:
        return 1
    if k > n or k < 0 or n <= 0:
        return 0
    return test(n, k-1) + test(n-1, k) - test(n-1, k-n)

n = 3
k = 1
print(test(n, k))


