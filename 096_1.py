str = 'stRINg lEArn'
str.center(20)  # 生成20个字符长度，str排中间
str.upper()  # 转大写
str.lower() #转小写
str.capitalize() #字符串首为大写，其余小写
str.swapcase()  # 大小写对换
str.title() #以分隔符为标记，首字符为大写，其余为小写
str.isalnum()  # 是否全是字母和数字，并至少有一个字符
str.isdigit()   #是否全是数字，并至少有一个字符
str.isalpha()   #是否全是字母，并至少有一个字符
str.islower()   #是否全是小写，当全是小写和数字一起时候，也判断为True
str.isspace()    #是否全是空白字符，并至少有一个字符
str.isupper()    #是否全是大写，当全是大写和数字一起时候，也判断为True
str.startswith('str')  # 判断字符串以'str'开头
str.endswith('arn')   #判读字符串以'arn'结尾
str.find('a')      #查找字符串，没有则返回-1，有则返回查到到第一个匹配的索引
str.rfind('n')     #同上，只是返回的索引是最后一次匹配的
str.index('a')     #返回索引值，如果没有匹配则报错
str.count('a')     #字符串中匹配的次数
str.replace('EAR','ear')  #匹配替换
str.strip('n')   #删除字符串首尾匹配的字符，通常用于默认删除回车符
str.lstrip('n')  # 左匹配
str.rstrip('n')  #右匹配
str.expandtabs()  #把制表符转为空格
str.decode('utf-8')                 #解码过程，将utf-8解码为unicode
str.decode('utf-8').encode('gbk')   #编码过程，将unicode编码为gbk
str.decode('utf-8').encode('utf-8') #编码过程，将unicode编码为utf-8

str = 'Learn string'
'-'.join(str)
'L-e-a-r-n- -s-t-r-i-n-g'

l1 = ['Learn', 'string']
'-'.join(l1)
'Learn-string'

str.split('n')
['Lear', ' stri', 'g']

str.split('n', 1)
['Lear', ' string']

str.rsplit('n', 1)
['Learn stri', 'g']

str.splitlines()
['Learn string']

str.partition('n')
('Lear', 'n', ' string')

str.rpartition('n')
('Learn stri', 'n', 'g')
