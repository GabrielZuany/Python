from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd
import mplcursors as mpc

plt.style.use('ggplot')

# Without Pandas
'''
import csv
import numpy as np

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    language_counter = Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
        # row['LanguageWorkedWith'].split(;) = ['HTML/CSS', 'JavaScript', 'Python', ...]
        # language_counter.update() = Like dict.update() but add counts instead of replacing them.

'''

# Using Pandas

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
        language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(): #item is a tuple
    languages.append(item[0])
    popularity.append(item[1])
    
languages.reverse() # to plot the barchart topdown
popularity.reverse()    

plt.barh(languages, popularity, height=0.5, alpha=0.75) # horizontal bar

plt.title("Most popular languages")
plt.ylabel("Programming languages")
plt.xlabel("Number of people who use")

plt.tight_layout()

mpc.cursor(hover=2) # create a cursor hover

plt.show()