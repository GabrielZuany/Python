#make a script to approve a bank load. The script will ask the house price, 
#the buyer wage and the time he will take to pay it. 
# Calculate the monthly installment amount knowing that it cannot exceed 30% of the buyers wage, or the bank load will be denied.

BankLoad = float(input('Insert the bank load that you need: '))
BuyerWage = float(input('Insert your wage: '))
TimeToPay = float(input('How long do you plan to pay(years): '))#Manipulate same typedata

MonthlyAmount = BankLoad/(TimeToPay*12)

print('Monthly amount = {:.2f}' .format(MonthlyAmount))

if MonthlyAmount/BuyerWage <= 0.3:
    print('You bank load was approved!')
else:
    print('BANK LOAD DENIED!')