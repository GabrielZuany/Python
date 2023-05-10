import matplotlib.pyplot as plt

plt.style.use('ggplot')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['brown', 'gray', 'black']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors, alpha=0.8)
plt.legend(loc=(0.779, 0.798))
plt.grid(True)
plt.tight_layout()

plt.show()