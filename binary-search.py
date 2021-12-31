def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        # mid = (low + high)
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


# question 1.1 - 7
# question 1.2 - 8

# question 1.3 - O(log n)
# question 1.4 - O(n)
# question 1.5 - O(n)
# question 1.6 - O(n)
