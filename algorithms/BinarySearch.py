from util import time_it

@time_it
def linear_search(num_list, num_to_find):
    for index, element in enumerate(num_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(num_list, num_to_find):
    left_index = 0
    right_index = len(num_list) - 1
    mid_index = 0
    
    while(left_index <= right_index):
        # Rounded down division
        mid_index = (left_index + right_index) // 2
        mid_num = num_list[mid_index]

        if mid_num < num_to_find:
              left_index = mid_index + 1
        elif mid_num > num_to_find:
            right_index = mid_index - 1
        else:
            return mid_index

    return -1


def binary_search_recursive(num_list, num_to_find, left_index, right_index):
    if left_index > right_index:
        return - 1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_num = num_list[mid_index]

    if mid_num < num_to_find:
        left_index = mid_index + 1
    elif mid_num > num_to_find:
        right_index = mid_index - 1
    else:
        return mid_index

    return binary_search_recursive(num_list, num_to_find, left_index, right_index)


def binary_findAll_occurs(num_list, num_to_find):
    """Find index of all the occurances of a number from sorted list"""
    occurences = []
    index = binary_search(num_list, num_to_find)

    if index == -1:
        return index

    occurences.append(index)
    for x in range(index + 1, len(num_list)):
        if num_list[x] == num_to_find:
            occurences.append(x)
        else:
            break
    for x in range(index - 1, -1, -1):
        if num_list[x] == num_to_find:
            occurences.append(x)
        else:
            break    
        
    return occurences


if __name__ == "__main__":
    numbers_list = [i for i in range(1000001)]
    number_to_find = 1000000

    lindex = linear_search(numbers_list, number_to_find)
    print(f"Number found at {lindex} using linear search")

    bindex = binary_search(numbers_list, number_to_find)
    print(f"Number found at {bindex} using binary search")

    rbindex = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {rbindex} using binary search")

    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15
    print(binary_findAll_occurs(numbers, number_to_find))
