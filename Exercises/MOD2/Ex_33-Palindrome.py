#Make a script that reads a string and print if it is a palindrome.

word = str(input('Write a word: '))
word = word.split(' ')
EndOfWord = len(word)
flag = 1

for count_str1 in range(0, len(word), +1):
    if word[count_str1] != word[EndOfWord-1]:#1st char of str is equal last char of str -> 2nd, last-1 -> 3rd, (last-1)-1 -> ...
        flag = 0
        break
    
    EndOfWord-=1

if flag == 1:
    print('PALINDROME!')
else:
    print('IS NOT A PALINDROME!')