# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:03:04 2018

@author: QinDong,cehui@139.com
"""

import math

def sign(x):
    "求符号函数：取参数的符号，返回1、0、-1"
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
    
def azimuth(x1,y1,x2,y2,style):
    "计算方位角函数,使用方法：azimuth(点A的X坐标，点A的Y坐标，点B的X坐标，点B的Y坐标，返回的方位角格式)"
    dltx=x2-x1
    dlty=y2-y1+1e-10
    a_tmp=math.pi*(1-sign(dlty)/2.0)-math.atan(dltx/dlty)
    a_tmp=a_tmp*180/math.pi
    return a_tmp


print(math.cos(2))
print(sign(-1))
print(azimuth(0,10,12,35,2))