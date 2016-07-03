﻿# Python-Algorithms
http://www.runoob.com/python/python-100-examples.html

- 题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
> 001.py 程序分析：可填在百位、十位、个位的数字都是1、2、3、4，组成所有的排列后再去 掉不满足条件的排列。
001_1.py 程序分析：按照计算的方式组成三位数。
001_2.py 程序分析：沿用原有方法，利用格式化输出排列成三位数。

- 题目2：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
> 002.py 程序分析：利用数轴来分界，定位。通过数组进行分段计算累加。
002_1.py 程序分析：利用if elif 结构分段讨论。

- 题目3：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
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

- 题目8：输出9*9乘法口诀表。
> 008.py 程序分析：分行与列考虑，共9行9列，i控制行，j控制列
008_.py 程序分析：修改后呈现三角排列。（控制乘数相同显示在同一行）

- 题目9：暂停一秒输出。
> 009.py 程序分析：导入time模块，调用sleep方法。

- 题目10：暂停一秒输出。
> 010.py 程序分析：使用time.sleep

- 题目11***：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
> 011.py 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....类似斐波拉契数列。

- 题目12：判断101-200之间有多少个素数，并输出所有素数。
> 012.py 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数.

- 题目13：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
> 013.py 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。

- 题目14***: 将一个正整数分解质因数。例如：输入90,打印出90=2\*3\*3\*5
> 014.py 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

- 题目15: 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
> 015.py 程序分析：(a>b)?a:b这是条件运算符的基本例子

- 题目16***：输出指定格式的日期。
> 016.py 程序分析：使用 datetime 模块。

- 题目17: 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
> 017.py 程序分析：遍历字符串，用isalpha、isspace、isdigit判断统计个数。
str.isalnum()、str.islower()、str.istitle() 首字母是否为大写，且其他字母为小写、str. isupper() 所有的字母是否都为大写。

- 题目18：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
> 018.py 程序分析：关键是计算出每一项的值。

- 题目19***：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
> 019.py 程序分析：请参照程序Python 练习实例14。
OS常用模块：
os.name()字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
os.listdir()返回指定目录下的所有文件和目录名。
os.remove()函数用来删除一个文件。
os.system()函数用来运行shell命令。
os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
os.path.split()函数返回一个路径的目录名和文件名。

- 题目20：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
> 020.py 程序分析：单程距离为原高度的1/2,弹跳往返一次距离为2Hn

- 题目21： 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
> 021.py 程序分析：用倒推方法求解。

- 题目22**： 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
> 022.py 程序分析：ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值。

- 题目23**： 打印出*组成的菱形。
> 023.py 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

- 题目24***：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
> 024.py,024_1.py,024_2.py 程序分析：分子分母类似斐波拉契数列。

- 题目25：求1+2!+3!+...+20!的和。
> 025.py,025_py 程序分析：此程序只是把累加变成了累乘。

- 题目26***：利用递归方法求0！，1！，2！,3！，4！，5!
> 026.py 程序分析：递归公式：fn=fn(n-1)*n

- 题目27：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
> 027.py 程序分析：利用递归方法。

- 题目28：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
> 028.py 程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。

- 题目29：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
> 029.py 程序分析：学会分解出每一位数。

- 题目30：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
> 030.py 程序分析：前半段与后半段相同即可。x[i] != x[len(x)-i - 1]

- 题目31：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
> 031.py 程序分析：用if...else...方法进行判断

- 题目32：按相反的顺序输出列表的值。
> 032.py 程序分析：利用切片操作list[::-1]。

- 题目33：按逗号分隔列表。
> 033.py 程序分析：考察join的用法。

- 题目34：练习函数调用
> 034.py 程序分析：系统先调用threehellos，再由内部调用hello_world.

- 题目35：文本颜色设置。
> 035.py 程序分析：ANSI代码可以设置颜色。字背景颜色范围: 40--49 字颜色: 30--39。
具体参见：http://www.2cto.com/os/201208/146234.html

- 题目36***：求100之内的素数。
> 036.py: map、reduce、filter、lambda、列表表达式

- 题目37：对N个数进行排序。（提示用户输入所需读取的数字的个数！）
> 037.py: 可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

- 题目38：求一个3*3矩阵对角线元素之和
> 038.py: 利用双重for循环控制输入顺序，最后按照对角线下标特点进行求和。

- 题目39****（冒泡，没看懂）：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
> 039.py: 首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

- 题目40**：将一个数组逆序输出。
> 040.py: 用第一个与最后一个交换。

- 题目41****(没搞得懂)：模仿静态变量的用法。
> 041.py：

- 题目42：学习使用auto定义变量的用法。
> 042.py 没有auto关键字，使用变量作用域来举例吧。

- 题目43：模仿静态变量(static)另一案例。
> 043.py 演示一个python作用域使用方法

- 题目44：
>

- 题目45：
>

- 题目46：
>

- 题目47：
>

- 题目48：
>

- 题目49：
>

- 题目50：
>

- 题目51：
>

- 题目52：
>

- 题目53：
>

- 题目54：
>

- 题目55：
>

- 题目56：
>

- 题目57：
>

- 题目58：
>

- 题目59：
>

- 题目60：
>

- 题目61：
>

- 题目62：
>

- 题目63：
>

- 题目64：
>

- 题目65：
>

- 题目66：
>

- 题目67：
>

- 题目68：
>

- 题目69：
>

- 题目70：
>

- 题目71：
>

- 题目72：
>

- 题目73：
>

- 题目74：
>

- 题目75：
>

- 题目76：
>

- 题目77:
>


