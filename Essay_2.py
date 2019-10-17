import itertools
def readInfix(filename):
    with open(filename) as f:
        Infix = f.readlines()
    return Infix[0]
##########################################Student do these 2 function
#Illustrating a stack class
class Stack:#tao mot kieu du lieu stack de tinh toan
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
precedence = {'(':1,'~':4,'&':3,'|':3,'>':2,'=':2}#phan chia do uu tien
#   
def Infix2Postfix(Infix):
    space = ' '
    Infix = space.join(Infix)
    tokens = Infix.split()
    Postfix=[]
    opstack = Stack()
    for token in tokens:
        if token.isidentifier():
            Postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            while True:
                temp = opstack.pop()
                if temp is None or temp == '(':
                    break
                elif not temp.isidentifier():
                    Postfix.append(temp)
        else:
            if not opstack.empty():
                temp = opstack.peek()
                while not opstack.empty() and precedence[temp] >= precedence[token]:
                    Postfix.append(opstack.pop())
                    temp = opstack.peek()
            opstack.push(token)
    while not opstack.empty():
        Postfix.append(opstack.pop())
    final =''
    Postfix = final.join(Postfix)
    return Postfix
def Postfix2Truthtable(Postfix):
    Truthtable=Postfix
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
