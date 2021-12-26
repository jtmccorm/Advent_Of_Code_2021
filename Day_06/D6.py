# AOC_2021
# author: @jtmccorm
from collections import Counter

import time

def matriculate(fish_dict):
    num_parent_fish = fish_dict[0]
    fish_dict[0] = fish_dict[1]
    fish_dict[1] = fish_dict[2]
    fish_dict[2] = fish_dict[3]
    fish_dict[3] = fish_dict[4]
    fish_dict[4] = fish_dict[5]
    fish_dict[5] = fish_dict[6]
    fish_dict[6] = fish_dict[7] + num_parent_fish
    fish_dict[7] = fish_dict[8]
    fish_dict[8] = num_parent_fish

if __name__ == '__main__':
    list_of_ages = [int(num) for num in
                      [line.split(',') for line in open("D6_input.txt")][0]]
    age_counter = Counter()
    for age in list_of_ages:
        age_counter[age] += 1

    print("Part 1")
    start = time.time()
    fish_dict = age_counter.copy()
    print(f"Initial State: {fish_dict}, {sum(fish_dict.values())}")
    for i in range(0,80):
        matriculate(fish_dict)
        print(f"Day {i+1:2d}: {fish_dict}, {sum(fish_dict.values())}")
    print(f"Time Elapsed - {time.time()-start}")

    print("Part 2")
    start = time.time()
    fish_dict = age_counter.copy()
    print(f"Initial State: {fish_dict}, {sum(fish_dict.values())}")
    for i in range(0,256):
        matriculate(fish_dict)
        print(f"Day {i+1:2d}: {fish_dict}, {sum(fish_dict.values())}")
    print(f"Time Elapsed - {time.time()-start}")