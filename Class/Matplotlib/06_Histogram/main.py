from itertools import filterfalse
import matplotlib.pyplot as plt 
import numpy as np
import statistics as st
plt.style.use('ggplot')

ages = [20, 25, 24, 23, 26, 27, 35, 46, 76, 34, 45, 56, 22, 1, 23]
bins = np.arange(0, 100, 10)#from 0 to 100 by 10 
clean = list(filterfalse(np.isnan, ages))  # Strip NaN values
clean = sorted(clean)
mean = st.mean(clean)

plt.axvline(mean)#insert a vertical line in plot

plt.hist(ages, bins = bins, edgecolor='black')

plt.show()
