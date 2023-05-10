#Make a script that asks a persons gender and if it isnot M or F, keep asking ultil user insert a valid value.
value = 'a'
while value not in 'FM':
    value = input('Insert your gender [M/F]').upper()
    continue