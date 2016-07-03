# coding=utf-8
# filter(def1,list)->list就是2，到100了，这个def怎么办呢 就是一个返回值为布尔型的函数
def isprime(m):
    # 质数是指只能被1和它本身整除的数
    for i in range(2, m / 2 + 1):
        if m % i == 0:
            return False
    return True


if __name__ == '__main__':
    print filter(isprime, range(2, 101))
# isprime也是一个迭代 输入是一个数字，输出是一个布尔型,可以让他返回一个列表，然后去not就行了
