#! python3
# _*_ coding:utf-8 _*_
# 记录python中的几种经典算法

'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”。
指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........这个数列从第3项开始，每一项都等于前两项之和。
如果设F(n）为该数列的第n项（n∈N*），那么这句话可以写成如下形式：:F(n)=F(n-1)+F(n-2)。显然这是一个线性递推数列。
'''

# 第一种
fib1 = lambda n: 1 if n < 2 else fib1(n - 1) + fib1(n - 2)


# 第二种记忆方法, 装饰器
def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fib2(i):
    if i < 2:
        return 1
    return fib2(i - 1) + fib2(i - 2)


# 第三种方法
def fib3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


print(fib2(5))
