"""
DSC 20 Winter 2026 Lab 02
Name: Yanhao Wu
PID: A19061338
"""

# Question 1
def name_plates(names):
    """
    Removes first and last character of each name, or 'new name is needed'
    if name is less than 3 characters.
    --
    Parameters:
        names: list of strings
    --
    Returns:
        A list of new names generated based on rule above

    >>> names = ["Marina", "Ty", "Jane Doe"]
    >>> name_plates(names)
    ['arin', 'new name is needed', 'ane Do']
    >>> names = ["Charisse Hao", 'Nicole Zhang ']
    >>> name_plates(names)
    ['harisse Ha', 'icole Zhang']
    >>> names = ['', 'ML']
    >>> name_plates(names)
    ['new name is needed', 'new name is needed']
    """
    new_names = []
    for i in names:
        if len(i) < 3:
            new_names.append('new name is needed')
        else:
            new_names.append(i[1:-1])
    return new_names


# Question 2
def checking_length(names):
    """
    Create a copy list of tuples, replace name with 'too short'
    and the number with 0 if there are not enough characters to remove.
    --
    Parameters:
        names: a list of tuples of the format (<string>, <int>)
    --
    Returns:
        A new list of tuples with original tuples changed or replaced.

    >>> names = [("Cardiff", 4), ("Doe", 1), ("Rogers", 3), \
('Stark', 2), ('', 4)]
    >>> checking_length(names) 
    [('too short', 0), ('Doe', 1), ('Rogers', 3), ('Stark', 2), \
('too short', 0)]
    >>> names = [("Cardiff", 2), ("Bond", 4), ("Odinson", 6), \
('Strange', 8), ('Danvers', 2)]
    >>> checking_length(names)
    [('Cardiff', 2), ('too short', 0), ('too short', 0), \
('too short', 0), ('Danvers', 2)]
    >>> names = []
    >>> checking_length(names)
    []
    """
    new_names = []
    for i in names:
        if len(i[0]) < i[1] * 2:
            new_names.append(("too short", 0))
        else:
            new_names.append((i[0], i[1]))
    return new_names


# Question 3
def remove_characters(names, threshold):
    """
    Removes `threshold` number of first and last characters from each
    name in inner lists, or 'too short' if there are not enough characters.
    --
    Parameters:
        names: a list of list(s) of names
        thresholds: a positive integer
    --
    Returns:
        The modified original list with characters removed or replaced

    >>> names = [["Cardiff", "Marina Langlois", "James Bond"], \
['Barbie ', 'Batman']] 
    >>> remove_characters(names, 1) 
    [['ardif', 'arina Langloi', 'ames Bon'], ['arbie', 'atma']]
    >>> remove_characters(names, 4) 
    [['too short', 'a Lan', ''], ['too short', 'too short']]
    >>> remove_characters(names, 5)
    [['too short', 'too short', 'too short'], ['too short', 'too short']]
    >>> remove_characters([],10)
    []
    """
    for i,j in enumerate(names):
        for index, name in enumerate(j):
            if len(name) < threshold * 2:
                names[i][index] = "too short"
            else:
                names[i][index] = names[i][index][threshold:-threshold]
    return names


# Question 4
def time_for_food(choices):
    """
    Returns a list with capitalized names with preferred time that is 
    either 'A' or 'M'.
    Start from empty list and return immediately if a time that is not 
    'A' or 'M' is found.
    --
    Parameters:
        choices: a list of lists of the form [<str>, <str>], with name 
            and time
    --
    Returns:
        A new list with the name(s) capitalized

    >>> choices = [["Marina", "A"], ["Jessica", "M"], ["Anish", "M"]]
    >>> time_for_food(choices)
    ['MARINA', 'JESSICA', 'ANISH']
    >>> choices = [["Batman", "A"], ["James", "m"], \
    ["Jay Gatsby", "O"]]
    >>> time_for_food(choices)
    ['BATMAN']
    >>> choices = [["James", "O"], ["Marina", "A"], ["Bond", "M"]]
    >>> time_for_food(choices)
    []
    """
    cap_names = []
    for i in choices:
        if i[1] == "A" or i[1] == "M":
            cap_names.append(i[0].upper())
        else:
            break
    return cap_names


# Question 5
def morning_people(input_string, last_character):
    """
    Finds number of strings ending with `last_character` and second 
    last is alphabetic.
    --
    Parameters:
        input_string: string of names separated by one space
        last_character: a character to match with the last character
            of each name
    --
    Returns:
        The number of people satisfying condition

    >>> input_string = "Marina Langlois Anya Willy Wonka"
    >>> morning_people(input_string, 'a')
    3
    >>> input_string = "Marina Henry Monica Louis@a"
    >>> morning_people(input_string, 'a')
    2
    >>> input_string = "Maria An@ns !reys James"
    >>> morning_people(input_string, 's')
    3
    >>> input_string = "Marin! Langloi!!!"
    >>> morning_people(input_string, '!')
    1
    """
    num = 0
    words = input_string.split(" ")
    for i in words:
        if i[-1] == last_character and i[-2].isalpha():
            num += 1
    return num


# Question 6.1
def question_1(dishes):
    """
    Finds the number of dishes
    --
    Parameters:
        dishes: dictionary with dishes as keys and ingredients as values
    --
    Returns:
        The total number of dishes

    >>> recipe1 = {"Tacos": ["Spices","Beef", "Salsa"], \
"Omelet": ["Eggs","Milk", "Salt", "Butter"]}
    >>> question_1(recipe1)
    2
    >>> recipe2 = {}
    >>> question_1(recipe2)
    0
    >>> recipe3 = {"Salad": [], "Hotpot": [], "Burger": ["Beef", \
"Buns", "lettuce"]}
    >>> question_1(recipe3)
    3
    """

    return len(dishes)


# Question 6.2
def question_2(dishes):
    """
    Finds the list of all dishes
    --
    Parameters:
        dishes: dictionary with dishes as keys and ingredients as values
    --
    Returns:
        A list of all dish names

    >>> recipe1 = {"Tacos": ["Spices","Beef", "Salsa"], \
"Omelet": ["Eggs","Milk", "Salt", "Butter"]}
    >>> question_2(recipe1)
    ['Tacos', 'Omelet']
    >>> recipe2 = {}
    >>> question_2(recipe2)
    []
    >>> recipe3 = {"Salad": [], "Hotpot": [], "Burger": ["Beef", \
"Buns", "lettuce"]}
    >>> question_2(recipe3)
    ['Salad', 'Hotpot', 'Burger']
    """
    return list(dishes.keys())


# Question 6.3
def question_3(dishes):
    """
    Finds the number of ingredients of the dish with least ingredients.
    If no dish, return 0.
    --
    Parameters:
        dishes: dictionary with dishes as keys and ingredients as values
    --
    Returns:
        The least number of ingredients

    >>> recipe1 = {"Tacos": ["Spices","Beef", "Salsa"], \
"Omelet": ["Eggs","Milk", "Salt", "Butter"]}
    >>> question_3(recipe1)
    3
    >>> recipe2 = {}
    >>> question_3(recipe2)
    0
    >>> recipe3 = {"Salad": [], "Hotpot": [], "Burger": ["Beef", \
"Buns", "lettuce"]}
    >>> question_3(recipe3)
    0
    """
    if len(dishes) == 0:
        return 0
    else:
        nums = []
        values = list(dishes.values())
        for i in values:
            nums.append(len(i))
        return min(nums)


# Question 6.4
def question_4(dishes):
    """
    Finds the name of the dish with the most number of ingredients.
    If there is a tie, return the last one.
    --
    Parameters:
        dishes: dictionary with dishes as keys and ingredients as values
    --
    Returns:
        The name of the dish.

    >>> recipe1 = {"Tacos": ["Spices","Beef", "Salsa"], \
"Omelet": ["Eggs","Milk", "Salt", "Butter"]}
    >>> question_4(recipe1)
    'Omelet'
    >>> recipe2 = {}
    >>> question_4(recipe2)
    ''
    >>> recipe3 = {"Salad": [], "Hotpot": [], "Burger": []}
    >>> question_4(recipe3)
    'Burger'
    """
    max_num = 0
    max_dish = ""
    for dish,ingredient in dishes.items():
        if len(ingredient) >= max_num:
            max_num = len(ingredient)
            max_dish = dish
    return max_dish


# Question 6.5
def question_5(dishes, new_dish):
    """
    Adds new dish to current dictionary of dishes. If dish already exists, 
    do nothing; if the dish does not yet exist in dictionary, add empty 
    list as its value.
    --
    Parameters:
        dishes: dictionary with dishes as keys and ingredients as values
        new_dish: string name of dish
    --
    Returns:
        Updated dictionary with new dish

    >>> recipe1 = {}
    >>> question_5(recipe1, 'Burger')
    {'Burger': []}
    >>> recipe2 = {'Omelet': ["Eggs","Milk", "Salt", "Butter"]}
    >>> question_5(recipe2, 'Omelet')
    {'Omelet': ['Eggs', 'Milk', 'Salt', 'Butter']}
    >>> question_5(recipe2, 'Salad')
    {'Omelet': ['Eggs', 'Milk', 'Salt', 'Butter'], 'Salad': []}
    """
    if not(new_dish in dishes):
        dishes[new_dish] = []
    return dishes


# Question 6.6
def question_6(dishes, new_dish, ingredient):
    """
    Adds ingredient to the list of ingredients of `new_dish` in 
    the dictionary if it exists; if not, create a list as value 
    with the ingredient as element.
    --
    Parameters:
        dishes: dictionary with dishes as keys and ingredients as values
        new_dish: string dish name
        ingredient: string 
    --
    Returns:
        The updated dictionary.

    >>> recipe1 = {}
    >>> question_6(recipe1, 'Salad', 'tomato')
    {'Salad': ['tomato']}
    >>> recipe2 = {'Salad': ['tomato']}
    >>> question_6(recipe2, 'Salad', 'chicken')
    {'Salad': ['tomato', 'chicken']}
    >>> recipe3 = {'Salad': ['tomato']}
    >>> question_6(recipe3, 'Salad', 'tomato')
    {'Salad': ['tomato', 'tomato']}
    """
    if new_dish in dishes:
        dishes[new_dish].append(ingredient)
    else:
        dishes[new_dish] = [ingredient]
    return dishes

# Question 6.7
def question_7(dishes, ingredient):
    '''
    Removes `ingredient` from all lists of ingredients in `dishes` if 
    exists in list.
    --
    Parameters:
        dishes: dictionary with dishes as keys and ingredients as values
        ingredient: string
    --
    Returns:
        Updated dictionary

    >>> recipe1 = {'Salad': ['tomato']}
    >>> question_7(recipe1, 'arugula')
    {'Salad': ['tomato']}
    >>> recipe2 = {'Salad': ['tomato', 'kale', 'spinach']}
    >>> question_7(recipe2, 'kale')
    {'Salad': ['tomato', 'spinach']}
    >>> recipe3 = {'Salad': ['tomato', 'spinach'], 'Burger': ['tomato']}
    >>> question_7(recipe3, 'tomato')
    {'Salad': ['spinach'], 'Burger': []}
    '''
    for i in dishes.values():
        if ingredient in i:
            i.remove(ingredient)
    return dishes

# Question 7
def password_to_lounge(names_dict):
    """
    Constructs secret language based on 3 rules:
    (1) If code is even-length string, reverse name;
    (2) If code is non-negative integer, add X `#` where X is name length;
    (3) If code is negative integer, get first character of name.
    --
    Parameters:
        names_dict: dictionary of names as keys and code as values
    --
    Returns:
        A password generated based on rules above.

    >>> dict1 = {'Adrian': 'haha', 'Marina': 1, \
'Langlois': 0, 'Walter': -2}
    >>> password_to_lounge(dict1)
    'nairdA##############W'
    >>> dict2 = {'Ty': 'dsc', '': 20}
    >>> password_to_lounge(dict2)
    ''
    >>> dict3 = {'M.L.': 5, 'DSC20': 'ab'}
    >>> password_to_lounge(dict3)
    '####02CSD'
    """
    password = ""
    for i,j in names_dict.items():
        if type(j) == str:
            if len(j) % 2 == 0:
                password = password + i[::-1]
        elif j >= 0:
            password = password + "#" * len(i)
        elif j < 0:
            password = password + i[0]
    return password
