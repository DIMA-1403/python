a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
import math
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('s=',s)