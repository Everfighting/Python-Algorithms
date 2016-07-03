# coding=utf-8
# isprime=lambda(x:[x%i==0 for i in range(2,x)]） 不行
# 还是用列表解析出2到x-1中的数字去判断
# [x%i for i in range(2,x) if x%i==0] 每个i是否能把x整除，if是过滤条件，如果有返回列表就是有数字把x整除了，素数应该返回一个[]
isprime = lambda x: not [x % i for i in range(2, x) if x % i == 0]
# 最后的公式就是
prime = filter(lambda x: not [x % i for i in range(2, x) if x % i == 0], range(2, 101))
print prime
print 'the number of primes is ', len(prime)
# filter用法：filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple。
