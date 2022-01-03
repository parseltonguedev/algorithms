# question 4.1
def summarize_array(array):
    if not array:
        return 0
    else:
        return array[0] + summarize_array(array[1:])


print(summarize_array([2, 4, 6]))


# question 4.2
def get_len_recursive(array):
    if not array:
        return 0
    else:
        return 1 + get_len_recursive(array[1:])


print(get_len_recursive([1, 2, 3, 9]))


# question 4.3
def get_max_recursive(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = get_max_recursive(array[1:])
    return array[0] if array[0] > sub_max else sub_max


print(get_max_recursive([2, 7, 54, 3, 27]))


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([6, 2, 5, 3, 13, 65, 235, 34, 0, -1]))

# question 4.4 - base - array == 0 or 1, recursive > 1
# question 4.5 - O(n)
# question 4.6 - O(n)
# question 4.7 - O(1)
# question 4.8 - O(n!)
