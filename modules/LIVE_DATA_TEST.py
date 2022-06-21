from re import L
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from itertools import count

x_values = []
y_values=[]

index = count()
def displayData():
    
    def animate(i):
        x_values.append(next(index))
        y_values.append(random.randint(-5,5))
        for x in range(len(y_values)):
            print(y_values[x])
        if(len(y_values) >= 10):
            y_values.pop(0)
            x_values.pop(0)

        plt.cla()
        plt.plot(x_values, y_values)


    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.tight_layout()
    plt.show()
    
displayData()