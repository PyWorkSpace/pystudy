# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
       return self._width

    @property
    def hight(self):
        return self._hight

    @property
    def resolution(self):
        return self.hight*self.width

    @width.setter
    def width(self,width):
        if not isinstance(width, int):
            raise ValueError('width must be an float!')
        self._width=width
    
    @hight.setter
    def hight(self,hight):
        if not isinstance(hight, int):
            raise ValueError('hight must be an float!')
        self._hight=hight

s = Screen()
s.width = 1024
s.hight = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')