
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import xlrd
# import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import json
from collections import OrderedDict

date = xlrd.open_workbook("风盾风控策略(4).xlsx")
data = copy(date)
table = data.get_sheet(0)

f = open('a.text')
print(f)
date = f.readlines()
# print(date)
# print(date[0])
# print(len(date))
single = OrderedDict()

for i in range(0,len(date)):
    print(date[i])
    da = date[i].split(',')
    for j in range(0,4):
        table.write(i, j, da[j])
        single[da[i]] = da[j]
        print(single)




# for j in da.split(','):
#     print(j)

# print(data.split(',')[0])
data.save('风盾风控策略(4).xlsx')
