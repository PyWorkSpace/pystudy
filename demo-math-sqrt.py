# -*- coding:utf-8 -*-
import math

def quadratic(a,b,c):
    if not isinstance([a,b,c], (int, float)):
        TypeError('a bad operand type') 
    if a==0 :
         raise TypeError("a must be not zero")
    tmp=b*b-4*a*c
    if tmp<0 :
        raise TypeError("b*b must be greater than 4*a*c")
    n=math.sqrt(tmp)
    nx=(-b+n)/(2*a)
    ny=(-b-n)/(2*a)
    return nx,ny

print(quadratic(1,4,1))
print(quadratic(1,-4,4))
print(quadratic(1,"-4",4))