![alt text](https://camo.githubusercontent.com/38eee254b913ee3775e6739f068ce7428d54c941/68747470733a2f2f696d672e736869656c64732e696f2f636972636c6563692f70726f6a6563742f6769746875622f6261646765732f736869656c64732f6d6173746572)
# Disrete-Structure-Essay-2019-Truth Table Generation from postfix
## Date: 15/10/2019
## Introduction: 
In this rep, I commit that I borrowed some codes on the internet and they are, respectively: [link 1](https://github.com/benjameep/truth-table/blob/master/README.md) for truthtable generating from postfix and [link 2](https://rextester.com/VGJZ53355) for infix to postfix generating 

## Contents:
- Firstly, if your computer does not have any library for excel file exporting for Python 3, I am sure that you should have one with bash below:
```bash
pip install xlwt
```
- Programing Language: Python 3.

**Attention:** *"Elsewhere" contents or misslead libraries will not be used in this essay.* 

## Programming Requirement:
1. Write function def Infix2Postfix(Infix):

a. Input: Infix is a string of logical operators (Table 1) and alphabet characters
from “A” to “Z” express a logic expression.

b. Output: Postfix is a string calculated from Infix using Reverse Polish notation.

2. Write function def Postfix2Truthtable(Postfix):

a. Input: Postfix from (1.)

b. Output: The truth table from the input logic expression Infix.

* The truth tables should be in alphabet order for initial variables

* Student must not add header to your truth table.

3. Apply your functions on Essay.py (given by Instructors)

4. Change the file name to <StudentID>.py (ex: student 19000123 should make the file
19000123.py)
 
5. Summit your file to appropriate place on https://elit.tdtu.edu.vn/

Example:
Input: R|(P&Q)

Output: (Student must not add header)

![alt text](https://github.com/NhutNguyen236/Disrete-Structure-Essay-2019-Reverse-Polish-Truthtable/blob/master/truh.png)

## Operator Meaning

| Operator |         Q         |
|:--------:|:-----------------:|
|     (    |  Open parenthesis |
|     ~    |         Not       |
|     |    |         Or        |
|     &    |        And        |
|     >    |    Implication    |
|     =    |   Bi implication  |
|     )    | Close parenthesis |

*Table 1. Logic Operator with precedence from top to bottom*

## Report Requirement:
!!The report should be written individually even if you are in a group of 2.
Create a Word or Latex document Using the report template and format your document
as is. The content should cover all the following requirements.
1. First chapter introduces your group members (up to 2), work you finished up on each
week, how you shared your work (if you have 2 members), and finally introduce what
other chapters do.
2. Second chapter includes the theory of Reverse Polish and Basic logic used on
calculation of Truth tables.
3. Third chapter should explain your program by doing step by step each function on Test
Case 1 and 2 (The codes should be on your report).
4. Fourth chapter shows your experimental result on 5 testcases (run the code on 5 test
cases and copy the screen picture (!!!don’t use mobile phone to catch the screen!!!)).
5. Fifth chapter lists all the references (if any including website)
6. Export your document to PDF format and change the file name to <StudentID>.pdf
7. Summit your file to appropriate place on https://elit.tdtu.edu.vn/
