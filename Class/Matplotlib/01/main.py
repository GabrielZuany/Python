from matplotlib import markers
import matplotlib.pyplot as plt

#print(plt.style.available)#shows the available theme plot
plt.style.use('ggplot')

# Median Developer Salaries by Age
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(dev_x, dev_y, marker= '.', label='All Devs') #build the plot


# Median Python Developer Salaries by Age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(py_dev_x, py_dev_y, marker= 'o', label='Python Devs')


js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(dev_x, js_dev_y, color='g', marker='*', label='JS Devs')


plt.xlabel('Ages') #x axis name
plt.ylabel('Median Salary(USD)')# y axis name
plt.title('Median Salary (USD) by Age')
plt.legend()

plt.grid(True)#shows the grid
plt.tight_layout()


plt.savefig('plot.png')#save the plot automatically

plt.show()