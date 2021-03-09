from statistics import median

def insertion_median(elements):
    medianArr = []
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            # Swap
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
        if i == 1:
            medianArr.append(elements[i])
        else:
            medianArr.append(median(elements[:i+1]))
    return medianArr

if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5]
    print(insertion_median(elements))
    
