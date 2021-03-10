def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    frequency = {}
    newArr = []

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                # Swap
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

    for x in range(len(arr)):
        if arr[x] not in frequency:
            newArr.append(arr[x])
            frequency[arr[x]] = 1            
    return newArr


if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    print(shell_sort(elements))
