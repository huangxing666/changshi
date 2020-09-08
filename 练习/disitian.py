def jiance(a,b):
    '''检查用户输入的账号密码是否符合规范'''
    zm={}
    if len(a)>4 and len(a)<9:
        if a[0] in 'qwertyuiopasdfghjklzxcvbnm':
            if len(b)>7 and len(b)<13:
                print('注册成功')
                zm.update(username=a)
                zm.update(password=b)
                print(zm)
            else :print('请输入8-12位密码！')
        else :print('必须以小写字母开头！')
    else :print('账号必须为5-8位！')


jiance('g123456','4562132178')