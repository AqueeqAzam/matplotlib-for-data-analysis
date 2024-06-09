import matplotlib.pyplot as plt
import numpy as np

share = [85, 50, 75, 80, 34, 67, 65]
price = [55, 44, 48, 52, 43, 89, 66]
colors = [10, 49, 30, 29, 56]

plt.title('Scatter plot', fontsize=20)
plt.xlabel('share', fontsize=15, c='b')
plt.ylabel('price', fontsize=15, c='b')
plt.scatter(share, price, c='r', marker='*', cmap='viridis')
plt.colorbar()
plt.show()
