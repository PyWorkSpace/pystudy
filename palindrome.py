# -*- coding: utf-8 -*-
def is_palindrome(n):
    l=len(n)
    if l<2:
        return true
    if l==2:
        return n[0:1]==n[-1:]
    
    