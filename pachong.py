a=open('gushi.txt','w',encoding='utf8')
a.write('静夜思\n作者：李白\n床前明月光，疑是地上霜。\n举头望明月，低头思故乡。')
a.close()

def du(a):
    try:
        a=open('gushi.txt','r',encoding='utf8')
        b=a.readlines()
        a.close()
        print(b)
        return b
    except Exception as f:
        print('第一个方法错误',f)
def xie(b):
    try:
        c=open('gushi2.txt','w',encoding='utf8')
        for i in b:
            c.write(i)
        c.close()
        
    except Exception as d:
        print('第二个方法错误',d)

try:
    xie(du(a))
    g=open('gushi2.txt','r',encoding='utf8')
    for i in g.readlines():
        print(i)
except Exception as e:
    print('第三个代码错误',e)