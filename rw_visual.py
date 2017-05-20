#coding=utf-8
from random_walk import RandomWalk
import matplotlib.pyplot as plt

#while True:
rm = RandomWalk(50000)
rm.fill_walk()
point_numbers = list(range(rm.num_points))

plt.scatter(rm.x_values, rm.y_values, c=point_numbers, cmap=plt.cm.Blues, s=5, edgecolor='none')


plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rm.x_values[-1], rm.y_values[-1], c='red', edgecolor='none', s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

#	keep_running = raw_input("Make another walk? (y/n): ")
#	if keep_running == 'n':
#		break