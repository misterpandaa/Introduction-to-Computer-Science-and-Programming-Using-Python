balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
paymentLowerBound = balance / 12
paymentUpperBound = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0
firstBalance = balance

while True:
    fixedMonthlyPayment = (paymentUpperBound + paymentLowerBound) / 2
    balance = firstBalance

    for i in range(12):
        unpaidBalance = balance - fixedMonthlyPayment
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        
    if balance < - 0.01:
        paymentUpperBound = fixedMonthlyPayment
    elif balance > 0.01:
        paymentLowerBound = fixedMonthlyPayment
    else:
        break            

print('Lowest Payment: ' + str(round(fixedMonthlyPayment, 2)))