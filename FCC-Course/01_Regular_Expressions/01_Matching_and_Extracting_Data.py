import re

text = 'My 2 favorite numbers are 19 and 45.'
plus = re.findall('[0-9]+', text) # [0-9]+ means that it will return the full number.
suppressed = re.findall('[0-9]', text) # [0-9] without + means that it will return each number found.
print(plus)
print(suppressed)

email = 'From: gzuanydev@gmail.com 03/11/22'
getEmail = re.findall('\S+@\S+', email) # find the string before the @ and after the @ until withe spaces at beginning and at the end.
print(getEmail)
