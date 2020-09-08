import re
# 建议在正则表达式中，被比较的字符串前面加上r,不用担心转义字符的问题

# pat=re.compile('AA')     #此处的AA是正则表达式
# m=pat.search('CBAAcsAFFA')    #使用search方法来校验内容
# print(m)

#没有模式对象
# m=re.search('aa','cbaa')
# print(m)

# print(re.findall('[A-D]+','AADDEDDADADAAA'))

# sub方法
# print(re.sub('a','A','asdfasfdaefw'))   #在第三个字符串中，找到a用A替换

# print('\"da\eq')
# print('sda\t',45,end='')
class dog():
    def __init__(self):

print(dir(dog))