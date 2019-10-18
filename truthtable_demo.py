import sys

#Impliccation definition
def implies(lo1,lo2):
    return (not lo1) or lo2

x = 'P~QRP&>|R>'
y = x
vars = []
for i in x:
    print(i,end=' ')
    if i.isalpha() and not i in vars:
        vars.append(i)
#new_vars just contains only operrands
new_vars = sorted(vars)
new_vars_y = new_vars
#For operrand separate
for i in range(2**len(new_vars)):
    print('')
    string = bin(i)[2:].rjust(len(new_vars),'0')
    bools = list(map((lambda x: True if x=='1' else False), string))
    a = dict(zip(new_vars,bools))
    math1 = []
    for j in x:
        if j.isalpha():
            math1.append(a[j])
            print(int(a[j]),end=' ')
print('\n','====================')
#For operator group up
for i in range(2**len(new_vars_y)):
  print('')
  string = bin(i)[2:].rjust(len(new_vars_y),'0')
  bools = list(map((lambda x: True if x=='1' else False), string))
  a = dict(zip(new_vars_y,bools))
  math2 = []
  for j in y:
        if j.isalpha():
            math2.append(a[j])
            #print(int(a[j]),end=' ')
        elif j == '&':
            math2[-2] = math2[-1] & math2[-2]
            print(int(math2[-2]),end=' ')
            del math2[-1]
        elif j == '|':
            math2[-2] = math2[-1] | math2[-2]
            print(int(math2[-2]),end=' ')
            del math2[-1]
        elif j == '=':
            math2[-2] = implies(math2[-2],math2[-1]) and implies(math2[-1],math2[-2])
            print(int(math2[-2]),end=' ')
            del math2[-1]
        elif j == '>':
            math2[-2] = implies(math2[-2],math2[-1])
            print(int(math2[-2]),end=' ')
            del math2[-1]
        elif j == '<':
            math2[-2] = implies(math2[-1],math2[-2])
            print(int(math2[-2]),end=' ')
            del math2[-1] 
        elif j == '~':
            math2[-1] = not math2[-1]
            print(int(math2[-1]),end=' ')
        else:
            print("Error: Invalid Character")
