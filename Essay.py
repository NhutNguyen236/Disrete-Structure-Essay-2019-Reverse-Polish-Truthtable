import itertools
def readInfix(filename):
    with open(filename) as f:
        Infix = f.readlines()
    return Infix[0]
##########################################Student do these 2 function
class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
def Infix2Postfix(Infix):
    prec = {"(":1, "~":2, "|":3, "&":3, ">":4, "=":4}

    stack = Stack()
    postfix_list = []
    token_list = Infix

    for token in token_list:
        if token.isalpha():
            postfix_list.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = stack.pop()
        else:
            while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]) and token.isalpha():
                  postfix_list.append(stack.pop())
                  print(postfix_list)
            stack.push(token)
    while not stack.isEmpty():
        postfix_list.append(stack.pop())
    Postfix = "".join(postfix_list)
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
