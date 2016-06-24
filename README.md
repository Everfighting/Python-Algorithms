﻿# Python-Algorithms
http://www.runoob.com/python/python-100-examples.html

- 题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
> 001.py 程序分析：可填在百位、十位、个位的数字都是1、2、3、4，组成所有的排列后再去 掉不满足条件的排列。
001_1.py 程序分析：按照计算的方式组成三位数。
001_2.py 程序分析：沿用原有方法，利用格式化输出排列成三位数。

- 题目2：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
> 002.py 程序分析：利用数轴来分界，定位。通过数组进行分段计算累加。
002_1.py 程序分析：利用if elif 结构分段讨论。

- 题目3：题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
> 003.py 程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。(该数必小于10000)

- 题目4：输入某年某月某日，判断这一天是这一年的第几天？
> 004.py 程序分析：先判断年份是否为闰年，然后在计算之前的月份的日期数。以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天

- 题目5：输入三个整数x,y,z，请把这三个数由小到大输出。
> 005.py 程序分析：将输入的三个数逐个加入列表中，然后用sort方法进行排序，呈现从小到大的结果。

- 题目6：斐波那契数列。
> 006.py 程序分析：斐波那契数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。 F0 = 0 (n=0) F1 = 1 (n=1) Fn = F[n-1]+ F[n-2] (n=>2)
006_.py 程序分析：用递推的思想做。

- 题目7：将一个列表的数据复制到另一个列表中
> 007.py 程序分析：使用列表[:]。
