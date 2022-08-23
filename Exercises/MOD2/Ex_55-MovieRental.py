movie_rental = list()
movie_info = dict()
QuantityOfMovies = int(input('How many movies do you want to save? '))

for Index in range(0, QuantityOfMovies):
    movie_info['title'] = str(input('Title: '))
    movie_info['year'] = str(input('Year: '))
    movie_info['director'] = str(input('Director: '))
    movie_rental.append(movie_info.copy())

choice = 'Y'
while choice == 'Y':
    option = int(input('Witch movie do you want to see details? '))
    
    if option > QuantityOfMovies:
        print('Invalid option!')
        exit(0)
        
    match option:
        case option:
            print(movie_rental[option-1])
        
    choice = str(input('Do you want to see another movie description? [Y/N] ')).upper()