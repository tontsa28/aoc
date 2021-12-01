# Open input file
with open("input.txt") as f:
    lines = f.readlines()

    # Init variables
    prev = 0
    nth = 0
    inc = 0
    dec = 0
    length = len(lines) - 1
    
    # Iterate through the list with a for loop
    for i in range(length):
        prev = nth
        nth = nth + 1
        prev_line = int(lines[prev])
        nth_line = int(lines[nth])

        if nth_line > prev_line:
            inc = inc + 1
        else:
            dec = dec + 1

    # Print increases and decreases
    print("Times increased: " + str(inc))
    print("Times decreased: " + str(dec))