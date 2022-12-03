# -*- coding: utf-8 -*-

parsedNums = []

with open('C:\\Users\\jss10\\Downloads\\AdventOfCodeD1_1.txt','r',encoding="utf-8") as f:
    l = f.readlines()
    
    temp = []
    for line in l:
        if line.strip():
            temp.append(int(line))
        else:
            parsedNums.append(temp)
            temp = []

    
