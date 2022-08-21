from cmath import sin, tan
import numpy as np 
from sympy import *


x=Symbol("x")
y=csc(x)**2+1

yprime=y.diff(x)
print(yprime)
