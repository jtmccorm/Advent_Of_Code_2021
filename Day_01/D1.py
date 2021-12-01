# AOC_2021
# author: @jtmccorm

def count_increases(int_list):
    num_increases = 0
    for i in range(1, len(int_list)):
        past, present = int_list[i - 1], int_list[i]
        if past < present: num_increases += 1
    return num_increases


if __name__ == '__main__':
    file = open("D1_input.txt")
    depth_readings = [int(line) for line in file]

    # part 1
    print(f"There are {count_increases(depth_readings)} increasing measurements")

    # part 2
    smoothed_readings = [depth_readings[i] + depth_readings[i + 1] + depth_readings[i + 2] for i in
                         range(0, (len(depth_readings) - 2))]
    print(f"After smoothing there are {count_increases(smoothed_readings)} increasing observations")
