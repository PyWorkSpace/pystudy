# -*- coding:utf-8 -*-

def add_end(L=None):
    if(L==None):
        L=[]
    L.append('END')
    return L

print(add_end())
print(add_end(['first','second']))

def calc(num):
    sum=0
    for n in num:
        sum+=n*n
    return sum

print(calc([1,2,3]))

def calc2(*num):
    sum=0
    for n in num:
        sum+=n*n
    return sum

print(calc2(1,2,3))

nums = [1, 2, 3]
print(calc2(*nums))

def person(name,age,**kv):
    print('name:',name,'age:',age,'other:',kv)

person('robin','29')
person('robin','29',city='chizhou',gender='Male')
