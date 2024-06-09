import matplotlib.pyplot as plt
import numpy as np

x = ['Python', 'c++', 'Java', 'javaScript']
y = [85, 50, 75, 80]
z = [55, 44, 48, 52]
c = ['r', 'y', 'g', 'b']

width = 0.2
p = np.arange(len(x))
p1 = [j+width for j in p]

# name of x and y axis with font size
plt.xlabel('coding language', fontsize=15)

plt.ylabel('growth rate', fontsize=15)

# make title
plt.title('Race of 2024 in coding language', fontsize=20)

# plt bargraph with width and color
# plt.bar(x, y, width=0.3, color='g')

# color in every bar
# plt.bar(x, y, width=0.3, color=c)

# plt bargraph with width, color center and edge
# plt.bar(x, y, width=0.3, color=c, align='edge' )
#plt.bar(x, y, width=0.3, color=c, align='center' )

# plt bargraph with width, color center, edge-color and alpha parameter
# plt.bar(x, y, width=0.3, color=c, edgecolor='b', alpha=0.6)

# plt bargraph with width, color center, edge-color and alpha parameter
# plt.bar(x, y, width=0.3, color='r', label='popularity')
# plt.bar(x, z, width=0.3, color='b', label='popularity1')
# plt.legend()

# plt bargraph with width, color center, edge-color and alpha parameter
plt.bar(p, y, width=0.3, color='r', label='popularity')
plt.bar(p1, z, width=0.3, color='b', label='trending')

plt.xticks(p+width/2, x, rotation=20)
plt.legend()


plt.show()
