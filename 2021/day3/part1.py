# Import Counter
from collections import Counter

# Open input file
with open("input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

    # Calculate gamma and epsilon
    gamma = int("".join([Counter(x).most_common(1)[0][0] for x in list(zip(*lines))]), 2)
    epsilon = int(len(lines[0])*"1", 2) - gamma

    # Print results
    print("Gamma: " + str(gamma))
    print("Epsilon: " + str(epsilon))
    print("Submarine power consumption: " + str(gamma * epsilon))