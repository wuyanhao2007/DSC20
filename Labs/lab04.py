"""
DSC 20 Winter 2026 Lab 04
Name: Yanhao Wu
PID: A19061338
"""

# Question 1.1
def problem_1(int_lst, mult_factor):
    """
    Multiply each element in a list by `mult_factor`
    ---
    Parameters:
        int_lst: a list of integers 
        mult_factor: an integer
    ---
    Returns:
        a new list where each element in the original list is 
        multiplied by mult_factor

    >>> problem_1([1, 3, 5], 3)
    [3, 9, 15]
    >>> problem_1([1, 3, 5], 0)
    [0, 0, 0]
    >>> problem_1([], -10)
    []
    """
    return list(map(lambda x: x * mult_factor, int_lst))


# Question 1.2
def problem_2(int_lst, factor):
    """
    Returns a list where each number has the `factor`
    ---
    Parameters:
        int_lst: a list of integers 
        factor: a positive integer
    ---
    Returns:
        a new list, where each element from a given list 
        has a given factor

    >>> problem_2([1, 3, 5], 3)
    [3]
    >>> problem_2([1, 3, 5], 1)
    [1, 3, 5]
    >>> problem_2([], 10)
    []
    >>> problem_2([1, 3, 4, 6, 5], 2)
    [4, 6]
    """

    return list(filter(lambda x: x % factor == 0, int_lst))


# Question 1.3
def problem_3(int_lst, factor):
    """
    Returns a list where each number has the `factor`, or None if not
    ---
    Parameters:
        int_lst: a list of integers 
        factor: a positive integer
    ---
    Returns:
        a list, where each element from a given list has a given factor, 
        and if that's not the case, replace it with None

    >>> problem_3([1, 3, 5], 3)
    [None, 3, None]
    >>> problem_3([1, 3, 5], 1)
    [1, 3, 5]
    >>> problem_3([], 10)
    []
    >>> problem_3([1, 3, 4, 6, 5], 2)
    [None, None, 4, 6, None]
    """
    return list(map(lambda x: x if x % factor == 0 else None, int_lst))


# Question 1.4
def problem_4(lst):
    """
    Remove all None values from the list
    ---
    Parameters:
        lst: a list of integers and/or None values
    ---
    Returns:
        a list that contains only the integers

    >>> problem_4([None, 3, None])
    [3]
    >>> problem_4([None, None, 4, 6, None])
    [4, 6]
    >>> problem_4([0, 1, 2, 3, 4, None])
    [0, 1, 2, 3, 4]
    >>> problem_4([])
    []
    """
    return list(filter(lambda x: x is not None, lst))


# Question 2.1
def forming_teams_1(teams, limit):
    """
    Returns a list with team names whose members all meet a minimum
    skill rating, or 'Need more practice' otherwise.
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names) 
            - the values are lists of integers (individual skill ratings)
        limit: an integer which specifies the minimum required rating
    ---
    Returns:
        a list of team names that have met the minimum skill requirement, 
        or the string 'Need more practice' if not

    >>> teams = {"team1": [5, 7, 6], "team2": [3, 8]}
    >>> forming_teams_1(teams, 5)
    ['team1', 'Need more practice']
    >>> forming_teams_1(teams, 6)
    ['Need more practice', 'Need more practice']
    >>> forming_teams_1(teams, 0)
    ['team1', 'team2']
    >>> forming_teams_1({}, 3)
    []
    """
    return list(map(
        lambda dic: dic[0] if list(
            filter(
                lambda x: x >= limit, dic[1]
            )
        ) == dic[1] else "Need more practice", teams.items()
    ))


# Question 2.2
def forming_teams_2(teams, limit):
    """
    Returns a list with only team names whose members all meet a 
    minimum skill rating.
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names) 
            - the values are lists of integers (individual skill ratings)
        limit: an integer which specifies the minimum required rating
    ---
    Returns:
        a list containing only the keys of the teams whose minimum 
        skill rating is at least limit

    >>> teams = {"team1": [5, 7, 6], "team2": [3, 8]}
    >>> forming_teams_2(teams, 5)
    ['team1']
    >>> forming_teams_2(teams, 6)
    []
    >>> forming_teams_2(teams, 0)
    ['team1', 'team2']
    >>> forming_teams_2({}, 3)
    []
    """

    return list(map(lambda tup: tup[0], (filter(
        lambda dic: list(
            filter(
                lambda x: x >= limit, dic[1]
            )
        ) == dic[1], teams.items()
    ))))


# Question 3.1
def next_round_1(teams, penalty, threshold):
    """
    Returns the teams advancing to next round based on whether their score is 
    at least `threshold` after applying a `penalty`, along with their adjusted
    score, in a list of tuples
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names)
            - the values are integers (the team's corresponding score) 
        penalty: an integer penalty to be subtracted from each team's score
        threshold: an integer representing the minimum score required 
        to advance
    ---
    Returns:
        a list of tuples: each tuple should contain the name of a team that 
        advances to the next round as the first element, and their adjusted 
        score as the second element

    >>> next_round_1({"team1": 15, "team2": 20}, 5, 10)
    [('team1', 10), ('team2', 15)]
    >>> next_round_1({"team1": 15, "team2": 30}, 10, 10)
    [('team2', 20)]
    >>> next_round_1({"team1": 5, "team2": 14}, 0, 20)
    []
    >>> next_round_1({}, 2, 3)
    []
    """
    # YOUR CODE GOES HERE #
    return


# Question 3.2
def next_round_2(teams, penalty, threshold):
    """
    Returns the teams advancing to next round and the number of their adjusted
    scores that meet the advancement requirement
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names) 
            - the values are lists of integers (the team's corresponding
            scores)
        penalty: an integer penalty to be subtracted from each individual score
        threshold: an integer representing the score required to advance
    ---
    Returns:
        a list of tuples: each tuple should contain the name of a team that
        advances to the next round as the first element, and the number of
        their adjusted scores that meet or exceed the required threshold as the
        second element

    >>> next_round_2({"team1": [10, 15, 20], "team2": [20]}, 5, 10)
    [('team1', 2), ('team2', 1)]
    >>> next_round_2({"team1": [], "team2": [36, 4, 20, 0]}, 11, 10)
    [('team1', 0), ('team2', 1)]
    >>> next_round_2({}, 3, 3)
    []
    """
    # YOUR CODE GOES HERE #
    return


# Question 3.3
def next_round_3(teams, results):
    """
    Finds the teams that advance: ('qualified', 'advanced', 'winner'), returns
    a list of tuples with team name and result
    ---
    Parameters:
        teams: a list of strings with team names
        results: a list of strings with the result for each team
    ---
    Returns:
        a list of tuples for only the teams that have advanced to the next
        round; in each tuple, the first element should be the team's name,
        and the second element should be their result, both as strings

    >>> next_round_3(['team1', 'team2', 'team3'], ['qualified', 'out', 'winner'])
    [('team1', 'qualified'), ('team3', 'winner')]
    >>> next_round_3(['team1', 'team2'], ['eliminated', 'out'])
    []
    >>> next_round_3(['team1', 'team2'], ['eliminated', 'advanced'])
    [('team2', 'advanced')]
    >>> next_round_3([], [])
    []
    """
    # YOUR CODE GOES HERE #
    return
