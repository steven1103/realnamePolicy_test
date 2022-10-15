from cmath import cos, sin
import matplotlib.pyplot as plt

x = input('x value')
y = input('y value')
radius = input('radius')
x = int(x)
y = int(y)
radius = int(radius)

x_list = []
y_list = []

for deg in range(0, 360):
    x_list.append(x + radius * cos(deg))
    y_list.append(y + radius * sin(deg))
 
plt.plot(x_list, y_list, color='black')
plt.title('circle graph')
plt.xlabel('+')
plt.ylabel('+')
plt.show()

plt.close()



