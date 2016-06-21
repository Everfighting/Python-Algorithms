# Python-Algorithms
http://www.runoob.com/python/python-100-examples.html

- 题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
> 001.py 程序分析：可填在百位、十位、个位的数字都是1、2、3、4，组成所有的排列后再去 掉不满足条件的排列。
001_1.py 程序分析：按照计算的方式组成三位数。
001_2.py 程序分析：沿用原有方法，利用格式化输出排列成三位数。

- 题目2：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
> 002.py 程序分析：利用数轴来分界，定位。通过数组进行分段计算累加。
002_1.py 程序分析：利用if elif 结构分段讨论。