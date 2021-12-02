# AOC_2021
# author : @jtmccorm

def process_command(location, command):
    direction, magnitude = command[0], int(command[1])
    if len(location) == 2:
        depth, position = location
        if direction == "forward": position += magnitude
        if direction == "down": depth += magnitude
        if direction == "up": depth -= magnitude
        return depth, position
    if len(location) == 3:
        depth, position, aim = location
        if direction == "down": aim += magnitude
        if direction == "up": aim -= magnitude
        if direction == "forward":
            position += magnitude
            depth += magnitude * aim
        return depth, position, aim


if __name__ == '__main__':
    file = open("D2_input.txt")
    commands = [line.rstrip("\n").split(" ") for line in file]

    # Part1
    location = (0, 0)  # (depth, position)
    for command in commands:
        location = process_command(location, command)
    print(f"Part 1: coords = {location} // product = {location[0] * location[1]}")

    # Part2
    location = (0, 0, 0)  # (depth, position, aim)
    for command in commands:
        location = process_command(location, command)
    print(f"Part 2: coords = {location} // product = {location[0] * location[1]}")
