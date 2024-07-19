import math
import numbers as np


# ex1 #
x=5
y=9

x=None
print(X)
print(y)

del x
print(x)


#ex2#

S='123'
N=float(S)
print(type(S))
print(type(N))

#ex3#
s1="HELLO"
s2="hello"
print(s1==s2)
print(s1.lower()==s2)
print(s1==s2.upper())


#ex4#
print("The word 'Engineering' has 11 letters.")
print("The word 'Book' has 4 letters.")

#ex5#
str="python is great"
word="python"
print(word in str)

#ex6#
str="python is great"
print(str.split()[-1])

#ex7#
list_a=[1,8,9,15]
list_a.insert(1,2)
list_a.append(4)

#ex8#
list_a.sort()

#ex17#
arr=np.linespace(-10,10,100)
print(arr)

#ex18#

array_a = np.array([-1, 0, 1, 2, 0, 3])
result_array = array_a[array_a > 0]

print(result_array)

#ex19

array=[[3,5,3],[2,2,5],[3,8,9]]
array.T

#ex20#

zero_array=np.zeros(2,4)

#ex21
zero_array[:,1]=1

#ex22
from IPython.core.magic import register_cell_magic

@register_cell_magic
def clear_variables(line, cell):
    """
    A magic function to clear all variables in the Jupyter notebook.
    Usage: %%clear_variables
    """
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic('reset -f')
    