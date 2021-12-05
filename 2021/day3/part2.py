# Import Counter
from collections import Counter

# Open input file
with open("input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    
    # Filter the results
    def filter(nums, pos, least=True):
        common = sorted(Counter([num[pos] for num in nums]).most_common(), key = lambda x: (x[1], x[0]), reverse=True)[least][0]
        new_nums = [num for num in nums if num[pos] == common]
        if len(new_nums) == 1:
            return new_nums[0]
        return filter(new_nums, pos + 1, least)

    # Get O2 and CO2
    o2 = int(filter(lines, 0, False), 2)
    co2 = int(filter(lines, 0, True), 2)

    # Print results
    print("Amount of O2: " + str(o2))
    print("Amount of CO2: " + str(co2))
    print("Submarine life support rating: " + str(o2 * co2))