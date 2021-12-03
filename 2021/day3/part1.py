with open("input.txt") as f:
    lines = f.readlines()

    nth = 0
    gamma = ""
    epsilon = ""
    length = len(lines)
    
    for i in range(length):
        nth_line = lines[nth]
        char1 = nth_line[0]
        gamma_count = 0
        epsilon_count = 0
        if char1 == "1":
            gamma_count = gamma_count + 1
        elif char1 == "0":
            epsilon_count = epsilon_count + 1
        print(gamma_count)
        print(epsilon_count)
        nth = nth + 1