# Given a list of item's weights, length of list and limit
# Want to figure out if the sum of the 2 item's weight is equal to the limit number

# create hash table
# store as keys the weights of the items if they are not already there

def get_indices_of_item_weights(weights, length, limit):
    cache = {}  # the cache will hold the weights as keys and the indexes in the list of weights as values
    # values will need to be returned cache is great for this
    list1 = []

    if length <= 1:
        return None

    if length == 2:
        if (weights[0] + weights[1]) == limit:  # if their sum is equal to the limit
            # return a tuple with the highest index as the first element
            return (1, 0)

    for idx in range(length):  # iterate through the list of weights
        if weights[idx] not in cache:
            # if the elem in the idx isnt in cache we will put it in there
            cache[weights[idx]] = idx

    for key in cache:  # iterate through keys in cache
        result = limit - key  # the result that I want to know would be the other number that when added to this key is equal to the limit
        if result in cache:  # if other number is in cache
            list1.append(cache[result])  # append it to my list

    return tuple(list1)  # convert list to tuple
