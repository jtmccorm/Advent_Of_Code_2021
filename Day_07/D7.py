# AOC_2021
# author: @jtmccorm
import numpy as np


def loss_1(data, x):
    sum = 0
    for point in data:
        sum += np.abs(x - point)
    return sum


def loss_2(data, x):
    sum = 0
    for point in data:
        dist = np.abs(x - point)
        for i in range(1, int(dist+1)):
            sum += i
    return sum


def gradient_descent(data, x, loss_fxn=loss_1):
    below = loss_fxn(data, x-1)
    value = loss_fxn(data, x)
    above = loss_fxn(data, x+1)
    if below < value < above: return x-1
    if below > value > above: return x+1
    if below > value < above: return x


if __name__ == '__main__':
    data = np.array([int(num) for num in
                            [line.split(',') for line in open("D7_input.txt")][0]])
    # data = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    print("Part 1 - *Unnecessary* Gradient Descent")
    x = np.median(data)
    # Unwittingly, I choose to initialize at the median only to quickly realize that the median
    # is equivalent to the minimum value of an absolute value loss fxn across the range of the data.
    # Still this gave me a head-start for part2!!
    optimum = False
    while not optimum:
        new_x = gradient_descent(data, x)
        if x == new_x:
            optimum = True
        else:
            print(f"Loss={loss_1(data, x)} at x={x}\t-> moving to x={new_x}")
            x = new_x
    print(f"Optimum Found: loss={loss_1(data, x)}, x={x}")

    print("Part 2 - Baller Gradient Descent")
    x = np.median(data)
    optimum = False
    while not optimum:
        new_x = gradient_descent(data, x, loss_2)
        if x == new_x:
            optimum = True
        else:
            print(f"Loss={loss_2(data, x)} at x={x}\t-> moving to x={new_x}")
            x = new_x
    print(f"Optimum Found: loss={loss_2(data, x)}, x={x}")
