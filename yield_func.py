#! python3
# _*_ coding:utf-8 _*_
# Time   : 18-2-3 下午8:28
# Author : Jin Tone

def fun():
    for i in range(20):
        x=yield i
        print('good',x)

if __name__ == '__main__':
    a=fun()
    a.__next__()
    x=a.send(4)
    print(x)

