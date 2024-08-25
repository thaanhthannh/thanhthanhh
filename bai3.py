# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:00:37 2024

@author: Thanh Thanh
"""
#Bai3
n=int(input("Nhap so:"))
if 10 <= n <= 99:
    print("Tong cac chu so:", (n//10)+(n%10))
else:
    print("Khong xac dinh")
