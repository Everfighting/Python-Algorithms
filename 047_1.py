# coding=utf-8
def exchange(a,b):
    a,b = b,a
    return (a,b)

print map(exchange,range(4),range(2,6))

print map(exchange,[3,],[4,])
# map后需跟随可迭代对象！

