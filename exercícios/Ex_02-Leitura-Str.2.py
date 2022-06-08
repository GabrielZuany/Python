#Crie um script que leia o dia, mes e ano de uma pessoa e mostre a data formatada

dia = input('Dia = ')
mes = input('Mes =  ')
ano = input('Ano = ')

print('Você nasceu no dia',dia,'de',mes,'de',ano)
#OU
print('Você nasceu no dia {} de {} de {}' .format(dia, mes, ano))
