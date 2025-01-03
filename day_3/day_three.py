import re

def read_input(file_path):
    """Reads the input file and returns its content as a string."""
    with open(file_path, "r") as input_file:
        return input_file.read()

def process_memory(data):
    """Processes the corrupted memory and calculates the results."""
    part1 = 0  # Sum of all valid mul results
    part2 = 0  # Sum of enabled mul results
    enabled = True

    # Find all valid instructions using regex
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)

    for inst in instructions:
        if inst == "do()":
            enabled = True
        elif inst == "don't()":
            enabled = False
        else:  # Valid mul(X,Y) instruction
            x, y = map(int, inst[4:-1].split(","))
            result = x * y
            part1 += result  # Always add to part1
            if enabled:
                part2 += result  # Add to part2 only if enabled

    return part1, part2

if __name__ == "__main__":
    # Replace with the actual path to your input file
    file_path = "../day_3/input.txt"
    data = read_input(file_path)
    part1, part2 = process_memory(data)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
