
shifoudenglu=False
dengluzhanghao=''



users=[
    {'username':'zhangsan','password':'121212','balance':'500'},
    {'username':'lisi','password':'232323','balance':'1000'},
    {'username':'wangwu','password':'343434','balance':'2000'}
]


def caozuojiemian():
    '''
    操作界面
    '''
    while 1:
        print('''
        账号：%s
        ******************************************
        ************欢迎注册系统*******************
        *** 1.注册 2.登录 3.查询余额 4.存款 5.取款 *
        ************* 6.转账 7.退出****************'''%dengluzhanghao)
        a=int(input('请输入操作指令:'))
        if a==1:
            registered()
        elif a==2:
            login()
        elif a==3:
            get_balance()
        elif a==4:
            cunkuan()
        elif a==5:
            qukuan()
        elif a==6:
            zhuanzhang()
        elif a==7:
            tuichu()
        else:
            print('你输入的操作指令有误，请重新输入')









def registered():
    '''
    注册账号
    '''

    while 1 :
        print('欢迎注册')        
        a=input('请输入账号（注册）')
        for user in users:
            if a == user['username']:
                print('账号已存在')
                break
        else:
            b=input('请输入密码（注册）')            
            if len(b)<6:
                    print('密码必须大于等于6位！')
            else:
                print('注册成功！,获得3000元奖励')
                users.append({'username':a,'password':b,'balance':'3000'})
                caozuojiemian() 


def login():
    '''
    登录
    '''
    while 1 :
        a=input('请输入账号（登录）')
        b=input('请输入密码（登录）')
        for user in users:
            if a in user['username'] and b in user['password']:
                    print('登录成功')
                    global shifoudenglu
                    shifoudenglu=True
                    global dengluzhanghao
                    dengluzhanghao=a
                    caozuojiemian()
                    break
        else:
            print('账号或密码错误,请重新输入')


def get_balance():
    '''
    查询余额
    '''
    if shifoudenglu:
        for user in users:
            if dengluzhanghao==user['username']:
                print('你的账户余额为：%s'%user['balance'])
                caozuojiemian()
                break
    else:
        print('你还没有登录！')
        caozuojiemian()

def cunkuan():
    '''
    存款
    '''
    if shifoudenglu:
        a=input('请输入你要存入的金额：')
        for user in users:
            if dengluzhanghao==user['username']:
                b=int(user['balance'])
                a=int(a)
                c=str(a+b)
                user['balance']=c
                print('存钱成功，你现在的余额为：%s'%c)
                caozuojiemian()
                break
    else:
        print('你还没有登录！')
        caozuojiemian()

def qukuan():
    '''
    取款
    '''
    while 1:
        if shifoudenglu:
            a=input('请输入你要取出的金额：')
            for user in users:
                if dengluzhanghao==user['username']:
                    b=int(user['balance'])
                    a=int(a)
                    if b>a:
                        user['balance']=str(b-a)
                        print('取款成功，注意拿走你的现金,你现在的余额为：%s'%user['balance'])                    
                        caozuojiemian()
                        break
                    else:
                        print('对不起，你的余额不足，你的余额为：%s'%user['balance'])
                        caozuojiemian()
                    break
        else:
            print('你还没有登录！')
            caozuojiemian()

def zhuanzhang():
    '''
    转账
    '''
    while 1:
        if shifoudenglu:
            a=input('请输入你要转出的账户：')
            for user1 in users:
                if a==user1['username']:
                    for user in users:
                        if dengluzhanghao==user['username']:
                            b=input('请输入你要转出的金额：')
                            b=int(b)
                            c=int(user['balance'])
                            d=int(user1['balance'])
                            if c>=b :
                                user['balance']=str(c-b)
                                user1['balance']=str(d+b)
                                print('转账成功，你的余额为：%s'%user['balance'])
                                caozuojiemian()
                                break
                            else:
                                print('你的余额不足，转账失败')
                                break
        else:
            print('你还没有登录！')
            caozuojiemian()

def tuichu():
    '''
    退出系统
    '''
    print('感谢你的使用！')



if __name__ == "__main__":
    caozuojiemian()



