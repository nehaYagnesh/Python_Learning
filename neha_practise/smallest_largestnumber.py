def smallest_number(list):
    smallest_num = None
    for value in list:
        if smallest_num is None or smallest_num > value:
            smallest_num = value
    print('Smallest number is: ',smallest_num)



def largest_number(list):
    largest_number = None
    for value in list:
        if largest_number is None or value > largest_number:
            largest_number = value
    print('Largest number :',largest_number)

smallest_number([2,9,4,19,78,100,0,-1])
largest_number([2,9,4,19,78,100,0,-1])