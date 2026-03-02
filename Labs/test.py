# Question 1
def complexity():
    '''
    Returns the time complexity of the four functions

    returns:
      list: list of answers to the 4 complexity questions

    >>> isinstance(complexity(), list)
    True
    >>> all([isinstance(el, int) for el in complexity()])
    True
    >>> len(complexity()) == 4
    True
    '''
    # YOUR ANSWER GOES HERE
    return [5, 4, 2, 6]


# Question 2
def add_greeting(*names, greeting="Hello"):
    '''
    Function that adds a greeting to each person's 
    name, or "Hello" if no greeting was provided.

    args:
        *names (strings): variable number of names
        greeting (string, optional): greeting to precede each 
            name, default is "Hello"
    returns:
        list: list of strings with greeting added to each name

    >>> add_greeting("Mike")
    ['Hello Mike']
    >>> add_greeting("John", "Jane", "Joe")
    ['Hello John', 'Hello Jane', 'Hello Joe']
    >>> add_greeting("Jack", "John", "Jeff", greeting="Hi")
    ['Hi Jack', 'Hi John', 'Hi Jeff']
    '''
    return [greeting + " " + name for name in names]


# Question 3
def approve(score_threshold, **students):
    '''
    Function that approves students if their score is at least
    score_threshold.

    args:
        score_threshold (int): minimum required score
        **students: names and scores
            key: student's name
            value (int): student's score
    returns:
        list of strings representing who is approved

    >>> approve(80, Mike=75, Jane=85, John=90)
    ['Jane is approved', 'John is approved']
    >>> approve(60, Amy=60, Bob=70, Carl=55)
    ['Amy is approved', 'Bob is approved']
    '''
    return [name + " is approved" for name, num in students.items() if num >= score_threshold]


# Question 4
def sum_negative(lst):
    '''
    Recursively computes the sum of negative numbers in a list.

    args:
        lst (list of int): list of integers
    returns:
        int: sum of negative integers in lst

    >>> sum_negative([1, -2, 3, -4])
    -6
    >>> sum_negative([])
    0
    '''
    if len(lst) == 0:
        return 0
    if lst[0] < 0:
        return lst[0] + sum_negative(lst[1:])
    else:
        return sum_negative(lst[1:])

# Question 5
def filter_string_dict(lst):
    """
    Takes a list of (key, value) tuples and returns a 
    dictionary containing only the pairs where value is a string.

    >>> data = [("a", 1), ("b", "hello"), ("c", 3), ("d", "world")]
    >>> filter_string_dict(data)
    {'b': 'hello', 'd': 'world'}
    >>> data2 = [("id", "A1"), ("status", 200), ("type", "admin")]
    >>> filter_string_dict(data2)
    {'id': 'A1', 'type': 'admin'}
    """
    if len(lst) == 0:
        return {}
    if isinstance(lst[0][1], str):
        return {lst[0][0]: lst[0][1]}.update(filter_string_dict(lst[1:]))
