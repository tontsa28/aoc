# Open input file
with open("input.txt") as f:
    lines = f.readlines()

    # Init variables
    prev1 = -1
    prev2 = 0
    prev3 = 1
    nth1 = -1
    nth2 = 0
    nth3 = 1
    inc = 0
    dec = 0
    length = len(lines) - 2

    # Iterate through the list with a for loop
    for i in range(length):
        prev1 = nth1
        prev2 = nth2
        prev3 = nth3
        nth1 = nth1 + 1
        nth2 = nth2 + 1
        nth3 = nth3 + 1
        prev_sum = int(lines[prev1]) + int(lines[prev2]) + int(lines[prev3])
        nth_sum = int(lines[nth1]) + int(lines[nth2]) + int(lines[nth3])

        if nth_sum > prev_sum:
            inc = inc + 1
        else:
            dec = dec + 1

    # Print increases and decreases
    print("Times increased: " + str(inc))
    print("Times decreased: " + str(dec))