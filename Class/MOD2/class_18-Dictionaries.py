data = dict()
data = {'name': 'Gabriel', 'age': 20}
data['New Element'] = 'M'#append do not work on dict

print(data['name'])
print(data['age'])
print(data['New Element'])

del data['New Element']
print(data)

print('-'*50)
movie = {'Title': 'Star Wars', 
         'Year': 1977, 
         'Director': 'George Lucas'}

print(movie.values())#content of dict
print(movie.keys())#identifiers of dict
print(movie.items())#both ^

for key, value in movie.items():
    print(f'The {key} is {value}')
print('-'*50)

movie_rental = list()
movie_info = dict()
for count in range(0, 3):
    movie_info['title'] = str(input('Title: '))
    movie_info['year'] = int(input('Year: '))
    movie_rental.append(movie_info.copy())#do not use [:] in dict
print(movie_rental)
