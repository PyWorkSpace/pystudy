# -*- coding: utf-8 -*-

def move(n,a,b,c):
    if not isinstance(n, (int, float)):
       raise TypeError('a bad operand type')
    if n<=0:
        raise TypeError('n 需要大于0')
    if n==1 :
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(4,'A','B','C')