"""
Input: List of numbers such as wafer yields
Output: Lot avg of wafer yield

"""
list_num = [17, 42, 9, 56, 23, 88, 4, 37, 61, 12, 
28, 53, 76, 8, 33, 69, 5, 91, 20, 49, 
14, 72, 31, 64, 11]

def sum(list_num):
    total = 0
    for i in list_num:
        total += i
    return total

  
def count(list_num):
    count = 0
    for i in list_num:
        count += 1
    return count


def average(list_num):
    average_list = sum(list_num) / count(list_num)
    return average_list



