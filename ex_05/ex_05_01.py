count = 0
total = 0.0
fval = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done' and count == 0:
        print('No numbers entered to perform math operations')
        continue
    elif sval == 'done' and count > 0:
        break
    
    try:
        fval = float(sval)
    except:
        print(f'{sval} is an invalid input')
        continue

    #print('Fval',fval)
    count = count + 1
    total = total + fval

print(f'Total: {total}, Count: {count}, Average : {total/count}')