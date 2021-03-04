def find_sum_iter(n):
    """Iterative approach"""
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def find_sum_rec(n):
    # Base condition
    if n == 1:
        return 1
    return n + find_sum_rec(n - 1)

def make_array(k, n = 0, arr = []):
    if n == k:
        # Base case
        return
    else:
        # Recursive case
        arr.append(n)
        make_array(k, n+1, arr)
    return arr

def listFlatten(inputList):
    for i in inputList:
        if type(i) == int:
            outputList.append(i)
        elif type(i) == list:
            listFlatten(i)
    return outputList



if __name__ == "__main__":
    outputList = []
    print(find_sum_rec(5))
    print(make_array(5))
    print(listFlatten([5,6,[7,8,9], 10, [11,[12]], 13]))
