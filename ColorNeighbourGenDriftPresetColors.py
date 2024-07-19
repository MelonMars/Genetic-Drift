import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
from utils import colors, calculate_closeness

closeness, time = [], []

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
                neighbors = [
                    self.parray[max(0, i-1), max(0, j-1)],
                    self.parray[max(0, i), max(0, j-1)],
                    self.parray[min(i+1, self.parray.shape[0]-1), max(0, j-1)],
                    self.parray[max(0, i-1), max(0, j)],
                    self.parray[i, j],
                    self.parray[min(i+1, self.parray.shape[0]-1), max(0, j)],
                    self.parray[max(0, i-1), min(j+1, self.parray.shape[1]-1)],
                    self.parray[max(0, i), min(j+1, self.parray.shape[1]-1)],
                    self.parray[min(i+1, self.parray.shape[0]-1), min(j+1, self.parray.shape[1]-1)]
                ]
                self.parray[i, j] = random.choice(neighbors)

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