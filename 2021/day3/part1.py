with open("input.txt") as f:
    lines = f.readlines()

    nth = 0
    gamma = ""
    epsilon = ""
    length = len(lines)
    
    for i in range(length):
        nth_line = lines[nth]
        bit = 0
        char = ""
        nthbit = nth_line[bit]
        gamma_count = 0
        epsilon_count = 0
        if nthbit == "1":
            gamma_count = gamma_count + 1
            char += "1"
        elif nthbit == "0":
            epsilon_count = epsilon_count + 1
            char += "0"
        if gamma_count > epsilon_count:
            gamma += char
        else:
            epsilon += char
        char = ""
        nth = nth + 1
        bit = bit + 1

    print(gamma)
    print(epsilon)
    print(gamma_count)
    print(epsilon_count)
    print(bit)
    print(nth)