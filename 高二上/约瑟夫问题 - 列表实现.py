# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:29:36 2021

@author: lenovo
"""

import time
llist=[0]
n=int(input(" 请输入参与人数（ N ） :"))
m=int(input(" 请输入淘汰数（ M ） :"))
#开始计时
start = time.clock()

for i in range(n):
    llist.append(i+1)
long=n
i=1
k=1
while long>1:
    if i==m:
        llist.pop(k)
        long=long-1
        i=0
        k-=1
    k=k%long+1
    i+=1
print(llist[1])
end = time.clock()
print("it  cost %s s for func running " %(end - start))