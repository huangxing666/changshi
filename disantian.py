# a= int(input('请输入你的年龄'))
# if a<12:
#     print('还在读小学')
# elif a<15:
#     print('在读初中')
# elif a<18:
#     print('在读高中')
# elif a<22:
#     print('在读大学')
# else :
#     print('社会人')
# a=input('输入年龄')
# if a in('0123456789'):
#     print('对')
# else :
#     print('错')
# name=['张三','李四','王五','任六','洪七','老八','宁九','楼十','台灯','水杯']
# nub=0
# b={}
# c={}
# while nub<10:
#     a=int(input('请输入'+name[nub]+'的成绩：'))
#     if a<60:
#         b[name[nub]]=a
#         nub=nub+1
#     else :
#         c[name[nub]]=a
#         nub=nub+1
# print('成绩不及格的同学：',b)
# print('成绩及格的同学',c)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'X',j,'=',i*j,end=' ')
#     print()

# zidian={}
# a=input('请输入你的账号：')
# if a[0] not in 'qwertyuiopasdfghjklzxcvbnm':
#     print('首位必须为小写字母！')
#     a=input('请输入你的账号：')
#     if len(a) <5 or len(a)>8:
#         print('请输入5-8个字符！')
#         a=input('请输入你的账号：')
# else :
#     zidian[username]=a
        # b=input('请输入你的密码：')
        # if len(b)<6 or len(b)>12:
        #     print('密码必须为6-12位！')
        #     b=input('请重新输入你的密码：')
        # else :
        #     zidian[password]=b
        #     print('注册成功！')
    # print('你的账号为：',a)

# def add(a,b):
#     '''加法'''
#     print(a+b)
# add(1,2)
# import pymysql
# pymysql.connect(host='127.0.0.1',user='root')
# print(type({}))
# print(list(range(0,20,2)))
# a={2,3,4,5,6,6,'dada','ewew','r4r3'}
# a.update()
# print(a)
# print(a)

# for i in range(10):
# 	print('你好')
# def jiafa(a,b):
#     '''
#     加法
#     '''
#     return(a+b)

# try:
#     print(jiafa('2',3))
# except:
#     print('代码错误')
class Yunsuanfu():

    def __init__(self):
        self.chengfa = '乘法'
        self.chufa='除法'



    def jiajian(self,num):
        if num==1:
            print('加法')
        else:
            print('减法')

yunsuan=Yunsuanfu()
yunsuan.jiajian(2)
# print(hasattr(yunsuan,'chengfa'))
print(yunsuan.chufa)