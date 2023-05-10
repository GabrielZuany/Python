'''Create a program where the user types any expression that uses parentheses. Your script should analyze whether the expression has open and closed parentheses in the correct order.'''

expression = input('EXP: ')
Open_P = expression.count('(')
Close_P = expression.count(')')
if Open_P == Close_P:
    print('Correct expression!')
else:
    print('Wrong expression!')