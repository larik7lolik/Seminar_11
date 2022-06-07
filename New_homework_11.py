## Дана функция  f(x)= - 8x^2+3x+17
## Определить корни
from sympy import *

x = Symbol('x')
func=-8*x**2+3*x+17
y=solve(func)
x1=float(y[0])
x2=float(y[1])

print(x1,x2)
## Найти интервалы на которых функция возрастает
fd=diff(func)
print(solve(0<fd))
## Найти интервалы на которых функция убывает
print(solve(fd<0))
## Построить график
import matplotlib.pyplot as plt
list_y=[]
for i in range(-100,100):
    x=i
    y=-8*x**2+3*x+17
    list_y.append(y)
print(list_y)

plt.plot(range(-100,100),list_y)
## 6. Определить промежутки, на котором f > 0
solve(0<func)