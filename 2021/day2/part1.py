# Open input file
with open("input.txt") as f:
    lines = f.readlines()

    # Init variables
    pos = 0
    dep = 0
    nth = 0
    length = len(lines)

    # Iterate through the list
    for i in range(length):
        nth_line = lines[nth].strip()
        for word in nth_line.split():
            if word.isdigit():
                if "forward" in nth_line:
                    pos = pos + int(word)
                elif "up" in nth_line:
                    dep = dep - int(word)
                elif "down" in nth_line:
                    dep = dep + int(word)
        nth = nth + 1

    # Print results
    print("Horizontal position: " + str(pos))
    print("Depth position: " + str(dep))
    print("Horizontal position multiplied by depth: " + str(pos * dep))