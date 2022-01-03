# question 2.1 - linked list
# question 2.2 - linked list
# question 2.3 - array
# question 2.4 - O(n) time complexity
# question 2.5 - slower


def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


print(find_smallest([50, 30, 10, 80, 20, 5, 99, 1]))
print(find_smallest([-50]))


def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array

print(selection_sort([30, 10, 80, 5, 99, 1, 0]))
