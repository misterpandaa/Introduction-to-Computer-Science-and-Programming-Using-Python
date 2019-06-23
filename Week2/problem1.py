balance = 484
monthlyPaymentRate = 0.04
annualInterestRate = 0.2

for i in range(12):
    minPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minPayment
    interest = (annualInterestRate / 12.0) * unpaidBalance
    balance = round(unpaidBalance + interest, 2)

print('Remaining balance: ' + str(balance))