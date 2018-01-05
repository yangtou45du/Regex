#1.正则表达式基本步骤：
'''
import re
regex=re.compile("")
match=regex.search()
match.group()
'''
#2.括号分组
import  re
'''
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('my number is 415-555-4242.')
print (mo.group(1))#415
print (mo.group(2))#555-4242
print (mo.group(0))#415-555-4242
print(mo.group())#415-555-4242
print (mo.groups())#（‘415’，‘555-4242’）
areaCode,mainNumber=mo.groups()
print (areaCode)#415
print(mainNumber)#555-4242
'''
#3.管道匹配多个分组
'''
heroRegx=re.compile(r'Batman|Tina Fey')
mo1=heroRegx.search('Batman and Tina Fey.')
print(mo1.group())#Batman  匹配第一个
mo2=heroRegx.search(r'Tina Fey and Batman.')
print(mo2.group())#Tina Fey

batRegx=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegx.search("Batmobile lost a wheel")
print (mo.group())#Batmobile
print  (mo.group(1))#mobile
print (mo.groups())#('mobile',)
'''
#4.问号实现可选分配
'''
batRegx=re.compile(r'Bat(wo)?man')
mo1=batRegx.search('the adventures of Batman')
print(mo1.group())#Batman
'''
#5.星号匹配零次或者多次
'''
batRegx=re.compile(r'Bat(wo)*man')
mo1=batRegx.search('the adventures of Batman')
print(mo1.group())#Batman
mo2=batRegx.search('the adventures of Batwoman')
print(mo2.group())#Batwoman
mo3=batRegx.search('the adventures of Batwowowowoman')
print(mo3.group())#Batmwowowoan
'''
#6.加号匹配一次或者多次
'''
batRegx=re.compile(r'Bat(wo)+man')
mo1=batRegx.search('the adventures of Batman')
print(mo1)#None
mo2=batRegx.search('the adventures of Batwoman')
print(mo2.group())#Batwoman
mo3=batRegx.search('the adventures of Batwowowowoman')
print(mo3.group())#Batmwowowoan
'''
#7.花括号匹配特定次数
'''
(ha){3}等同(ha)(ha)(ha)
(ha){3,5}等同(ha)(ha)(ha)｜(ha)(ha)(ha)(ha)｜(ha)(ha)(ha)(ha)(ha)

'''
#8.贪心和非贪心匹配
'''
greenHaRegex=re.compile(r'(Ha){3,5}')#默认贪心，匹配最长
mo1=greenHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreenHaRegex=re.compile(r'(Ha){3,5}?')#非贪心，匹配最短
mo2=nongreenHaRegex.search('HaHaHaHaHa')
print(mo2.group())
'''
#9.findall()方法
#search返回第一次匹配的findall返回所有的匹配,是一个字符串列表
'''
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('cell:415-555-9999,work:212-555-0000')
print(mo.group())#415-555-9999
print (phoneNumRegex.findall("cell:415-555-9999,work:212-555-0000"))#['415-555-999','212-555-0000']
phoneNumRegex1=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print (phoneNumRegex1.findall("cell:415-555-9999,work:212-555-0000"))#[('415','555','999'),('212','555','0000')]
'''
#10.字符分类
'''
\d:0~9的数字
\D：除0~9以外的任何字符
\w：任何字母，数字或下划线（匹配单词）
\W：除字符，数字。和下划线以外的任何字符
\s：空格，制表符，或者换行符（可以认为匹配空白字符）
\S：除空格，制表符。换行符以外的任何字符
'''
#11.建立自己的字符分类】
'''
[aeiouAEIOU]匹配所有的元音字符
[^AEIOUaeiou]匹配所有非元音字母
[a-zA-Z0-9]匹配所有的大小写字符与数字

'''
#12.插入字符和美元字符
'''
开始处使用^字符表明匹配必须发生在备查找文本的开始处
$表示必须以这个正则表达式模式结束
'''
'''
beginWithHello=re.compile(r'^Hello')
mo=beginWithHello.search('Hello word')
print (mo.group())#Hello
mo1=beginWithHello.search('he said Hello')
print (mo1)

endsWithNumber=re.compile(r'\d$')#以数字结束
mo2=endsWithNumber.search('your number is 42')
print(mo2.group())#2
endsWithNumber=re.compile(r'\d+$')#以数字结束
mo2=endsWithNumber.search('your number is 42')
print(mo2.group())#42

'''
#13.通配字符（句点）匹配除了换行之外所有的字符,只匹配一个字符
'''
atRegex=re.compile(r'.at')
mo=atRegex.findall('the cat in the hat sat on the flat mat at')
print (mo)
'''
#14.点-星匹配所有字符
'''
nogreedyRegex=re.compile(r'<.*?>')#非贪心模式
mo=nogreedyRegex.search('<to serve man> for dinner.>')
print(mo.group())
greedyRegex=re.compile(r'<.*>')#贪心模式
mo1=greedyRegex.search('<to serve man> for dinner.>')
print(mo1.group())
'''
#15.句点匹配换行，传入re.DOTALL
'''
noNewlineRegex=re.compile(r'.*')
mo=noNewlineRegex.search('serve the public .\nprotect').group()
print(mo)
NewlineRegex=re.compile(r'.*',re.DOTALL)
mo1=NewlineRegex.search('serve the public .\nprotect').group()
print(mo1)
'''
#16.不区分大小写、re.I
'''
robocop=re.compile(r'robocop',re.I)
mo=robocop.search('RoBocop').group()
print(mo)
'''
#17.sub()替换字符串
nameRegex=re.compile(r'Agent \w+')
mo=nameRegex.sub('CENSON','Agent Alice GAVE')
print(mo)



















