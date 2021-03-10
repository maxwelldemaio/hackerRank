def merge_sort(arr):
    # Check if we hit bottom node
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    
    # Divide arr into 2 parts
    left = arr[:mid]
    right = arr[mid:]

    # Call merge sort on both left and right
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    # Iterate to end of one or the other
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    # Catch rest of elements of longer list
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


if __name__ == "__main__":
    arr = [10,3,15,7,8,23,98,29]
    print(merge_sort(arr))

    # a = [5,8,12,56]
    # b = [7,9,45,51]
    # print(merge_two_sorted_lists(a,b))