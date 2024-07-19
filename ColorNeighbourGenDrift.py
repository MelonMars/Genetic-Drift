import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random



class Environment:
    def __init__(self, size:int=256):
        self.size = size
        self.parray = np.zeros((self.size, self.size, 3), dtype=np.uint8)

    def spawn(self):
        for i in range(self.size):
            for j in range(self.size):
                self.parray[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        print(self.parray)

    def update(self, ii):
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
        plt.imshow(self.parray)
        plt.title(ii)

if __name__ == "__main__":
    env = Environment(50)
    env.spawn()
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, env.update, interval=0.0001)
    plt.show()