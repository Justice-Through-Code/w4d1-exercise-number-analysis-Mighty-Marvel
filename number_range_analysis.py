#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    #intialize an accumualtor variable 
    #iterate over a range of numbers
    #add the current to the accumulator
    #return the sum
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.
    acc = 0
    
    for num in range(start, end + 1):
        acc += num
    
    return acc
    
    
def find_smallest_number(start, end):
    #intialize the acummulator variable valued at 100 million
    #iterate over the range of numbers from start to end 
    #when the current number is smaller than than the smallest number the smallest number gets updated
    #the smallest number is returned
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    smallest = int(100000000)

    for small_num in range(start, end + 1):
        if small_num < smallest:
            smallest = small_num
    # TODO: Return the found smallest number.
    return smallest
def find_largest_number(start, end):
    #intialize a variable at zero
    #iterate over the range of numbers from start to end
    #when the current number is larger than the largest number the larger number is updated
    #the largest number is returned
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    largest = int(0)
    
    for large_num in range(start, end + 1):
        if large_num > largest:
            largest = large_num
    
    # TODO: Return the found largest number.
    return largest

def count_even_numbers(start, end):
    #a variable is initialized with a value of zero
    #then the code iterates through the range from start to end determining if the numbers can be evenly divided (leaving no remainder)
    #incresing the value of count by 1
    #then the even numbers are returned
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    count = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            count += 1
            

    # TODO: Return the count of even numbers.
    return count
def count_odd_numbers(start, end):
    #the variable is intialized valued at zero
    #iterate over the range start to end
    #determine if there is a reminder and if so return the numbers
    #increase the count variable by 1 
    #the odd numbers are returned
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    count = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            count += 1
    # TODO: Return the count of odd numbers.
    return count