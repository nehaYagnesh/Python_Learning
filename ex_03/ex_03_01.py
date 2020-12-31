print('Calculate Pay')
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
floatingPointhours = float(hours)
floatingPointRate = float(rate)
#print(floatingPointhours,floatingPointRate)

if floatingPointhours > 40:
    # print('Overtime')
    regPay = floatingPointhours * floatingPointRate
    overtimePay = (floatingPointhours-40.0) * (floatingPointRate * 0.5)
   # print('Reg Pay',regPay , 'Overtime Pay',overtimePay)
    pay = regPay + overtimePay
else:
    #print('Regular')
    pay = floatingPointhours * floatingPointRate

print('Pay:',pay)