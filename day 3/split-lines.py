# split every line of input.txt into 2 strings of the same length
# and compare them to see if they are the same

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        splitline = line.strip()
        print(splitline)
        # calculate the length of each string and split them into 2 strings
        length = len(splitline)
        half = length // 2
        first = splitline[:half]
        second = splitline[half:]
        with open("output.txt", "a") as f:
            f.write(f"{first}\n{second}\n")