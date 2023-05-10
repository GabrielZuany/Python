#Make a program that reads an integer and show his successor and predecessor
#Faça um programa que leia um inteiro e mostre seu sucessor e seu antecessor

num = int(input('Insert a number:'))
print('The predecessor of {} is {} and his successor is {}' .format(num, num-1, num+1))