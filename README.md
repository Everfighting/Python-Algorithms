﻿# Python-Algorithms
http://www.runoob.com/python/python-100-examples.html

- 题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

        001.py 程序分析：可填在百位、十位、个位的数字都是1、2、3、4，组成所有的排列后再去 掉不满足条件的排列。
        001_1.py 程序分析：按照计算的方式组成三位数。
        001_2.py 程序分析：沿用原有方法，利用格式化输出排列成三位数。

- 题目2：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

        002.py 程序分析：利用数轴来分界，定位。通过数组进行分段计算累加。
        002_1.py 程序分析：利用if elif 结构分段讨论。

- 题目3：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

        003.py 程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。(该数必小于10000)

- 题目4：输入某年某月某日，判断这一天是这一年的第几天？

        004.py 程序分析：先判断年份是否为闰年，然后在计算之前的月份的日期数。以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天

- 题目5：输入三个整数x,y,z，请把这三个数由小到大输出。

        005.py 程序分析：将输入的三个数逐个加入列表中，然后用sort方法进行排序，呈现从小到大的结果。

- 题目6：斐波那契数列。

        006.py 程序分析：斐波那契数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。 F0 = 0 (n=0) F1 = 1 (n=1) Fn = F[n-1]+ F[n-2] (n=>2)
        006_.py 程序分析：用递推的思想做。

- 题目7：将一个列表的数据复制到另一个列表中

        007.py 程序分析：使用列表[:]。

- 题目8：输出9*9乘法口诀表。

        008.py 程序分析：分行与列考虑，共9行9列，i控制行，j控制列
        008_.py 程序分析：修改后呈现三角排列。（控制乘数相同显示在同一行）

- 题目9：暂停一秒输出。

        009.py 程序分析：导入time模块，调用sleep方法。

- 题目10：暂停一秒输出。

        010.py 程序分析：使用time.sleep

- 题目11***：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

        011.py 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....类似斐波拉契数列。

- 题目12：判断101-200之间有多少个素数，并输出所有素数。

        012.py 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数.

- 题目13：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方

        013.py 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。

- 题目14***: 将一个正整数分解质因数。例如：输入90,打印出90=2\*3\*3\*5

        014.py 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
        (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
        (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
        (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

- 题目15: 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

        015.py 程序分析：(a>b)?a:b这是条件运算符的基本例子

- 题目16***：输出指定格式的日期。

        016.py 程序分析：使用 datetime 模块。

- 题目17: 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

        017.py 程序分析：遍历字符串，用isalpha、isspace、isdigit判断统计个数。
        str.isalnum()、str.islower()、str.istitle() 首字母是否为大写，且其他字母为小写、str. isupper() 所有的字母是否都为大写。

- 题目18：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

        018.py 程序分析：关键是计算出每一项的值。

- 题目19***：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

        019.py 程序分析：请参照程序Python 练习实例14。
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

        020.py 程序分析：单程距离为原高度的1/2,弹跳往返一次距离为2Hn

- 题目21： 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

        021.py 程序分析：用倒推方法求解。

- 题目22**： 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

        022.py 程序分析：ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值。

- 题目23**： 打印出*组成的菱形。

        023.py 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

- 题目24***：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

        024.py,024_1.py,024_2.py 程序分析：分子分母类似斐波拉契数列。

- 题目25：求1+2!+3!+...+20!的和。

        025.py,025_py 程序分析：此程序只是把累加变成了累乘。

- 题目26***：利用递归方法求0！，1！，2！,3！，4！，5!

        026.py 程序分析：递归公式：fn=fn(n-1)*n

- 题目27：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

        027.py 程序分析：利用递归方法。

- 题目28：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

        028.py 程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。

- 题目29：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

        029.py 程序分析：学会分解出每一位数。

- 题目30：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

        030.py 程序分析：前半段与后半段相同即可。x[i] != x[len(x)-i - 1]

- 题目31：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

        031.py 程序分析：用if...else...方法进行判断

- 题目32：按相反的顺序输出列表的值。

        032.py 程序分析：利用切片操作list[::-1]。

- 题目33：按逗号分隔列表。

        033.py 程序分析：考察join的用法。

- 题目34：练习函数调用

        034.py 程序分析：系统先调用threehellos，再由内部调用hello_world.

- 题目35：文本颜色设置。

        035.py 程序分析：ANSI代码可以设置颜色。字背景颜色范围: 40--49 字颜色: 30--39。
        具体参见：http://www.2cto.com/os/201208/146234.html

- 题目36：求100之内的素数。(好题！)

        036.py: map、reduce、filter、lambda、列表表达式

- 题目37：对N个数进行排序。（提示用户输入所需读取的数字的个数！）

        037.py: 可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

- 题目38：求一个3*3矩阵对角线元素之和

        038.py: 利用双重for循环控制输入顺序，最后按照对角线下标特点进行求和。

- 题目39：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。（好题！）

        039.py: 首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

- 题目40：将一个数组逆序输出。（好题）

        040.py: 用第一个与最后一个交换。

- 题目41：模仿静态变量的用法。(好题)

        041.py:

- 题目42:学习用auto定义变量的用法。(好题)

        042.py:分清楚局部变量和全局变量。

- 题目43：模仿静态变量(static)另一案例。（好题）

        043.py：演示一个python作用域使用方法

- 题目44****：

- 题目45：统计 1 到 100 之和。

        045.py for循环逐渐累加

- 题目46：求输入数字的平方，如果平方运算后小于 50 则退出。

        046.py 简单条件判断

- 题目47：两个变量值互换。

        047.py 定义一个互换变量的函数，并调用它。

- 题目48：数字比较。

        048.py if...else进行判断。

- 题目49：使用lambda来创建匿名函数。

        049.py 创建匿名函数lambda并调用它。

- 题目50：输出一个随机数。

        050.py 使用 random 模块。

- 题目51：学习使用按位与 & 。

        051.py 0&0=0; 0&1=0; 1&0=0; 1&1=1。

- 题目52：学习使用按位或 |

        052.py 0|0=0; 0|1=1; 1|0=1; 1|1=1

- 题目53：学习使用按位异或 ^

        053.py 0^0=0; 0^1=1; 1^0=1; 1^1=0

- 题目54*******：取一个整数a从右端开始的4〜7位。

        054.py
        (1)先使a右移4位。
        (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
        (3)将上面二者进行&运算。

- 题目55：学习使用按位取反~。

        055.py ~0=1; ~1=0;

- 题目56(略)：画图，学用circle画圆形。

        056.py Tk模块，后续再研究。

- 题目57：同上。

- 题目58：同上。

- 题目59：同上。

- 题目60：计算字符串长度。

        060.py len()函数

- 题目61******：打印出杨辉三角形（要求打印出10行如下图）。
    - 杨辉三角规律：

- 题目62：查找字符串

        str.find('str1')

- 题目63：画椭圆ellipse：略。

- 题目64：利用ellipse 和 rectangle 画图：略。

- 题目65：图形:略。

- 题目66：输入3个数a,b,c，按大小顺序输出。　
    - 读取三个数，if...else...判断大小，交换顺序。
    - 列表读取，并sort.

- 题目67*****：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

        逐一将输入数字存入列表
        判断最大数和最小数
        将最大数与第一个元素交换，最小数与最后一个元素交换。

- 题目68**********：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

- 题目69**********：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

- 题目70：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
    - 字符串长度len()

- 题目71*******：编写input()和output()函数输入，输出5个学生的数据记录。

- 题目72：创建一个链表:

- 题目73：反向输出一个链表。

        list.reverse() 列表方向排序

- 题目74：连接两个链表

        list.sort() 列表正向排序

- 题目75：放松一下，算一道简单的题目。

- 题目76*******：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n(利用指针函数)

- 题目77:循环输出列表

- 题目78**：找到年龄最大的人，并输出。请找出程序中有什么问题。

- 题目79：字符串排序。

- 题目80：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？

- 题目81******：809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

- 题目82*****：八进制转换为十进制

- 题目83*****: 求0—7所能组成的奇数个数

- 题目84：连接字符串。

- 题目85*****：判断一个素数能被几个9整除。

- 题目86：两个字符串连接程序。

- 题目87****：回答结果（结构体变量传递）。

- 题目88：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

- 题目89：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换

- 题目90：列表使用实例。

- 题目91：时间函数举例1。

        在Windows中最好使用clock()函数，而在其他平台上最好使用time.time()。

- 题目92：时间函数举例2。

- 题目93：时间函数举例3。

- 题目94：时间函数举例4,一个猜数游戏，判断一个人反应快慢。

- 题目95：字符串日期转换为易读的日期格式。

- 题目96：计算字符串中子串出现的次数。

- 题目97：从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入一个#为止。

- 题目98:从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

- 题目99：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

- 题目100：列表转换为字典。

