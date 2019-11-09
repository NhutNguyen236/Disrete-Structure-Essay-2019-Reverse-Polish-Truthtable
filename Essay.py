import itertools
def readInfix(filename):
    with open(filename) as f:
        Infix = f.readlines()
    return Infix[0]
##########################################Student do these 2 function
#Illustrating a stack class
class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
        
    def push(self, val):
        self.items.append(val)
        self.length += 1
        
    def pop(self):
        if self.empty():
            return None
        self.length -= 1
        return self.items.pop()
        
    def size(self):
        return self.length
    
    def peek(self):
        if self.empty():
            return None
        return self.items[self.size()-1]
    
    def empty(self):
        return self.length == 0
    
    def __str__(self):
        return str(self.items)
# Precedence for each operator
precedence = {'(':0,'~':5,'&':4,'|':3,'>':2,'=':1}
def Infix2Postfix(Infix):
    #wrap infix up into one place when there are spaces 
    Infix = ' '.join(Infix)
    #break Infix into chunks which called token then store in tokens 
    tokens = Infix.split()
    Postfix=[]
    stack = Stack()
    #access to every token in tokens 
    for token in tokens:
        #if the checking token is alphabetic, put it in Postfix
        if token.isalpha():
            Postfix.append(token)
        #if not but token is a left parenthese push it to stack 
        elif token == '(':
            stack.push(token)
        #if it is not but it is a right parenthese, then check:
        elif token == ')':
            while True:
                #using a vari named temp to keep stack pop
                temp = stack.pop()
                #if temp is empty or it is left parenthses then break go to next step
                if temp is None or temp == '(':
                    break
                #if not but thing inside temp is alphabetic put it in Postfix
                elif not temp.isalpha():
                    Postfix.append(temp)
        #if it is not right parenthese but it is a '~' and followed by another '~', push both to the satck
        elif token == '~' and stack.peek() == '~':
                stack.push(token)
        #if none of the above 
        else:
            #when stack is not empty then peek each element then compare precedence if peeked token has higher prec than the token is 
            #pushed to stack then pop it out and put in Postfix and repeat
            if not stack.empty():
                temp = stack.peek()
                while not stack.empty() and precedence[temp] >= precedence[token]:
                    Postfix.append(stack.pop())
                    temp = stack.peek()
            stack.push(token)
    #this step is reached to the end of postfix and stack is not empty yet then pop all out and put the rest in postfix
    while not stack.empty():
        Postfix.append(stack.pop())
    #Rejoin the list named Postfix to turn it into a string
    Postfix = ''.join(Postfix)
    #return result 
    return Postfix

# Define an implication function 
def implies(lo1,lo2):
    return (not lo1) or lo2

def Postfix2Truthtable(Postfix):
    #Creating a list to contain only operands named opd
    opd = []
    for i in Postfix:
        if i.isalpha() and not i in opd:
            opd.append(i)
    #create order for opd
    order_opd = sorted(opd)
    order_opd_new = opd
    #number of rows
    rows = 2**len(order_opd)
    #creat an empty sub_truthtable :)
    sub = []
    for i in range(rows):
        #Turning each i into binary form and fill up with right amount of 0 
        string = bin(i)[2:].zfill(len(order_opd))
        #turn 1 into True and 0 into False and map them up as a list ready for putting them as rows
        bools = list(map((lambda x: True if x=='1' else False),string))
        sub.append(bools)
    #turn sub_truthtable into tuple ready for mounting
    A = [tuple(x) for x in sub]
    #temp list for element assignment math2,3
    math2 = []
    math3 = []
    for i in range(rows):
        string = bin(i)[2:].zfill(len(order_opd))
        bools = list(map((lambda x: True if x=='1' else False),string))
        el = dict(zip(order_opd,bools))
        #loop in every token of Postfix
        for j in Postfix:
            #check if j is alphabet, if yes append dictionary of i to temporary list name math2
            if j.isalpha():
                math2.append(el[j])
            # if it is &,|,=,> calculate 2 first operand before that operator then delete itself to fit in math3
            elif j =='&':
                math2[-2] = math2[-1] and math2[-2]
                math3.append(math2[-2])
                del math2[-1]
            elif j =='|':
                math2[-2] = math2[-1] or math2[-2]
                math3.append(math2[-2])
                del math2[-1]
            elif j == '=':
                math2[-2] = implies(math2[-2],math2[-1]) and implies(math2[-1],math2[-2])
                math3.append(math2[-2])
                del math2[-1]
            elif j == '>':
                math2[-2] = implies(math2[-2],math2[-1])
                math3.append(math2[-2])
                del math2[-1]
            elif j == '~':
                math2[-1] = not math2[-1]
                math3.append(math2[-1])
            #if there is something diffrent from ~&|>= then append Invalid to math3 
            else:
                math3.append("Invalid")
    #create an empty truthtable waiting for tuple up :)
    Truthtable = []
    #couting number of operators
    opt_lst = []
    for i in Postfix:
        if not i.isalpha():
            opt_lst.append(i)
    numopt = len(opt_lst)
    #Splitting the second table into 'numopt' of tuple 
    y = zip(*[iter(math3)]*numopt)
    B = list(y)
    #Tuple up the truthtable
    for i in range(0,len(B)):
        Truthtable.append(A[i]+B[i])
    return Truthtable
##########################################End student part
def writeTruthtable(table):
    import sys
    outfile=sys.argv[0]
    outfile=outfile[0:-2]
    outfile+="txt"
    with open(outfile, 'w') as f:
        for lines in table:
            for item in lines:
                f.write("%s\t" % item)
            f.write("\n")
    f.close()
def main():
    Infix=readInfix("Logicexpression.txt")
    Postfix=Infix2Postfix(Infix)
    Truthtable=Postfix2Truthtable(Postfix)
    writeTruthtable(Truthtable)
main()
