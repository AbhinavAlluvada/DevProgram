dict = {'Virat': 1400,'Rohit':4089,'Jadeja':3000,'Hardik':1630}
lst = []
for i in dict.values():
    lst.append(i)
sum = 0
for i in lst:
    sum = sum + i
print(lst)
print("Total Score:",sum)

for i in dict:
    print(i,"\t",(dict[i]/sum)*100)
