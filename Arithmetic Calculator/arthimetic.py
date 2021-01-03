import math

def arithmetic_arranger(problems):
    # problems = ["29+89","79+23","5+10"]

#       32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474


    for problem in problems:
        if '+' in problem:
          variables = problem.split('+')
          operator = '+'
        elif '-' in problem:
          variables = problem.split('-')
          operator = '-'
        variable1 = variables[0]
        variable2 = int(variables[1])

        # Loop to print variable 1
    

        # print(f'Variable 1 : {variable1} , variable 2 : {variable2},operator:{operator}')
        if operator == '+':
            result = variable1 + variable2
        elif operator == '-':
            result = variable1 - variable2

        # Determining the length of dashes to be present 
        dashes = len(result) + 2

        print(f'{variable1}\n{operator}{variable2}\n-----\n{result}')


    # Arranged problems will be returning problem's answer
    arranged_problems = []
    return arranged_problems

arithmetic_arranger(['290+40','500-10','100-3','300+5'])