from collections import Counter
count = Counter()
for element in ['a','b',3,7,6,1,'b',9,3,6,8,8,'a']:
    count[element] = count[element] + 1
print(count)
