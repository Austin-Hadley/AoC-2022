
# read every line from output.txt and compare the lines 2 by 2 and find a common letter
with open("output.txt") as f:
    lines = f.readlines()
    #iterate through every 2 lines checking to see what letter is the same
    for i in range(0, len(lines), 2):
        first = lines[i].strip()
        second = lines[i+1].strip()
        for j in range(len(first)):
            for k in range(len(second)):
                if first[j] == second[k]:
                    print(first[j], end="")
                else:
                    print(" ", end="")