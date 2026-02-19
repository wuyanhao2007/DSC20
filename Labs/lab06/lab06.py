"""
DSC 20 Winter 2026 Lab 06
Name: Yanhao Wu
PID: A19061338
"""

# Question 1
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function. You don't need to add new doctests for this function.
    
    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 10 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-10, duplicates allowed) #
    return [6, 4, 7, 7, 3, 6, 4, 10, 10, 6]

# Question 2.1
def number_of_adults_1(lst, age = 18):
    """
    For every three children aged less than or equal to the given age
    threshold, one adult is needed.
    ---
    Parameters:
        - lst (list of ints): Ages of individuals.
        - age (int): Age threshold, defaulted to 18.
    ---
    Returns:
        int: Number of adults needed.
    
    >>> number_of_adults_1([1,2,3,4,5,6,7])
    3
    >>> number_of_adults_1([1,2,3,4,5,6,7], 5)
    2
    >>> number_of_adults_1([1,2,3,4,5,6,7], age = 2)
    1
    """

    return (len([i for i in lst if i <= age]) + 2) // 3

# Question 2.2
def number_of_adults_2(*args):
    """
    For every three children younger than the given age 
    threshold, one adult is needed.
    --- 
    Parameters:
        *args (int): A variable number of integer
        ages to check. Each integer represents the 
        age of an individual.
    ---
    Returns:
        int: Number of adults needed.

    >>> number_of_adults_2(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_2(10,20,13,4)
    1
    >>> number_of_adults_2(19, 20)
    0
    """
    return (len([i for i in args if i <= 18]) + 2) // 3

# Question 2.3
def number_of_adults_3(*args, age = 18):
    """
    For every three children younger than the given age 
    threshold, one adult is needed.
    --- 
    Parameters:
        *args (int): A variable number of integer
        ages to check. Each integer represents the 
        age of an individual.
        age (int): Age threshold, defaulted to 18.
    ---
    Returns:
        int: Number of adults needed.
    
    >>> number_of_adults_3(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 5)
    2
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 2)
    1
    """
    return (len([i for i in args if i <= age]) + 2) // 3

# Question 3
def activities_of_children(activity, **kwargs):
    """
    Determines which children will participate in the proposed activity.
    ---
    Parameters:
        - activity (str): The activity to check participation for.
        - **kwargs: Variable keyword arguments where each key is a
        child's name and each value is a list of activities the 
        child is interested in.
    ---
    Returns:
    list of tuples: Each tuple contains the child's name
    and a boolean indicating whether the child will participate
    in the specified activity.

    >>> activities_of_children("soccer", Marina = ['soccer', \
    'basketball', 'tennis'], Rob = ['swimming', 'tennis'], \
    Adrian = ['tennis', 'soccer', 'volleyball'])
    [('Marina', True), ('Rob', False), ('Adrian', True)]

    >>> activities_of_children("swimming", Sam = ['soccer', \
    'swimming', 'tennis'], \
    Yue = ['volleyball', 'tennis'], \
    Pooja = ['badminton', 'running'])
    [('Sam', True), ('Yue', False), ('Pooja', False)]

    >>> activities_of_children("tennis", Karina = [], \
    Else=['soccer', 'swimming'], \
    David=['basketball', 'running'], \
    Yacun=['tennis', 'badminton'])
    [('Karina', False), ('Else', False), ('David', False), ('Yacun', True)]

    >>> activities_of_children("basketball")
    []
    """
    return [(name, True) if activity in act
            else (name, False) for name,act in kwargs.items()]


# Question 4
def files_target_count(target, *args):
    """
    Get count of the target character across all files.
    Not case sensitive.
    ---
    Parameters:
        - target (str): the target character
        - *args: unspecified number of file names as strings
    ---
    Returns:
        - int: Target character count across all files.

    >>> files_target_count('e', 'files/file1.txt', 'files/file2.txt')
    5
    >>> files_target_count('\\n', 'files/file1.txt', 'files/file2.txt')
    10
    >>> files_target_count('E', 'files/file1.txt', 'files/file2.txt')
    5
    >>> files_target_count('', 'files/file1.txt', 'files/file2.txt')
    0
    >>> files_target_count('e', 'files/file1.txt', 'files/file2.txt',\
     'files/file3.txt', 'files/file4.txt')
    99
    >>> files_target_count('\\n', 'files/file2.txt', 'files/file4.txt',\
     'files/file3.txt')
    26
    """
    count = 0
    if len(target) == 0:
        return 0
    for i in args:
        with open(i, "r") as f:
            lines = f.readlines()
            for j in lines:
                count += j.lower().count(target.lower())
    return count

# Question 5
def field_trip(age_limit, **kwargs):
    """
    Determines the number of adults needed for each group based
    on the age limit. For every three children younger than the
    specified age limit, one adult is needed.
    ---
    Parameters:
        - age_limit (int): The maximum age considered as a child.
        - **kwargs: Variable keyword arguments where each key is 
        a group ID, and the value is a list of children's ages in 
        that group.
    ---
    Returns:
        dict: A dictionary where each key is a group ID, and the 
        value is the number of adults required for that group.

    >>> field_trip(14, group1 = [1, 2, 3], group2 = [4, 5, 6, 7], \
    group3=[15, 16])
    {'group1': 1, 'group2': 2, 'group3': 0}
        
    >>> field_trip(14, group1 = [21, 3], group2 = [41, 1, 2, 24, 6], \
    group3=[30, 3, 1, 7, 88])
    {'group1': 1, 'group2': 1, 'group3': 1}
        
    >>> field_trip(100, group1 = [21, 3], group2 = [41, 1000, 2, 24, 6], \
    group3 = [3, 1, 7, 88])
    {'group1': 1, 'group2': 2, 'group3': 2}
    """
    return {group: number_of_adults_3(*lst, age = age_limit) for group,lst in kwargs.items()}