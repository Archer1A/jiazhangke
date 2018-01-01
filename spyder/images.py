#coding:utf-8
#author:wangyijun
import xlrd
from collections import Counter
workbook = xlrd.open_workbook("贾樟柯_导演.xls")
sheet = workbook.sheet_by_index(0)
list=[]
for i in range(sheet.nrows):
    rows= sheet.row_values(i)
    list.append(rows[2][2:-2])
count_list = Counter(list)
x=[]
y=[]
list={}
for key,values in count_list.items():
    list[key]=values
x=sorted(list)
ll={}
for i in x:
    y.append(list[i])


#print(list_new)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(x,y)
plt.show()