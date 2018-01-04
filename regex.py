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
greenHaRegex=re.compile(r'(Ha){3,5}')#默认贪心，匹配最长
mo1=greenHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreenHaRegex=re.compile(r'(Ha){3,5}?')#非贪心，匹配最短
mo2=nongreenHaRegex.search('HaHaHaHaHa')
print(mo2.group())
