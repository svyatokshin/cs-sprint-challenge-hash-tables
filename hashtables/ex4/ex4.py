# Given a list of integers both positive and negative
# Want to figure out what positive numbers have corresponding negative numbers in the same list

def has_negatives(a):
    cache = {}
    list1 = []
    # convert all numbers in list to positive ones using abs()
    a = [abs(i) for i in a]

    for i in a:
        if i not in cache:
            cache[i] = 1  # if not in cache we set equal to 1

        else:
            cache[i] += 1  # if in cache already we add 1

    for key in cache:
        if cache[key] == 2:  # if theres 2 for a specific key, we append to list and return
            list1.append(key)

    return list1


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
