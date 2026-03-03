"""
DSC 20 Winter 2026 Homework 06
Name: Yanhao Wu
PID: A19061338
Source:
"""

#Question 1
def randomize(*args):
    """ 
    takes a series of arguments and returns a
    dictionary where the keys are the data types
     and the values are lists of items, organized
      according to the rules below.

    If the type is a:
    string: keep the characters at the even indices
     of the string, i.e. (0th, 2nd, 4th, 6th index
     and so on…)
    int: if even cast to True, if odd cast to False.
    float: if negative, convert to equivalent
    positive value, if non-negative, change it into
     int by cutting off everything after the decimal.
    list: use its length as a value for a
    corresponding dictionary list.
    Anything else: key is 'garbage', and use unchanged
     arguments as values for a corresponding dictionary list.


    >>> randomize(1, 2.3, False, 'DSC20')
    {'int': [False], 'float': [2], 'garbage': [False], 'str': ['DC0']}
    >>> randomize(True, 4, 'ABC', -9.8, [1,2,3], 'a', False)
    {'garbage': [True, False], 'int': [True], 'str': ['AC', 'a']\
, 'float': [9.8], 'list': [3]}
    >>> randomize(False, True, 'DS', True, 'abc', -3.2, 5, {'a': 1}, -2, ' .')
    {'garbage': [False, True, True, {'a': 1}], 'str': ['D', 'ac', ' ']\
, 'float': [3.2], 'int': [False, True]}
    >>> randomize()
    {}
    >>> randomize(True)
    {'garbage': [True]}

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> randomize('Hello', -5.5)
    {'str': ['Hlo'], 'float': [5.5]}

    >>> randomize([], 100)
    {'list': [0], 'int': [True]}

    >>> randomize({1, 2}, {'key': 'val'})
    {'garbage': [{1, 2}, {'key': 'val'}]}
    """
    divide = 2
    result = {}
    for arg in args:
        if isinstance(arg, bool):
            key = 'garbage'
            value = arg
        elif isinstance(arg, int):
            key = 'int'
            if arg % divide == 0:
                value = True
            else:
                value = False
        elif isinstance(arg, float):
            key = 'float'
            if arg < 0:
                value = -arg
            else:
                value = int(arg)
        elif isinstance(arg, str):
            key = 'str'
            value = arg[::divide]
        elif isinstance(arg, list):
            key = 'list'
            value = len(arg)
        else:
            key = 'garbage'
            value = arg
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

#Question 2
def rearrange_args(*args, **kwargs):
    """
    combines the positional arguments (*args) and
    keyword arguments (**kwargs) into a list of tuples.
     Each tuple in the output should include:
    The type of argument (positional or keyword),
    The position of the argument within *args or **kwargs
     (using 0-based indexing),
    The value held by the argument.


    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> rearrange_args('hi', x=100)
    [('positional_0', 'hi'), ('keyword_0_x', 100)]

    >>> rearrange_args(a=1, b=2, c=3)
    [('keyword_0_a', 1), ('keyword_1_b', 2), ('keyword_2_c', 3)]

    >>> rearrange_args()
    []
    """
    return_lst = []
    for index, arg in enumerate(args):
        return_str1 = f"positional_{index}"
        return_lst.append((return_str1, arg))
    for index, (key, value) in enumerate(kwargs.items()):
        return_str2 = f"keyword_{index}_{key}"
        return_lst.append((return_str2, value))
    return return_lst

#Question 3.1
def count_the_password(lst, password):
    """
    takes a list of strings as the first parameter
     and a string password as the second parameter.

    >>> count_the_password(["cooldragon", "dragon", "gold"], "dragon")
    1
    >>> count_the_password(["DRAGON", "dragon!!"], "dragon")
    0
    >>> count_the_password([], "dragon")
    0
    >>> count_the_password(["dragon "], "dragon")
    0
    >>> count_the_password(["dragon", "likes", "recursions", "right", \
"dragon", "?"], "dragon")
    2

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> count_the_password(["dragon", "dragon", "dragon"], "dragon")
    3
    >>> count_the_password(["dragon", "dragons", "dragon"], "dragon")
    2
    >>> count_the_password(["hello", "world"], "dragon")
    0
    """
    if len(lst) == 0:
        return 0
    if lst[0] == password:
        count = 1
    else:
        count = 0
    return count + count_the_password(lst[1::], password)


#Question 3.2  
def corrupt_password(input, to_insert):
    """
    takes in a single string, a character to_insert
     and returns a corrupted new string where each
     character is followed by a to_insert character.

    >>> corrupt_password('dragon', '#')
    'd#r#a#g#o#n#'
    >>> corrupt_password('', '@')
    ''
    >>> corrupt_password('I can help', '-')
    'I- -c-a-n- -h-e-l-p-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_password("abc", "*")
    'a*b*c*'
    >>> corrupt_password(" ", "#")
    ' #'
    >>> corrupt_password("zzz", "!")
    'z!z!z!'

    """
    if len(input) == 0:
        return ""
    return input[0] + to_insert + corrupt_password(input[1::],
                                                   to_insert)

# Question 3.3
def outsmart_dragon(lst, password, to_insert):
    """
    takes a list of strings, a password to look
    for and an element to insert.

    >>> outsmart_dragon(['dragon'], 'dragon','#')
    ['dragon']
    >>> outsmart_dragon([], 'dragon','@')
    []
    >>> outsmart_dragon(['help me', 'dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'dragon']
    >>> outsmart_dragon(['help me', 'dear dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'd-e-a-r- -d-r-a-g-o-n-']
    >>> outsmart_dragon(['DrAgOn', 'Dragon'], 'dragon','-')
    ['D-r-A-g-O-n-', 'D-r-a-g-o-n-']

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> outsmart_dragon(["dragon", "hi"], "dragon", "*")
    ['dragon', 'h*i*']
    >>> outsmart_dragon(["a", "b", "dragon"], "dragon", "?")
    ['a?', 'b?', 'dragon']
    >>> outsmart_dragon(["no dragons here"], "dragon", "-")
    ['n-o- -d-r-a-g-o-n-s- -h-e-r-e-']
    """
    if len(lst) == 0:
        return []
    if lst[0] == password:
        recur = [lst[0]]
    else:
        recur = [corrupt_password(lst[0], to_insert)]
    return [] + recur + outsmart_dragon(lst[1::], password,
                                        to_insert)

#Question4
def corrupt_with_vowels(input):
    """
    removes vowels from an input string. You can assume
     input is always string. Vowels are the letters
     (a, e, i, o, u) . Not case-sensitive.

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_with_vowels("hello")
    'hll'
    >>> corrupt_with_vowels("AEIOUaeiou")
    ''
    >>> corrupt_with_vowels("why")
    'why'

    """
    if len(input) == 0:
        return ""
    if input[0].lower() in "aeiou":
        char = ""
    else:
        char = input[0]
    return char + corrupt_with_vowels(input[1::])

#Question 5
def where_to_go(point1, point2, separator):
    """
    takes three parameters:
    integers point1 and point2,
    string separator

    then it returns a string with all integers between point1 and
    point2 (both ends are included) separated by a third parameter.
    When point1 < point2, then the numbers in the string are in
     ascending order.
    When point1 > point2, then the numbers in the string are in
     descending order.
    When point1 == point2, just return the string representation
     of the bound itself.


    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> where_to_go(3, 5, '-')
    '3-4-5'
    >>> where_to_go(5, 3, ':')
    '5:4:3'
    >>> where_to_go(0, 0, ',')
    '0'
    """
    if point1 == point2:
        return str(point1)
    if point1 < point2:
        return (str(point1) + separator +
                where_to_go(point1 + 1, point2, separator))
    else:
        return (str(point1) + separator +
                where_to_go(point1 - 1, point2, separator))

