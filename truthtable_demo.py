import sys
from collections import OrderedDict
#Impliccation definition
def implies(lo1,lo2):
    return (not lo1) or lo2

x = 'RPQ&|'
y = x
numb_of_opt = []
for i in x:
    if not i.isalpha():
        numb_of_opt.append(i)
print(numb_of_opt)
numopt = len(numb_of_opt)
print(numopt)
vars = []
for i in x:
    print(i,end=' ')
    if i.isalpha() and not i in vars:
        vars.append(i)
#new_vars just contains only operrands
new_vars = sorted(vars)
new_vars_y = new_vars
math1 = []
math = []

#For operrand separate
for i in range(2**len(new_vars)):
    print('')
    string = bin(i)[2:].zfill(len(new_vars))
    bools = list(map((lambda x: True if x=='1' else False), string))
    math.append(bools)
    a = dict(zip(new_vars,bools))
    for j in  "".join(OrderedDict.fromkeys(x)):
        if j.isalpha():
            print(int(a[j]),end=' ')
print('\n','====================')
A=[tuple(a) for a in math]
print(A)
#For operator group up
math2 = []
math3 = []
for i in range(2**len(new_vars_y)):
  print('')
  string = bin(i)[2:].rjust(len(new_vars_y),'0')
  bools = list(map((lambda x: True if x=='1' else False), string))
  a = dict(zip(new_vars_y,bools))
  math.append(a)
  for j in y:
        if j.isalpha():
            math2.append(a[j])
            #print(int(a[j]),end=' ')
        elif j == '&':
            math2[-2] = math2[-1] & math2[-2]
            print(int(math2[-2]),end=' ')
            math3.append(math2[-2])
            del math2[-1]
        elif j == '|':
            math2[-2] = math2[-1] | math2[-2]
            print(int(math2[-2]),end=' ')
            math3.append(math2[-2])
            del math2[-1]
        elif j == '=':
            math2[-2] = implies(math2[-2],math2[-1]) and implies(math2[-1],math2[-2])
            print(int(math2[-2]),end=' ')
            math3.append(math2[-2])
            del math2[-1]
        elif j == '>':
            math2[-2] = implies(math2[-2],math2[-1])
            print(int(math2[-2]),end=' ')
            math3.append(math2[-2])
            del math2[-1]
        elif j == '<':
            math2[-2] = implies(math2[-1],math2[-2])
            print(int(math2[-2]),end=' ')
            math3.append(math2[-2])
            del math2[-1]
        elif j == '~':
            math2[-1] = not math2[-1]
            print(int(math2[-1]),end=' ')
            math3.append(math2[-1])
        else:
            print("Error: Invalid Character")
print('\n=======================')          
y = zip(*[iter(math3)]*numopt)
B = list(y)
print(B)
print(len(A),len(B))
#Sum of A and B to complete truth table
D = []
for i in range(0,len(B)):
    D.append(A[i]+B[i])
print(D)
