#Make a script that reads a string and print if it is a palindrome.

phrase = str(input('Write a word: ')).strip().upper()#remove whitespaces(out of phrase)
words = phrase.split()#split phase by separated words
union = ''.join(words)#join separated words without whitespace
EndOfWord = len(union)
flag = 1

for count_str1 in range(0, len(union), +1):
    if union[count_str1] != union[EndOfWord-1]:#1st char of str is equal last char of str -> 2nd, last-1 -> 3rd, (last-1)-1 -> ...
        flag = 0
        break

    EndOfWord-=1

if flag == 1:
    print('PALINDROME!')
else:
    print('IS NOT A PALINDROME!')