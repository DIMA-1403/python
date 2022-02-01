import random
x = []
for i in range(12):
    x.append(random.randint(7500, 15000))
print('salary', x)
a = x
for i in x:
    a.append(i )
print('second list',  a)
