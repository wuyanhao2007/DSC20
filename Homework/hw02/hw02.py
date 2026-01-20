"""
DSC 20 Winter 2026 Homework 02
Name: Yanhao Wu
PID: A19061338
Source:
"""

# Question 1
def name_mapping(given_names, preferred_names):
    """
    Make the given name and corresponding preferred name
    a tuple and return the list of all given name and
    perferred name combination. If no given name is
    provided, return NO NAME PROVIDED instead.


    >>> given_names = ['Amanda', 'Jeffrey', 'Richard']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('Richard', 'Rick')]

    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Mandy'), ('NO NAME PROVIDED', 'Jeff'), \
('NO NAME PROVIDED', 'Rick')]

    # Add at least 3 doctests below here #
    >>> given_names = ['Amanda']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('NO NAME PROVIDED', 'Jeff'), \
('NO NAME PROVIDED', 'Rick')]
    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = ['Mandy', 'Jeff']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff')]
    >>> given_names = ['Amanda', 'Jeffrey', 'a']
    >>> preferred_names = ['Mandy', 'Jeff', 'a']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('a', 'a')]
    """
    tuple_names = []
    for i in range(len(preferred_names) - len(given_names)):
        given_names.append('NO NAME PROVIDED')
    for index, name in enumerate(given_names):
        tuple_names.append((name, preferred_names[index]))
    return tuple_names


# Question 2
def valid_pairs(keys, values):
    """
    If the keys is valid as a dictionary key, return a tuple
    of key and its corresponding values. If it is not valid,
    return the tuple of the key is 'not valid' and no value.

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    # Add at least 3 doctests below here #
    >>> keys = [[], ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('not valid',), ('not valid',)]

    >>> keys = [[], {}]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('not valid',), ('not valid',)]

    >>> keys = ["fun", 'not']
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not', 6)]
    """
    tuple_name = []
    for i,j in enumerate(keys):
        if type(j) == dict or type(j) == list:
            tuple_name.append(('not valid', ))
        else:
            tuple_name.append((j, values[i]))
    return tuple_name


# Question 3
def dict_of_names(name_tuples):
    """
    take a list of a tuples and return a dictionary
    that of names and corresponding perferred names.
    If the name is not provided, make a tuple which key
    is not provided.

    >>> dict_of_names([('Richard', 'Rick'),
    ... ('Roxanne', 'Rose'), ('Roxanne', 'Ann'),
    ... ('Richard', 'Ricky'), ('Roxanne', 'Roxie'),
    ... ('Mitchell', 'Mitch')])
    {'Richard': ['Rick', 'Ricky'], 'Roxanne': ['Rose', 'Ann', 'Roxie'], \
'Mitchell': ['Mitch']}

    >>> dict_of_names([('Melissa', 'Lisa'),
    ... ('Isabel', 'Bella'), ('NO NAME PROVIDED', 'Faith')])
    {'Melissa': ['Lisa'], 'Isabel': ['Bella'], \
'NO NAME PROVIDED': ['Faith']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick'), \
    ('NO NAME PROVIDED', 'Jacob')])
    {'NO NAME PROVIDED': ['Derrick', 'Jacob']}

    # Add at least 3 doctests below here #
    >>> dict_of_names([])
    {}
    >>> dict_of_names([('Richard', 'Rick')])
    {'Richard': ['Rick']}
    >>> dict_of_names([('Richard', 'Rick'),
    ... ('Roxanne', 'Rose')])
    {'Richard': ['Rick'], 'Roxanne': ['Rose']}
    """
    dict_name = {}
    for i,j in name_tuples:
        if i in dict_name:
            dict_name[i].append(j)
        else:
            dict_name[i] = [j]
    return dict_name


# Question 4.1
def contractor_payment(suggestions):
    """
    takes a list of lists, where each inner list follows the format
     above, and returns a dictionary where the keys are contractor
    labels and the values are theaverage payment for each contractor

    >>> contractor_payment([[10, 20, 30], [0, 20, 10]])
    {'1': 5.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([[10, 20, 30], [30, 20, 10], [5, 10, 15]])
    {'1': 15.0, '2': 16.67, '3': 18.33}

    >>> contractor_payment([[-5, -10, -4], [-20, 15, 40]])
    {'1': -12.5, '2': 2.5, '3': 18.0}

    # Add at least 3 doctests below here #
    >>> contractor_payment([])
    {'1': 0.0, '2': 0.0, '3': 0.0}

    >>> contractor_payment([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    {'1': 0.0, '2': 0.0, '3': 0.0}

    >>> contractor_payment([[0, 20, 30], [0, 20, 10]])
    {'1': 0.0, '2': 20.0, '3': 20.0}
    """
    contractor_dict = {'1': 0.0, '2': 0.0, '3': 0.0}
    round_num = 2
    index = 2
    for i in suggestions:
        contractor_dict['1'] += round(i[0]/len(suggestions), round_num)
        contractor_dict['2'] += round(i[1]/len(suggestions), round_num)
        contractor_dict['3'] += round(i[index]/len(suggestions), round_num)
    return contractor_dict

# Question 4.2
def new_pay(hours):
    """
    give the contractor bonus. The formula of bonus is
    bonus_pay = (
      0.01 * hours worked by contractor 1 +
      0.015 * hours worked by contractor 2 +
      min(0.02 * abs(100 - hours worked by contractor 3), 0.025 *
      hours worked by contractor 3) - 5
    If any contractor works less than expected, the bonus will
    turns to penalty, which is -10 in bonus.
    Return the amount of bonus of penalty, and add the donus
    in the dictionary.

    >>> case1 = {'1': 200, '2': 138, '3': 172}
    >>> round(new_pay(case1), 2)
    0.51
    >>> case1
    {'1': 200, '2': 138, '3': 172, 'pay': 'Bonus'}

    >>> case2 = {'1': 130, '2': 84, '3': -14}
    >>> new_pay(case2)
    -10
    >>> case2
    {'1': 130, '2': 84, '3': -14, 'pay': 'Penalty'}

    >>> case3 = {'1': 42, '2': 96, '3': 63}
    >>> round(new_pay(case3), 1)
    -2.4
    >>> case3
    {'1': 42, '2': 96, '3': 63, 'pay': 'Penalty'}

    # Add at least 3 doctests below here #
    >>> case1 = {'1': 0, '2': 0, '3': 0}
    >>> round(new_pay(case1), 2)
    -5.0
    >>> case1
    {'1': 0, '2': 0, '3': 0, 'pay': 'Penalty'}

    >>> case1 = {'1': -1, '2': -1, '3': -1}
    >>> round(new_pay(case1), 2)
    -10
    >>> case1
    {'1': -1, '2': -1, '3': -1, 'pay': 'Penalty'}

    >>> case1 = {'1': 0, '2': 138, '3': 172}
    >>> round(new_pay(case1), 2)
    -1.49
    >>> case1
    {'1': 0, '2': 138, '3': 172, 'pay': 'Penalty'}
    """
    penalty = -10
    bonus = (0.01 * hours['1'] + 0.015 * hours['2'] +
             min(0.02 * abs(100 - hours['3']), 0.025 * hours['3']) - 5)
    for i in hours.values():
        if i < 0:
            bonus = penalty
    if bonus >= 0:
        hours['pay'] = 'Bonus'
    else:
        hours['pay'] = 'Penalty'
    return bonus

# Question 5
def potential_ideas_for_business(items):
    """
    Take the unique items from each supplier and sort
    those unique items in a list and return it.

    >>> items = {'supplier 1': ['Tea', 'Peaches'], \
    'supplier 2': ['Peaches', 'Apples', 'Cups']}
    >>> potential_ideas_for_business(items)
    ['Apples', 'Cups', 'Peaches', 'Tea']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 2': ['Milk', 'Eggs', 'Vanilla', 'Butter'], \
    'supplier 3': ['Butter', 'Sugar']}
    >>> potential_ideas_for_business(items)
    ['Butter', 'Chocolate', 'Eggs', 'Flour', 'Milk', 'Sugar', 'Vanilla']

    >>> items = {'supplier 1': [], 'supplier 2': []}
    >>> potential_ideas_for_business(items)
    []

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 2': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 3': ['Flour', 'Eggs', 'Chocolate', 'Milk']}
    >>> potential_ideas_for_business(items)
    ['Chocolate', 'Eggs', 'Flour', 'Milk']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 2': [], \
    'supplier 3': []}
    >>> potential_ideas_for_business(items)
    ['Chocolate', 'Eggs', 'Flour', 'Milk']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk']}
    >>> potential_ideas_for_business(items)
    ['Chocolate', 'Eggs', 'Flour', 'Milk']
    """
    unique_lst = []
    for supplier in items.values():
        for item in supplier:
            if item not in unique_lst:
                unique_lst.append(item)
    return sorted(unique_lst)

# Question 6.1
def count_lines_1(filepath):
    """
    count the line of files.

    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24
    >>> count_lines_1('files/offices1.txt')
    3
    >>> count_lines_1('files/offices2.txt')
    4
    >>> count_lines_1('files/AlErNaTiNg.txt')
    2
    """
    with open(filepath, 'r') as f:
        count = 0
        for line in f:
            count += 1
    return count


# Question 6.2
def count_lines_2(filepath):
    """
    count the line of files.

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24
    >>> count_lines_2('files/offices1.txt')
    3
    >>> count_lines_2('files/offices2.txt')
    4
    >>> count_lines_2('files/AlErNaTiNg.txt')
    2
    """
    with open(filepath, 'r') as f:
        text = f.read().split('\n')
    return len(text)


# Question 6.3
def count_lines_3(filepath):
    """
    count the lines of files

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24
    >>> count_lines_3('files/offices1.txt')
    3
    >>> count_lines_3('files/offices2.txt')
    4
    >>> count_lines_3('files/AlErNaTiNg.txt')
    2
    """
    with open(filepath, 'r') as f:
        line = f.readlines()
    return len(line)


# Question 7
def collected_items(filepath):
    """
    take the item from each file and put it
    in same order provided in the file.

    >>> collected_items('files/ings1.txt')
    ['ice-cream', 'boba tea', 'fish']
    >>> collected_items('files/ings2.txt')
    ['shovel', 'headphones', 'bird', 'brownies']
    >>> collected_items('files/empty_trip.txt')
    []

    # Add at least 3 doctests below here #
    >>> collected_items('files/ings3.txt')
    ['shovel']
    >>> collected_items('files/ings4.txt')
    ['shovel', 'headphones', 'bird', 'brownies', '1']
    >>> collected_items('files/ings5.txt')
    ['shovel', 'headphones']
    """
    items = []
    index = 2
    with open(filepath, 'r') as f:
        line = f.readlines()
        for i in line:
            items.append(i.split(',')[index])
    return items


# Question 8
def case_letters(filepath):
    """
    return the numebr of uppercase letter
    and lowercase letter in the file path

    >>> case_letters('files/AlErNaTiNg.txt')
    >>> with open('files/AlErNaTiNg.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    5
    13
    >>> case_letters('files/another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    19

    # Add at least 3 doctests below here #
    >>> case_letters('files/AIJ.txt')
    >>> with open('files/AIJ.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    3
    8

    >>> case_letters('files/p()()()().txt')
    >>> with open('files/p()()()().txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    9

    >>> case_letters('files/adsfoij.txt')
    >>> with open('files/adsfoij.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    15
    """
    upper_num = 0
    lower_num = 0
    for i in filepath:
        if i.isupper():
            upper_num += 1
        elif i.islower():
            lower_num += 1
    with open(filepath, 'w') as f:
        f.write(str(upper_num) + "\n" + str(lower_num))


# Question 9
def map_office(filepath):
    """
    return the sum of all the positive office
    number and add the number in the corresponding
    floor file following by these mapping rules.
    Less than 1 is 'not a valid office number'
    Between 1 and 199 (inclusive) is ‘ground floor’
    Between 200 and 299 (inclusive) is ‘second floor’
    Above 300 (inclusive) is ‘third floor and above’


    >>> map_office('files/offices1.txt')
    259
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number
    second floor

    >>> map_office('files/offices2.txt')
    734
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    third floor and above
    not a valid office number
    second floor
    ground floor

    >>> map_office('files/offices3.txt')
    0
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    not a valid office number

    >>> map_office('files/offices4.txt')
    0
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    not a valid office number
    not a valid office number


    >>> map_office('files/offices5.txt')
    11000
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    third floor and above
    third floor and above
    """
    ground_floor = 199
    second1 = 200
    second2 = 299
    third_floor = 300
    sum_num = 0
    text = []
    with open(filepath, 'r') as f:
        line = f.readlines()
        for i in line:
            if int(i) >= 0:
                sum_num += int(i)
        for i in line:
            if int(i) < 1:
                text.append("not a valid office number")
            elif 1 <= int(i) <= ground_floor:
                text.append("ground floor")
            elif second1 <= int(i) <= second2:
                text.append("second floor")
            elif int(i) >= third_floor:
                text.append("third floor and above")
    with open('files/floors.txt', 'w') as f:
        for i in text:
            f.write(i + "\n")
    return sum_num



