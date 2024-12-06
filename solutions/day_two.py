def read_input():
    '''read input file'''

    input_file = open("../inputs/input2.txt","r")
    return input_file

def split_into_reports():
    input_data = read_input()  
    list_of_reports = [[int(x) for x in line.split()] for line in input_data] # List comprehension for making list
    return list_of_reports

def check_if_valid(array):
    
    if array != sorted(array) and array != sorted(array, reverse=True):
        print("Not sorted")
        return False
    
    for i in range(len(array) - 1):
        if abs(array[i] - array[i + 1]) > 3 or abs(array[i] - array[i + 1]) == 0:
            return False
        
    return True

def part_one_solution():
    answer = 0
    array = split_into_reports()
    for x in array:
        if check_if_valid(x) == True:
            answer = answer + 1
    
    print(answer)
    return answer
       
    
part_one_solution()


    
    


