#Make a scrpit to print the N elements os Fibonacci sequence.
#0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21 -> 34 -> 55 -> 89 ....
MiddleTerm = 1
PreviousTerm = 0
NextTerm = 1

end = int(input('Insert the number of terms os Fibonacci that you want to see: '))
print('1 -> ', end='')

for count in range(0, end-1, +1):
    NextTerm = MiddleTerm+PreviousTerm
    print('{} -> ' .format(NextTerm, MiddleTerm, PreviousTerm), end = '')
    PreviousTerm = MiddleTerm
    MiddleTerm = NextTerm

print('END')