# AOC_2021
# author: @jtmccorm

def getGammaEpsilon(nums):
    # Nothing like incomprehensible comprehensions
    sums = [sum([int(num[bit_idx]) for num in nums]) for bit_idx in range(len(nums[0]))]
    gamma = "".join([str(int(sum >= len(nums) / 2)) for sum in sums])
    epsilon = "".join([str(int(sum < len(nums) / 2)) for sum in sums])
    return gamma, epsilon


def mostCommonBit(nums, bit_idx):
    return str(int(sum([int(num[bit_idx]) for num in nums]) >= len(nums) / 2))


def RatingSearch(candidates, bit_idx, min=False):
    search_bit = mostCommonBit(candidates, bit_idx)
    if min: search_bit = str(int(not bool(int(search_bit))))
    candidates = [n for n in candidates if n[bit_idx] == search_bit]
    if len(candidates) == 1:
        return candidates[0]
    else:
        return RatingSearch(candidates, bit_idx+1, min)


if __name__ == '__main__':
    nums = [line.rstrip("\n") for line in open("D3_input.txt")]

    # Part 1
    gamma, epsilon = getGammaEpsilon(nums)
    print(f"Part 1 : Gamma = {int(gamma, 2)}, Epsilon = {int(epsilon, 2)}, product = {int(gamma, 2) * int(epsilon, 2)}")

    # Part 2
    oxygen = RatingSearch(nums, 0, False)
    co2 = RatingSearch(nums, 0, True)
    print(f"Part 2 : oxygen = {int(oxygen,2)}, co2 = {int(co2, 2)}, product = {int(oxygen,2) * int(co2,2)}")
