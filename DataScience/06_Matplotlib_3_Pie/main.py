import matplotlib.pyplot as plt

plt.style.use('ggplot')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode = [0, 0, 0, 0.1, 0]
plt.pie(slices, labels=labels, explode=explode, shadow = True, startangle=120, autopct='%1.1f%%', wedgeprops={'edgecolor':'white', 'linewidth':1.5})

plt.title('Most used Programming Languages')
plt.legend(labels, loc='upper left', bbox_to_anchor=(0.9, 0.2))
plt.tight_layout()

plt.show()