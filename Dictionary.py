dict = {'Virat': 100,'Rohit':49,'Jadeja':30,'Hardik':23}
dict['Gill'] = 25
#print(dict)
dict['Jadeja'] = 50
#print(dict)
dict.update({'Virat':0})
#print(dict)
dict.update({'Hardik':3,'Rahane':40})
#print(dict)
dict.setdefault('Rohit',12)
#print(dict)
dict.setdefault('Pujara',150)
#print(dict)
dict.pop('Pujara',150)
#print(dict)
dict.popitem()
#print(dict)
#print(dict.get('Rohit'))
lst = [1,2,3,4,4,5]
dct = dict.fromkeys(lst)
print(dct)
dct.update({1:10,2:12,3:15})
print(dct)
for i in dict:
    print(i,'\t',dict[i])
print('\n')
for i in dict.keys():
    if i == 'Rohit':
        dict[i] = 2
for i in dict:
    print(i,'\t',dict[i])
print(dict.keys())
print(dict.values())
print(dict.items())
for i in dict:
    print(dict.values())