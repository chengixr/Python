#677. 键值映射
'''
实现一个 MapSum 类，支持两个方法，insert 和 sum：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。
如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
'''


class MapSum:
    def __init__(self):
        self.dict = {}
    def insert(self, key:str, val:int):
        self.dict[key] = val
    def sum(self, prefix: str) -> int:
        res = 0
        for key,val in self.dict.items():
            if key.startswith(prefix):
                res += val
        return res
    # def sum(self, prefix:str):
    #     sum = 0
    #     for value in self.dict.keys():
    #         perfect = True
    #         for i in range(len(prefix)):
    #             if i == len(value):
    #                 perfect = False
    #                 break
    #             if prefix[i] != value[i]:
    #                 perfect = False
    #         if perfect == True:
    #             sum += self.dict[value]
    #     return sum
    
if __name__ == '__main__':
    mapSum = MapSum()
    mapSum.insert('aa', 3)
    print(mapSum.sum('a'))
    mapSum.insert('aa', 2)
    print(mapSum.sum('a'))
    print(mapSum.sum('aa'))
    mapSum.insert('aaa', 3)
    print(mapSum.sum('aaa'))