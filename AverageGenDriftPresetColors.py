import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
from utils import colors, calculate_closeness

closeness = []
time = []

def average_color(color1, color2):
    # Extract RGB components from color1 and color2
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    # Calculate average RGB values
    avg_r = (r1 + r2) // 2
    avg_g = (g1 + g2) // 2
    avg_b = (b1 + b2) // 2

    # Return the average color as a tuple
    return (avg_r, avg_g, avg_b)

class Environment:
    def __init__(self, size:int=256):
        self.size = size
        self.parray = np.zeros((self.size, self.size, 3), dtype=np.uint8)

    def spawn(self):
        for i in range(self.size):
            for j in range(self.size):
                self.parray[i, j] = random.choice(colors)

    def update(self, ii):
        closeness.append(calculate_closeness(self.parray))
        for i in range(self.parray.shape[0]):
            for j in range(self.parray.shape[1]):
                self.parray[i, j] = average_color(self.parray[random.randint(0, self.size-1), random.randint(0, self.size-1)], self.parray[random.randint(0, self.size-1), random.randint(0,self.size-1)])
        #plt.imshow(self.parray)
        #plt.title(ii)

if __name__ == "__main__":
    for i in range(100):
        env = Environment(size=50)
        env.spawn()
        env.update(0)
        t = 1
        while closeness[-1] < .90:
            env.update(t)
            t += 1
        time.append(t)
    print(np.mean(time))