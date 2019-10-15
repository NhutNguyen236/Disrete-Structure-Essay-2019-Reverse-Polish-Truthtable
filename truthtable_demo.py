import sys

while True:

    x = input("\n\nEnter Calculation: ").upper()

    vars = []
    for i in x:
        print(i,end=' ')
        if i.isalpha() and not i in vars:
            vars.append(i)

    for i in range(2**len(vars)):
        print('')
        string = bin(i)[2:].rjust(len(vars),'0')
        bools = list(map((lambda x: True if x=='1' else False), string))
        a = dict(zip(vars,bools))
        math = []
        for j in x:
            
            if j == '&':
                math[-2] = math[-2] & math[-1]
                print(int(math[-2]),end=' ')
                del math[-1]
                
            elif j == '|':
                math[-2] = math[-2] | math[-1]
                print(int(math[-2]),end=' ')
                del math[-1]
            elif j == '=':
                math[-2] = (math[-2] <= math[-1])and(math[-2] >= math[-1])
                print(int(math[-2]),end=' ')
                del math[-1]
            elif j == '>':
                math[-2] = math[-2] <= math[-1]
                print(int(math[-2]),end=' ')
                del math[-1]
            elif j == '<':
                math[-2] = math[-2] >= math[-1]
                print(int(math[-2]),end=' ')
                del math[-1]
            elif j == '~' or j == '|':
                math[-1] = not math[-1]
                print(int(math[-1]),end=' ')
            else:
                print("Error: Invalid Character")
