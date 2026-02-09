"""
DSC 20 Spring 2025 Lab 05
Name: Yanhao Wu
PID: A19061338
"""

# PRE-DEFINED FUNCTIONS
def identity(x):
    return x

def squared(x):
    return x**2

def cubed(x):
    return x**3

def root(x):
    return round(x ** 0.5, 2)

# Question 1
def vector_op(lst, func):
    """
    Applies function to each element in the list
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1, 2, 3]
    >>> vector_op(lst, squared)
    [1, 4, 9]
    >>> lst = [1, 2, 3, 5]
    >>> vector_op(lst, lambda x: -x)
    [-1, -2, -3, -5]
    >>> vector_op(lst, identity)
    [1, 2, 3, 5]
    >>> lst = [10, 20, 30]
    >>> vector_op(lst, cubed)
    [1000, 8000, 27000]
    """
    return [func(i) for i in lst]

# Question 2
def matrix_op(lsts, func):
    """
    Applies function to each element in the 2D list
    --
    Parameters:
        lsts: list of lists of numbers
        func: a function to be applied
    --
    Returns:
        List of lists of transformed numbers

    >>> lsts = [[1,2], [3,4]]
    >>> matrix_op(lsts, squared)
    [[1, 4], [9, 16]]
    >>> lsts = [[10, 20], [30, 40]]
    >>> matrix_op(lsts, lambda x: x / 10)
    [[1.0, 2.0], [3.0, 4.0]]
    >>> lsts = [[5,15], [25,35]]
    >>> matrix_op(lsts, identity)
    [[5, 15], [25, 35]]
    """

    return [[func(j) for j in i] for i in lsts]

# Question 3
def hop_hop(lst, func):
    """
    Applies function to each element in list twice
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_hop(lst, squared)
    [1, 16, 81]
    >>> lst = [5,6,7,8]
    >>> hop_hop(lst, lambda x:x+1)
    [7, 8, 9, 10]
    >>> lst = [10,20,30]
    >>> hop_hop(lst, cubed)
    [1000000000, 512000000000, 19683000000000]
    """
    return [func(func(i)) for i in lst]

# Question 4
def hop_many(lst, func, iterations):
    """
    Applies function to each element in list specified number of times
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
        iterations: number of times to perform operation
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_many(lst, squared, 2)
    [1, 16, 81]
    >>> hop_many(lst, squared, 3)
    [1, 256, 6561]
    >>> hop_many(lst, identity, 100)
    [1, 2, 3]
    >>> hop_many(lst, lambda x: x - 1, 4)
    [-3, -2, -1]
    """
    def iter_func(element):
        for i in range(iterations):
            element = func(element)
        return element
    return [iter_func(i) for i in lst]

# Question 5
def grades_stats(input_lst, choice):
    """
    Calculates mean, median, or both stats for input list. `choice` is 
    1 for median, 2 for mean, and any other for both stats.
    --
    Parameters:
        input_lst: list of integers
        choice: positive integer representing each stat
    --
    Returns:
        Stats of the input list

    >>> lst = [3, 2, 1]
    >>> grades_stats(lst, 1)
    2
    >>> grades_stats(lst, 2)
    2.0
    >>> grades_stats(lst, 0)
    (2, 2.0)
    >>> lst = [1, 2, 4]
    >>> grades_stats(lst, 2)
    2.33
    >>> grades_stats(lst, -1)
    (2, 2.33)
    """
    def find_median(): # Calculate median
        sort_lst = sorted(input_lst)
        if len(sort_lst) % 2 == 0:
            return (sort_lst[int(len(sort_lst)/2)]
                    + sort_lst[int(len(sort_lst)/2)+1])
        else:
            return sort_lst[len(sort_lst)//2]


    def find_mean(): # Calculate mean
        return round(sum(input_lst) / len(input_lst), 2)

    if choice == 1:
        return find_median()
    elif choice == 2:
        return find_mean()
    else:
        return find_median(), find_mean()


# Question 6
def calculate_total_price(base_price, meal_type, meal_time):
    """
    Calculates total price of meal after discounts.
    --
    Parameters:
    base_price: number representing price of meal
    meal_type: string meal type that meal discount is based
    on
    meal_time: string meal time that time discount is based on
    --
    Returns:
    The final price of the meal after applying potential discounts

    >>> calculate_total_price(50, 'vegan', 'breakfast')
    38.25
    >>> calculate_total_price(40, 'meat', 'lunch')
    34.2
    >>> calculate_total_price(25, 'snack', 'dinner')
    25
    """

    def apply_type_discount(meal_type):
        if meal_type == 'vegan':
            return 0.85
        elif meal_type == 'meat':
            return 0.9
        elif meal_type == 'dessert':
            return 0.95
        return 1

    def apply_time_discount(meal_time):
        if meal_time == 'breakfast':
            return 0.90
        elif meal_time == 'lunch':
            return 0.95
        elif meal_time == 'dinner':
            return 1
        return 1

    return round((base_price * apply_type_discount(meal_type)
            * apply_time_discount(meal_time)), 2)

