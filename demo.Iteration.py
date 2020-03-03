# -*- coding: utf-8 -*-  
from collections import Iterable

def testIteration():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key)
    for k,v in d.items():
        print(k,v)
    
print(isinstance('abc', Iterable),
isinstance([1,2,3], Iterable),
isinstance(123, Iterable))
testIteration()

for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)