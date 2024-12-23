import re
import sys


def read_input():
    '''read input file'''

    input_file = open("../day_2/input2.txt","r")
    return input_file

# pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
# part1 = sum(prod(map(int, val)) for val in pairs)
data = read_input()
part1 = 0
part2 = 0
enabled = True
for inst in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
    
        if inst == "do()":
            enabled = True
        elif inst == "don't()":
            enabled = False
        else:
            x, y = map(int, inst[4:-1].split(","))
            part1 += x * y
            if enabled:
                part2 += x * y

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
