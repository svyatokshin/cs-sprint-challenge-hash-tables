# have up to ten lists within a list
# trying to figure out which items are present in all of the lists
# lists can have up to 1,000,000 items

def intersection(arrays):
    cache = {}  # store the elements of all the arrays
    list1 = []  # will be container to hold repeated items
    length = 0  # to keep track of number of arrays in input

    for num in arrays:  # num will refer to each specific list within arrays
        length += 1    # add 1 to our length to keep track of amount of lists
        for i in num:  # i will refer to each elem in specified list
            if i not in cache:
                cache[i] = 1  # add elem if not in cache
            else:
                cache[i] += 1  # if not we increment by 1

    for key in cache:
        if cache[key] >= length:  # if the value of the key is greater then the number of lists given
            list1.append(key)  # append to the result list

    return list1


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
