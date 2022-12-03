# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 01:03:41 2022

@author: jss10
"""
rps = []
RPSDict = {'A X':(1 + 3),
           'A Y':(2 + 6),
           'A Z':(3),
           'B X':(1),
           'B Y':(2 + 3),
           'B Z':(3 + 6),
           'C X':(1 + 6),
           'C Y':(2),
           'C Z':(3 + 3),}
RPSDict2 = {'A X':(3),
           'A Y':(1 + 3),
           'A Z':(2 + 6),
           'B X':(1),
           'B Y':(2 + 3),
           'B Z':(3 + 6),
           'C X':(2),
           'C Y':(3 + 3),
           'C Z':(1 + 6),}
with open('C:\\Users\\jss10\\Downloads\\AdventOfCode.txt','r',encoding="utf-8") as f:
    l = f.readlines()
    
    for line in l:
        rps.append(line.strip())
sum = 0
for i in rps:
    sum += RPSDict.get(i,0)
print(sum)