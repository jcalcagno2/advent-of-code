from collections import defaultdict

def read_input(file_path):
    """Reads the input file and returns its content as a string."""
    with open(file_path, "r") as f:
        lines = list(map(str.strip, f.readlines()))
        return lines


def search():
    lines = read_input("../day_4/input.txt")
    
    
    char_map = defaultdict(set)
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            char_map[val].add((r, c))

    part1 = 0
    for r, c in char_map["X"]:
        for dr, dc in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            for i, char in enumerate("MAS", 1):
                if (r + (dr * i), c + (dc * i)) not in char_map[char]:
                    break
            else:
                part1 += 1
    print(f"Part 1: {part1}")

    return part1

print(search())

            
print(search())
    

        


