'''Create a tuple with the Brasileirão teams. Then, show: 
A) The first 5 placed; 
B) The last 4 placed; 
C) A list with the teams ordered alphabetically; 
D) In what position is Flamengo.'''
Teams = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional', 'Atletico -MG', 'America-MG', 'Bragantino', 'Santos', 'Sao Paulo', 'Botafogo', 'Goias', 'Ceara SC', 'Fortaleza', 'Cuiaba', 'Avai', 'Coritiba', 'Atletico-GO', 'Juventude')

print('The first 5 placed are: {}\n' .format(Teams[:5]))
print('The last 4 placed are: {}\n' .format(Teams[14:]))
print('Sorted list:\n{}\n' .format(sorted(Teams)))
print(f'Flamengo position is: {Teams.index("Flamengo")+1}')