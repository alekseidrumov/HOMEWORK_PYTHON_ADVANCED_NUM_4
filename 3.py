from collections import Counter
f = open('Test.txt','r')
s = f.read()
list_s = s.split(",")
c = Counter()
for element in list_s:
    c[element] = c[element] + 1
print(c)
c_dict = dict(c)
max1 = 0
max_key1 = ''
for key, values in c_dict.items():
    if values > max1:
            max1 = values
            max_key1 = key
print('ТОП 1 —',max_key1)
max2 = 0
max_key2 = ''
for key, values in c_dict.items():
    if values > max2 and values < max1:
        max2 = values
        max_key2 = key
print('ТОП 2 —',max_key2)
max3 = 0
max_key3 = ''
for key, values in c_dict.items():
    if values > max3 and values < max2:
        max3 = values
        max_key3 = key
print('ТОП 3 —',max_key3)


