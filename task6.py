import random
x = []
for i in range(4):
    x.append(random.randint(1, 10))
print('first list', x)
a = x[:]
for i in x:
    a.append(i*2)
print('second list',  a)