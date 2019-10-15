import xlwt
import os
import importlib

def main():
    pass

if __name__ == "__main__":
    #Read Answers
    with open('CasesResult.Case') as f:
        Result = f.readlines()
    Result=[I.strip('\n') for I in Result]
    def str2bool(a):
        return a.lower() in ['true']
    #Write Result from file to TruthTableA
    TruthTableA=[list(tuple(str2bool(c) for c in b.split(sep=',')) for b in list(a for a in A.split(sep=';'))) for A in Result]
    print(TruthTableA[0])
    Dir=os.listdir()
    Dir=[a[0:-3] for a in Dir if '.py' in a and 'Test' not in a and 'Answer' not in a]
    print(Dir)
    book = xlwt.Workbook()
    sh = book.add_sheet('Sheet1')#Write XLSX HEADER
    sh.write(0,0,'ID')#Write XLSX HEADER
    #Read Testcases
    with open('Testcases.txt') as f:
        Infix = f.readlines()
    Infix=[I.strip('\n') for I in Infix]
    for i in range(1,len(Infix)+1):
        sh.write(0,i,f'Test {i}')#Write XLSX HEADER

    n=1
    for d in Dir:
        #Import Student program 
        mod = importlib.import_module(d)
        def combine(a):
            a=mod.Infix2Postfix(a)
            a=mod.Postfix2Truthtable(a)
            return a
        TruthTable=[combine(I) for I in Infix]
        #Compare Student program with TestResult
        Score=[T == TA for T,TA in zip(TruthTable,TruthTableA)]
        sh.write(n,0,d)
        #Write Scores to XLSX FILE
        for i in range(1,len(Score)+1):
            sh.write(n,i,Score[i-1])
        sh.write(n,len(Score)+1,sum(Score)/len(Score)*10)
        n+=1
    book.save('Score.csv')    