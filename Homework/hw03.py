"""
DSC 20 Winter 2026 Homework 03
Name: Yanhao Wu
PID: A19061338
Source:
"""


# Question 1.1
def operate_nums(lst):
    """
    takes a list of integers and returns a new list that
    double the value of odd integers and triples the
    value of even integers.

    >>> operate_nums([1, 2, 3, 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3.1, -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]

    # Add at least 3 doctests below here #
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]

    >>> operate_nums(3)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> operate_nums([[1, 2, 3]])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> operate_nums([1])
    [2]

    """
    assert isinstance(lst, list)
    assert all([isinstance(i, int) for i in lst])
    mutiplier = 3
    doub = 2
    return [i * mutiplier if i % doub == 0 else i * doub for i in lst]

# Question 1.2
def string_lengths(text, nums):
    """
     takes a list of non-empty strings and a list
      of positive integers of the same length and
      returns a list of boolean values, where True
       indicates that the length of the string is
        strictly greater than the corresponding
        integer in the second list, and False otherwise.


    >>> string_lengths(['a', 'b', 'c'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', 'abc'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['a', 'b'], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5])
    [True, False, False]

    # Add at least 3 doctests below here #
    >>> string_lengths(2, 1)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> string_lengths(['abc', 'abcd', 'abcde'], ['D', 5, 5])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> string_lengths(['abc', 'abcd'], ['D', 5, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert all([isinstance(text, list), isinstance(nums, list)])
    assert len(text) == len(nums)
    assert all(isinstance(i, int) for i in nums)
    assert all(len(i) != 0 for i in text)
    assert all(i >= 0 for i in nums)
    return [len(text[i]) > nums[i] for i in range(len(text))]

# Question 1.3
def process_dict(input_dict):
    """
    take a dictionary that the keys are tuples
    and the values are lists of string, calculating the
    sum of the length of tuple and length of each strings
    in list.
    
    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2,): \
    ['b']})
    [15, 2]

    # Add at least 3 doctests below here #
    >>> process_dict(1)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> process_dict({(1, 'd'): ['a', 'b'], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError

    >>> process_dict({'i': ['a', 'd'], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(input_dict, dict)
    assert all(isinstance(i, tuple) for i in input_dict)
    assert all(isinstance(i, list) for i in input_dict.values())
    assert all(isinstance(j, int) for i in input_dict for j in i)
    assert all(isinstance(j, str) for i in input_dict.values() for j in i)
    leng_tup = [len(i) for i in input_dict]
    length = [sum([len(j) for j in i]) for i in input_dict.values()]
    return [leng_tup[i] + length[i] for i in range(len(leng_tup))]

# Question 2
def unusual_sort(indices, items):
    """
    take the indices value, corresponding sorted values
    of items by sorted indices, and sorted indices, makes
    them a tuple.

    >>> unusual_sort([0, 4, 2, 3, 1], \
        ["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 1, 4)]

    >>> unusual_sort([0.0, 4.0, 2.0, 3.0, 1.0], \
    ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    >>> unusual_sort([0, 4, 2, 3, 1], \
        [4, "four", True, {'one':'two'}, "one"])
    [(4, 0, 0), ('one', 4, 1), (True, 2, 2), \
({'one': 'two'}, 3, 3), ('four', 1, 4)]

    >>> unusual_sort([1, 2], \
    ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort(1, 1)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert all([isinstance(indices, list), isinstance(items, list)])
    assert len(indices) == len(items)
    assert all([isinstance(i, int) for i in indices])
    sorted_lst = sorted(indices)
    assert sorted_lst == [i for i in range(len(indices))]
    corr_dic = {indices[i]: items[i] for i in range(len(indices))}
    return [(corr_dic[sorted_lst[i]], indices[i], sorted_lst[i])
            for i in range(len(indices))]

# Question 3
def change_input(strange_list):
    """
    replace the lowercase vowels to uppercase,
    double the integer, and remain the others.

    >>> change_input(["3.14IS PIE", "11My aGe iS"])
    ['6.28IS PIE', '22My AGE IS']
    >>> change_input(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO t12O slEEp At ', '10I lIkE tO stArt wOrk bEfOrE ']
    >>> change_input("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    >>> change_input([1])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input(92992)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input(["asdfa34", ["asldoijf"]])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(strange_list, list)
    assert all([isinstance(i, str) for i in strange_list])
    doub = 2
    return ["".join([str(int(j) * doub) if j.isdigit() else
                     j.upper() if j.islower() and j in "aeiou" else
                     j for j in i]) for i in strange_list]

# Question 4
def change_input_even_more(strange_list):
    """
    replace the lowercase vowels to uppercase,
    double the integer and move them to the end
    of the string, and remain the others.
    >>> change_input_even_more(["3.14IS PIE", "11My aGe iS"])
    ['.IS PIE628', 'My AGE IS22']
    >>> change_input_even_more(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    >>> change_input_even_more([1])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input_even_more(92992)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input_even_more(["asdfa34", ["asldoijf"]])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(strange_list, list)
    assert all([isinstance(i, str) for i in strange_list])
    doub = 2
    return ["".join([ch.upper() if ch in "aeiou" else ch for
                     ch in s if not ch.isdigit()])+
            "".join([str(int(ch) * doub)
            for ch in s if
            ch.isdigit()])for
            s in strange_list]

# Question 5.1
def cheapest_gas(gas_stations, mileage):
    """
    find the cheapest gas station in the available range.

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'

    # Add at least 3 doctests below here #
    >>> cheapest_gas(gas_stations, 70)
    'Shell'

    >>> cheapest_gas(gas_stations, 80)
    'Shell'

    >>> cheapest_gas(gas_stations, 50)
    'Shell'
    """
    within_range = {i[1]: brand for brand, value in
                    gas_stations.items() for i in value
                    if i[0] <= mileage}
    return within_range[min(within_range.keys())]


# Question 5.2
def cheapest_average_gas(gas_stations, mileage):
    """
    find the average cheapest gas station in the available range.

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.1), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 20)
    'Shell'

    # Add at least 3 doctests below here #
    >>> cheapest_average_gas(gas_stations, 70)
    'Arco'

    >>> cheapest_average_gas(gas_stations, 80)
    'Arco'

    >>> cheapest_average_gas(gas_stations, 50)
    'Arco'
    """
    within_range = {i[1]: brand for brand, value in
                    gas_stations.items() for i in value
                    if i[0] <= mileage}
    dic_templ = {i: [] for i in within_range.values()}
    [dic_templ[brand].append(price) for price, brand in within_range.items()]
    mean = {sum(price) / len(price) : brand
            for brand, price in dic_templ.items()}
    return mean[min(mean.keys())]



# Question 6
def new_orders(orders, action, dish_name, amount):
    """
    depending on the action and the dish name,
    updating the orders by minusing or adding the
    amount to original price. If price is lower than
    0, then set it to 0

    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'add', 'pizza', 5)
    {'pizza': 15, 'burger': 5}

    >>> new_orders(orders, 'remove', 'burger', 3)
    {'pizza': 10, 'burger': 2}

    >>> new_orders(orders, 'remove', 'pizza', 15)
    {'pizza': 0, 'burger': 5}

    >>> new_orders([], 'remove', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    >>> new_orders(orders, 'a', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> new_orders(orders, 'remove', 'burger', 100)
    {'pizza': 10, 'burger': 0}

    >>> new_orders(orders, 'remove', 'burger', -3)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert all([isinstance(orders, dict), isinstance(action, str),
            isinstance(dish_name, str), isinstance(amount, int)])
    assert [isinstance(i, str) for i in orders.keys()]
    assert [isinstance(i, int) for i in orders.values()]
    assert amount >= 0
    assert action in ["add", "remove"]
    return {dish: price + amount if action == 'add' and dish_name == dish
                else 0 if action == 'remove' and dish_name == dish and
                          price - amount < 0 else price - amount if
    action == 'remove' and dish_name == dish else price
                for dish, price in orders.items()}
