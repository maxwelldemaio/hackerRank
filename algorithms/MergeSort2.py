def merge_sort(arr, key, descending=False):
    # Check if we hit bottom node
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    # Divide arr into 2 parts
    left = arr[:mid]
    right = arr[mid:]

    # Call merge sort on both left and right
    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge_two_sorted_lists(left, right, arr, key, descending)


def merge_two_sorted_lists(a, b, arr, key, descending=False):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    # Iterate to end of one or the other
    if descending:
        while i < len_a and j < len_b:
            if a[i][key] >= b[j][key]:
                arr[k][key] = a[i][key]
                i += 1
            else:
                arr[k][key] = b[j][key]
                j += 1
            k += 1
    else:
        while i < len_a and j < len_b:
            if a[i][key] <= b[j][key]:
                arr[k][key] = a[i][key]
                i += 1
            else:
                arr[k][key] = b[j][key]
                j += 1
            k += 1

    # Catch rest of elements of longer list
    while i < len_a:
        arr[k][key] = a[i][key]
        i += 1
        k += 1
    while j < len_b:
        arr[k][key] = b[j][key]
        j += 1
        k += 1


if __name__ == "__main__":
    elements = [
        {'name': 'vedanth',   'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12,  'time_hours': 3},
        {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        {'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    merge_sort(elements, key='name', descending=True)
    print(elements)
