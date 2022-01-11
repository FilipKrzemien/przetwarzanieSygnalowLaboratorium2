from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

T=2
w=np.pi
p = 1.300

def f(t):
  return p*t**2

def f2(t):
  return f(t)*np.cos(w*t)

def f3(t):
  return f(t)*np.cos(2*w*t)

a0=1/T*quad(f, -1, 1)[0]
a1=2/T*quad(f2, -1, 1)[0]
a2=2/T*quad(f3, -1, 1)[0]


print("a0=",a0)
print('a1=',a1)
print('a2=',a2)

def F(t):
  return a0+a1*np.cos(np.pi*t)+a2*np.cos(2*np.pi*t)

t=np.linspace(-1, 1, 100)
fig, ax=plt.subplots()
ax.plot(t,f(t),t,F(t))
ax.grid(True)
plt.show()


a, b, c, t = symbols('a b c t')

expr1 = (a*t**2+2*b*t+c -(a0+a1*cos(w*t)+a2*cos(2*w*t)))*t**2
result1 = integrate(expr1, (t, -1, 1))
expr2 = (a*t**2+2*b*t+c -(a0+a1*cos(w*t)+a2*cos(2*w*t)))*t
result2 = integrate(expr2, (t, -1, 1))
expr3 = (a*t**2+2*b*t+c -(a0+a1*cos(w*t)+a2*cos(2*w*t)))
result3 = integrate(expr3, (t,-1,1))

equations = [
  Eq(result1, 0),
  Eq(result2, 0),
  Eq(result3,0)
]
print(solve(equations))