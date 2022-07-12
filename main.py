import math
import os
import random
import re
import sys
import statistics
import numpy as np
import pandas as pd

def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def valuation(reqArea, area, price):
    #print(len(area))
    home=[]
    price_home=0
    for i in range(0,len(area)):
        d=duplicates(area, area[i])
        d.remove(i)
        if len(d)==0:
            home.append([area[i],price[i]])
        else:
            cmplist=[price[d[i]] for i in range(0,len(d))]
            mp=statistics.mean(cmplist)
            std=statistics.pstdev(cmplist)
            if abs(mp - price[i]) <= 3 * std:
                home.append([area[i],price[i]])
    #print(home)
    if len(home)==0 :
        price_home=int(round(1000))
    if len(home) == 1:
        price_home=int(round(home[0][1]))
    matches=[]
    for i in range(0,len(home)):
        if home[i][0]==reqArea:
            matches.append(home[i][1])
    if len(matches)>=1:
        return statistics.mean(matches)
    r=home.copy()
    r.sort()
    uniquef=[x[0] for x in r]
    # extrapolation of price 
    if len(set(uniquef)) == len(uniquef):
        if reqArea>r[len(r)-1][0]:
            min1=r[len(r)-2]
            max1=r[len(r)-1]
            s=[]
            s.append(min1[1])
            s.append(max1[1])
            price_home=int(round(max1[1]+(reqArea-max1[0])*(max1[1]-statistics.mean(s))/(max1[0]-min1[0])))
    else:
        if reqArea>r[len(r)-1][0]:
            min1=r[len(r)-2]
            max1=r[len(r)-1]
            s=[]
            for u in r:
                if min1[0] in u:
                    s.append(u[1])
            price_home=int(round(max1[1]+(reqArea-max1[0])*(max1[1]-statistics.mean(s))/(max1[0]-min1[0])))         
    for i in range(0,len(r)):
        if r[i-1][0]<reqArea  and r[i][0]>reqArea :
            min1=r[i-1]
            max1=r[i]
            price_home=int(round(min1[1] + (reqArea - min1[0]) * (max1[1] -(min1[1])) / (max1[0] - min1[0])))
            break
    if price_home>=1000000:
        price_home=int(round(1000000))
    if price_home<=1000:
        price_item=int(round(1000))
    return price_home