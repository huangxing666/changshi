a=(1,2,3)
b=(2,3,4)
c=(1,3,4)
d=(1,2,4)
e=[]
def jisuan(a):

    for i in a :
        for j in a:
            if j==i:
                pass
            else:
                if a[0]!=i and a[0]!=j:
                    f=i*100+j*10+a[0]
                    print(f)
                    e.append(f)
                elif a[1]!=i and a[1]!=j:
                    f=i*100+j*10+a[1]
                    print(f)
                    e.append(f)
                elif a[2]!=i and a[2]!=j:
                    f=i*100+j*10+a[2]
                    print(f)
                    e.append(f)
                else:
                    pass
jisuan(a)
jisuan(b)
jisuan(c)
jisuan(d)
print(e)
print(len(e))

update biao set color=yellow where car_color=black
