hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    floatingPointhours = float(hours)
    floatingPointRate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()    

if floatingPointhours > 40:
    regPay = floatingPointhours * floatingPointRate
    overtimePay = (floatingPointhours-40.0) * (floatingPointRate * 0.5)
    pay = regPay + overtimePay
else:
    pay = floatingPointhours * floatingPointRate

print('Pay:',pay)