import math

def arithmetic_arranger(problems):

    operand1 = list()
    operator_list = list()
    operand2 = list()
    for problem in problems:
        if '+' in problem : 
            p1 = problem.split('+')
            operator = '+'
        elif '-' in problem :
            p1 = problem.split('-')
            operator = '-'
        operand1.append(p1[0])
        operand2.append(p1[1])
        operator_list.append(operator)
    


    print(' '.join('   {}'.format(x) for x in operand1))
    print('\t'.join('{}  {}'.format(x,y) for x,y in zip(operator_list,operand2)))
arithmetic_arranger(['29+89','79+23','5+10'])