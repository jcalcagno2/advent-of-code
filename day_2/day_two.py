def read_input():
    '''read input file'''

    input_file = open("../day_2/input2.txt","r")
    return input_file

def split_into_reports():
    input_data = read_input()  
    list_of_reports = [[int(x) for x in line.split()] for line in input_data] # List comprehension for making list
    return list_of_reports

def check_if_valid(nums):
    diffs = [abs(x1 - x2) for x1, x2 in zip(nums, nums[1:])]
    if not all(1 <= d <= 3 for d in diffs):
        return False
    if all(x1 < x2 for x1, x2 in zip(nums, nums[1:])):
        return True
    if all(x1 > x2 for x1, x2 in zip(nums, nums[1:])):
        return True
    return False

def check_again(nums, part1: bool = True):
    if check_if_valid(nums):
        return True
    if part1:
        return False
    for i in range(len(nums)):
        if check_if_valid(nums[:i] + nums[i + 1 :]):
            return True
    return False



lines = split_into_reports()

part1 = len([r for r in lines if check_if_valid(r)])
print(f"Part 1: {part1}")

part2 = len([r for r in lines if check_again(r, part1=False)])
print(f"Part 2: {part2}")




    
    


