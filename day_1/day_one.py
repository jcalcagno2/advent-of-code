import os

def read_input():
    '''read input file'''

    input_file = open("../day_1/input.txt","r")
    return input_file

def find_answer():
    '''split into left and right arrays'''

    input_file = read_input()
    left_values = []
    right_values = []

    for line in input_file:
        p = line.split()
        left_values.append(int(p[0]))
        right_values.append(int(p[1]))
    
    addition(left_values,right_values) # Call answer method

def addition(array1, array2):
    """Subtract the values of the 2 arrays and return sum of differences"""

    array1.sort()
    array2.sort()
    answer = 0 

    for num in range(len(array1)):
        answer = answer + abs(array1[num] - array2[num]) 
    print(answer)


find_answer()


