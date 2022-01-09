# AOC_2021
# author: @jtmccorm

import numpy as np


class DumboOctopusMap:
    def __init__(self, np_map):
        self.energy_map = np_map
        self.epoch = 0
        self.flashes = 0

    def flash(self, x, y):
        self.flashes += 1
        # up_right, up, up_left, right, left, down_right, down_left
        if (x != 0) & (y != 0):  # up_left
            self.energy_map[x-1, y-1] = self.energy_map[x-1, y-1] + 1
            if self.energy_map[x-1, y-1] == 10:
                self.flash(x-1, y-1)
        if x != 0:  # up
            self.energy_map[x-1, y] = self.energy_map[x-1, y] + 1
            if self.energy_map[x-1, y] == 10:
                self.flash(x-1, y)
        if (x != 0) & (y != 9):  # up_right
            self.energy_map[x-1, y+1] = self.energy_map[x-1, y+1] + 1
            if self.energy_map[x-1, y+1] == 10:
                self.flash(x-1, y+1)
        if y != 0:  # left
            self.energy_map[x, y-1] = self.energy_map[x, y-1] + 1
            if self.energy_map[x, y-1] == 10:
                self.flash(x, y-1)
        if y != 9:  # left
            self.energy_map[x, y+1] = self.energy_map[x, y+1] + 1
            if self.energy_map[x, y+1] == 10:
                self.flash(x, y+1)
        if (x != 9) & (y != 0):  # down_left
            self.energy_map[x+1, y-1] = self.energy_map[x+1, y-1] + 1
            if self.energy_map[x+1, y-1] == 10:
                self.flash(x+1, y-1)
        if x != 9:  # down
            self.energy_map[x+1, y] = self.energy_map[x+1, y] + 1
            if self.energy_map[x+1, y] == 10:
                self.flash(x+1, y)
        if (x != 9) & (y != 9):  # down_right
            self.energy_map[x+1, y+1] = self.energy_map[x+1, y+1] + 1
            if self.energy_map[x+1, y+1] == 10:
                self.flash(x+1, y+1)

    def iterate(self):
        # print(self.energy_map)  # Useful for debugging
        for x in range(10):
            for y in range(10):
                self.energy_map[x, y] = self.energy_map[x, y] + 1
                if self.energy_map[x, y] == 10: self.flash(x, y)
        for x in range(10):
            for y in range(10):
                if self.energy_map[x, y] > 9: self.energy_map[x, y] = 0
        self.epoch += 1

    def check_synch(self):
        if np.sum(self.energy_map) == 0: return True

if __name__ == '__main__':
    # Part 1 ===============================
    Octopus_Garden = DumboOctopusMap(np.array([[int(char) for char in line.rstrip()] for line in open("D11_input.txt")]))
    for i in range(100):
        Octopus_Garden.iterate()
    print("Part 1")
    print(f"\tFlashed = {Octopus_Garden.flashes}")
    # Part 2 ===============================
    while not Octopus_Garden.check_synch():
        Octopus_Garden.iterate()
    print("Part 2")
    print(f"\tSynchronized at Epoch={Octopus_Garden.epoch}")