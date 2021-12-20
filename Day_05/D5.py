# AOC_2021
# author: @jtmccorm

import numpy as np

class OceanFloor:
    def __init__(self):
        self.surface = np.zeros((1000, 1000), dtype=int)

    def activate_line(self, start, end, diag=False):
        x1, y1 = int(start[0]), int(start[1])
        x2, y2 = int(end[0]), int(end[1])
        if x1 == x2:
            if y1 < y2: self.surface[x1, y1:y2+1] += 1
            elif y2 < y1: self.surface[x1, y2:y1+1] += 1
        elif y1 == y2:
            if x1 < x2: self.surface[x1:x2+1, y1] += 1
            elif x2 < x1: self.surface[x2:x1+1, y1] += 1
        elif diag:
            if x1 < x2 and y1 < y2:
                for x, y in zip(range(x1, x2+1), range(y1, y2+1)):
                    self.surface[x, y] += 1
            elif x1 > x2 and y1 > y2:
                for x, y in zip(range(x1, x2-1, -1), range(y1, y2-1, -1)):
                    self.surface[x, y] += 1
            elif x1 < x2 and y1 > y2:
                for x, y in zip(range(x1, x2+1), range(y1, y2-1, -1)):
                    self.surface[x, y] += 1
            elif x1 > x2 and y1 < y2:
                for x, y in zip(range(x1, x2-1, -1), range(y1, y2+1)):
                    self.surface[x, y] += 1

    def count_doubles(self):
        double_entries = self.surface[np.where(self.surface > 1)]
        return len(double_entries)

    def display(self):
        np.savetxt("output.csv", self.surface, fmt="%d", delimiter=",")


if __name__ == '__main__':
    coord_list = [(x[0].split(","), x[1].split(",")) for x in
              [line.rstrip().split(' -> ') for line in open("D5_input.txt")]]

    # Part 1:
    ocean = OceanFloor()
    for coords in coord_list:
        start_coords, end_coords = coords
        ocean.activate_line(start=start_coords, end=end_coords)
    print(f"Part 1: {ocean.count_doubles()}")

    # Part 2:
    ocean = OceanFloor()
    for coords in coord_list:
        start_coords, end_coords = coords
        ocean.activate_line(start=start_coords, end=end_coords, diag=True)
    ocean.display()
    print(f"Part 2: {ocean.count_doubles()}")
