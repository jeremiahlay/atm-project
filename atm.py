# Write a program that mimics an ATM

# set an initial balance
# then deduct from the account with a withdrawal
# Note that if you withdrawal more than the balance, your program should notifiy the user of insufficient funds

balance = 2000

amt_due = int(input('Enter the amount to withdrawal: '))

balance = balance - amt_due


if amt_due > balance:
    print('insufficient funds')
   
else:
    print('please take your cash')
    print('Avalaible Balance:',(balance))

print('This is the end of the ATM')



