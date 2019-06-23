balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
fixedMonthlyPayment = 10
firstBalance = balance

while True:
    balance = firstBalance

    for i in range(12):
        unpaidBalance = balance - fixedMonthlyPayment
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)

        if balance <= 0:
            break
    
    if balance <= 0:
        break
    else:
        fixedMonthlyPayment += 10

print('Lowest Payment: ' + str(fixedMonthlyPayment))