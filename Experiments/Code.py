# Algorithm of getting the biggest number from presented numbers
def bignumber(number):
    preresult = []
    result = []
    number = str(number)
    for element in number:
        preresult.append(int(element))
    while len(preresult) != 0:
        max = 0
        for element in preresult:
            if len(preresult) > 1 and element > max:
                max = element
            elif len(preresult) == 1:
                max = preresult[0]
        result.append(max)
        preresult.remove(max)

    return result


print(bignumber(317995))

# Algorithm of binary search (with cycle)
array1 = [3, 5, 8, 10, 12, 15, 18, 20, 20, 50, 60]


def binarysortcycle(array, search):
    left = 0
    right = len(array) - 1
    while (left != right):
        middle = int(left + (right - left) / 2)
        if search == array[middle]:
            return middle
        elif search < array[middle]:
            right = middle - 1
        elif search > array[middle]:
            left = middle + 1


print(binarysortcycle(array1, 20))

# Algorithm of binary search (with recursion)
array2 = [3, 5, 8, 10, 12, 15, 18, 20, 20, 50, 60]


def binarysortrecursion(array, search, left=0, right=len(array)):
    if left == right:
        return -1
    middle = int(left + (right - left) / 2)
    if search == array[middle]:
        return middle
    elif search < array[middle]:
        right = middle - 1
    elif search > array[middle]:
        left = middle + 1
    return binarysortrecursion(array, search, left, right)


print(binarysortrecursion(array2, 60))


