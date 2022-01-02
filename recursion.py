# pseudo code


def look_for_key_while(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('found a key!')


def look_for_key_recursion(box):
    for item in box:
        if item.is_a_box():
            look_for_key_recursion(item)
        elif item.is_a_key():
            print('found the key!')


def find_integer(array):
    for item in array:
        array = array[1:]
        if isinstance(item, int):
            return f'got int {item}'
        else:
            print(item)
            return find_integer(array)

print(find_integer(['a', 'b', 2, 'c', 'd']))



def countdown(number):
    print(number)
    if number <= 0:
        return
    return countdown(number - 1)

countdown(5)


# question 3.1 - current program status - greet function is suspended and greet2 function is working


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


# question 3.2 - infinetly growing stack untill stack overflow error