# pure python because I dont anticipate needing other libraries
dict = {
    "A X\n": 4,
    "A Y\n": 8,
    "A Z\n": 3,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 7,
    "C Y\n": 2,
    "C Z\n": 6
}
dict2 ={
    "A X\n": 3,
    "A Y\n": 4,
    "A Z\n": 8,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 2,
    "C Y\n": 6,
    "C Z\n": 7
}
# sometimes a dict is just the best unfortunate answer. 
# I simply don't forsee the amount of matchups in rock paper scissors growing exponentially.
with open('file.txt') as day2:
    total, total2 = 0, 0
    for line in day2:
        total += dict[line]
        total2 += dict2[line]
print(f"Part 1: {total}")
print(f"Part 2: {total2}") #currently wrong, not sure why 