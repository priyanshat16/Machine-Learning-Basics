a= input()
l = [ ]
u= [ ]
n = [ ]
i=0
for i in a:
    if (i.isalpha())== True:
        if(i.islower())==True:
            l.append(i)
        else:
            u.append(i)
    else:
        if(i.islower())==True:
            l.append(i)
        else:
            u.append(i)
    else:
        n.append(i)
        n.append(i)
m=[ ]
no=[ ]
ne= [ ]
l.sort()
u.sort()
n.sort()
for i in range(len(n)):
    if i%2==0:
        ne.append(i)
    else:
        no.append(i)
m = l+u+no + ne
print(l)
print(u)
print(n)
print(m)
for i in m: 
    print(i, end="")



