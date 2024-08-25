# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:04:12 2024

@author: Thanh Thanh
"""
#Bai9
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
import math
term1 = (math.sqrt(a) - math.sqrt(b)) / (math.sqrt(math.sqrt(a)) - math.sqrt(math.sqrt(b)))
term2 = (math.sqrt(a) + math.sqrt(math.sqrt(a*b)) / math.sqrt(math.sqrt(a)) + math.sqrt(math.sqrt(b)))
result = term1 - term2
print("Ket qua:", result)
