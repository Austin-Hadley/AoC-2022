from pprint import pprint
a = "Rock"
b = "Paper"
c = "Scissors"

x = "Rock"
y = "Paper"
z = "Scissors"

# Read every line of file.txt into a list of lines
# The variable "lines" is a list of strings.
with open("day2.txt") as f:
    lines = f.readlines()

# a/x = tie
# a/y = win
# a/z = lose
# b/x = lose
# b/y = tie
# b/z = win
# c/x = win
# c/y = lose
# c/z = tie

score = 0

def winLoseTie(line):
    global score
    if (line == "A X\n" or line == "B Y\n" or line == "C Z\n"):
        score += 3
    elif (line == "A Y\n" or line == "B Z\n" or line == "C X\n"):
        score += 6
    elif (line == "A Z\n" or line == "B X\n" or line == "C Y\n"):
        score += 0

def choiceScore(line):
    global score
    if (line == "A X\n" or line == "B X\n" or line == "C X\n"):
        score += 1
    elif (line == "B Y\n" or line == "A Y\n" or line == "C Y\n"):
        score += 2
    elif (line == "C Z\n" or line == "B Z\n" or line == "A Z\n"):
        score += 3


for line in lines:
    winLoseTie(line)
    choiceScore(line)
    #pprint(line)
    pprint(score)