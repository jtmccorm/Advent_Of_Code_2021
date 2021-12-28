# AOC_2021
# author: @jtmccorm

import numpy as np
import matplotlib.pyplot as plt


def fill_basins(map):
    for x in range(np.shape(map)[0]):
        for y in range(np.shape(map)[1]):
            if map[x, y] > 0:
                if y != 99:
                    if map[x, y+1] == 0: map[x, y+1] = map[x, y]
                if y != 0:
                    if map[x, y-1] == 0: map[x, y-1] = map[x, y]
                if x != 99:
                    if map[x+1, y] == 0: map[x+1, y] = map[x, y]
                if x != 0:
                    if map[x-1, y] == 0: map[x-1, y] = map[x, y]
    if 0 in np.unique(map):
        return fill_basins(map)
    else: return map


if __name__ == '__main__':
    height_map = np.array([[int(char) for char in line.rstrip()] for line in open("D9_input.txt")])

    # Part 1 =================================
    low_points = np.zeros_like(height_map)
    for x in range(np.shape(height_map)[0]):
        for y in range(np.shape(height_map)[1]):
            up, down, left, right = True, True, True, True
            if x != 0: left = height_map[x, y] < height_map[x - 1, y]
            if x != 99: right = height_map[x, y] < height_map[x + 1, y]
            if y != 0: up = height_map[x, y] < height_map[x, y - 1]
            if y != 99: down = height_map[x, y] < height_map[x, y + 1]
            if all([up, down, left, right]):
                low_points[x, y] = height_map[x, y] + 1
    print(f"Part 1 - {np.sum(low_points)}")

    # Part 2 =================================
    basin_map = np.zeros_like(height_map)
    low_point_ctr = 0
    for x in range(np.shape(height_map)[0]):
        for y in range(np.shape(height_map)[1]):
            # identify unique low points
            up, down, left, right = True, True, True, True
            if x != 0: left = height_map[x, y] < height_map[x-1, y]
            if x != 99: right = height_map[x, y] < height_map[x+1, y]
            if y != 0: up = height_map[x, y] < height_map[x, y-1]
            if y != 99: down = height_map[x, y] < height_map[x, y+1]
            if all([up, down, left, right]):
                low_point_ctr += 1
                basin_map[x, y] = low_point_ctr
            elif height_map[x, y] == 9:
                basin_map[x, y] = -1

    basin_map = fill_basins(basin_map)  # fill the basins
    basins, size = np.unique(basin_map, return_counts=True)  # count size of basins
    basin_size_ordered = sorted(zip(list(basins), list(size)), key=lambda item: item[1])  # order the counts
    # display and Save
    print("Part 2:")
    print("\t", basin_size_ordered[-2])
    print("\t", basin_size_ordered[-3])
    print("\t", basin_size_ordered[-4])
    print("Total :", basin_size_ordered[-2][1]*basin_size_ordered[-3][1]*basin_size_ordered[-4][1])
    plt.imshow(basin_map, cmap='nipy_spectral')
    plt.savefig("basin.png")