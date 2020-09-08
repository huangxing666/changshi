#阿巴啊吧
#5555
# a={'姓名':'黄兴','年龄':'22','学历':'本科'}
# print(a)
# print(a.get('学历1'))
# print(a['学历'])
# print(a.pop('年龄'))
# a.update(工作状态='待业')
# print(a)
# a=input('请输入你的姓名：')
# b=input('请输入你的年龄：')
# c=input('请输入你的性别：')
# d={'姓名':a,'年龄':b,'性别':c}
# print(d)


# a=input('请输入你的账号：')
# b=input('请输入你的密码：')
# zm={}
# if len(a)>4 and len(a)<9:
#     if a[0] in 'qwertyuiopasdfghjklzxcvbnm':
#         if len(b)>7 and len(b)<13:
#             print('注册成功')
#             zm.update(username=a)
#             zm.update(password=b)
#             print(zm)
#         else :print('请输入8-12位密码！')
#     else :print('必须以小写字母开头！')
# else :print('账号必须为5-8位！')
# i=int(0)
# while i<3:
#     print('第',i,'次')
#     i+=1

# a={'c':'1','b':'2'}
# for key,value in a.items():
#     print('key=%s,value=%s'%(key,value))

n=int(input('请输入一个2<=n<=109的数:'))
m=int(input('请输入一个1<=m的数:'))

a=range(1,n)
p=0
c=[]
for i in a:
    b=-i
    d=i-p*m
    if m==1:
        if i/2!=0:
            e=-i
            c.append(e)
            print('成功1')
        else:
            c.append(i)
            print('成功2')
    else:
        while (2*m)>d>m:
            
            c.append(i)
            print('成功3')
            continue
        else:
            c.append(b)
            print('成功4')
# for i in c:
#     print(sum(i))
print('sum(c)')

