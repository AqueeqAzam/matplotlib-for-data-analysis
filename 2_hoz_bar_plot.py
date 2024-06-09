import matplotlib.pyplot as plt
import numpy as np

x = ['Python', 'c++', 'Java', 'javaScript']
y = [85, 50, 75, 80]
z = [55, 44, 48, 52]
c = ['r', 'y', 'g', 'b']



# name of x and y axis with font size
plt.xlabel('coding language', fontsize=15)

plt.ylabel('growth rate', fontsize=15)

# make title
plt.title('Race of 2024 in coding language', fontsize=20)


# plt bargraph with width, color center, edge-color and alpha parameter
plt.barh(p, y, color='r', label='popularity')
plt.barh(p1, z, color='b', label='trending')


plt.legend()


plt.show()
