"""
DSC 20 Fall 2025 Homework 01
Name: Yanhao Wu
PID: A19061338
"""
# Question 1
def login(fname, lname):
    """
    Reverse fname and take every other character
    and take everythird character from lname to
    create a company login for the members

    >>> login("Marina", "Langlois")
    'aiaLgi'
    >>> login("", "")
    ''
    >>> login("San", "Diego")
    'nSDg'

    # Add your own doctests below
    >>> login("Charlie", "Kirk")
    'elaCKk'
    >>> login("", "Brandon")
    'Bnn'
    >>> login("ali", "")
    'ia'
    """
    username = ""
    interval_first = -2
    interval_second = 3
    for i in range(len(fname) -1, -1, interval_first):
        username = username + fname[i]
    for i in range(0, len(lname), interval_second):
        username = username + lname[i]
    return username

# Question 2
def ages(age1, age2):
    """
    Take the age that is closer but less than 23,
    if both ages are at least 23, return “You both
    can rent!”

    >>> ages(19, 21)
    21
    >>> ages(26, 21)
    21
    >>> ages(26, 27)
    'You both can rent!'
    >>> ages(19, 23)
    19

    # Add your own doctests below
    >>> ages(19, 23)
    19
    >>> ages(23, 23)
    'You both can rent!'
    >>> ages(20, 26)
    20
    """
    legal_age = 23
    if age1 >= legal_age:
        if age2 >= legal_age:
            return 'You both can rent!'
        else:
            return age2
    else:
        if age2 >= legal_age:
            return age1
        else:
            return max(age1, age2)


# Question 3
def renter(name1, name2, name3):
    """
    take the longest name from the argument,
    if they are same length, take the last one


    >>> renter("K", "BB", "Joy")
    'Joy'
    >>> renter("Joy", "K", "BB")
    'Joy'
    >>> renter("BB", "Joy", "K")
    'Joy'
    >>> renter("BB", "K", "Jo")
    'Jo'
    >>> renter("BB", "Jo", "Su")
    'Su'

    # Add your own doctests below
    >>> renter("BB", "Jo", "K")
    'Jo'
    >>> renter("B", "J", "K")
    'K'
    >>> renter("", "", "")
    ''
    """
    index = -1
    longest_number = -1
    name_list = [name1, name2, name3]
    for i in range(len(name_list)):
        if longest_number <= len(name_list[i]):
            longest_number = len(name_list[i])
            index = i
    return name_list[index]


# Question 4.1
def helper_distance(lst, x2, y2):
    """
    calculates the Euclidean distance between two given points.
    
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance ([100, 100], 100.5, 100)
    0.5

    # Add your own doctests below
    >>> helper_distance([3, 3], 3, 4)
    1.0
    >>> helper_distance([3, 4], 3, 4)
    0.0
    >>> helper_distance([0, 4], 3, 4)
    3.0
    """
    root = 0.5
    square = 2
    length = x2 - lst[0]
    width = y2 - lst[1]
    return (length ** square + width ** square) ** root

# Question 4.2
def lunch(lunch_places, office_x, office_y, threshold):
    """
    Find the location of the lunch places that walk from the
    office within the threshold

    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> lunch ([[100, 100]], 100.5, 100, 0.2)
    []

    # Add your own doctests below
    >>> lunch([[0, 0], [30.5, 20.7], [100, 100]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([], 3, 4, 5)
    []
    >>> lunch([[3, 4]], 0, 0, 5)
    [[3, 4]]
    """
    within_thr = []
    for i in lunch_places:
        distance = helper_distance(i, office_x, office_y)
        if distance <= threshold:
            within_thr.append(i)
    return within_thr

# Question 5
def lunch_names(lunch_places, office_x, office_y, threshold, names):
    """
    Find the name of the lunch places that walk from the office
     within the threshold

    >>> lunch_names([[0, 0], [30, 20], [5, 9]], 3.2, 4, 6, \
    ['place1', 'place2', 'place3'])
    ['place1', 'place3']
    >>> lunch_names([[-3, -4], [6, 7]], 3, 4, 10, \
    ['place1', 'place2'])
    ['place1', 'place2']
    >>> lunch_names ([[100, 100]], 100.5, 100, 0.2, ['place1'])
    []

    # Add your own doctests below
    >>> lunch_names([[100, 100], [200, 200]], 0, 0, 0.2, ['place1', 'place2'])
    []
    >>> lunch_names([[0, 0]], 0, 0, 0.2, ['place1'])
    ['place1']
    >>> lunch_names([[0, 0], [100, 100]], 3.2, 4, 6, ['place1', 'place2'])
    ['place1']
    """
    within_thr = []
    for i in range(len(lunch_places)):
        distance = helper_distance(lunch_places[i], office_x, office_y)
        if distance <= threshold:
            within_thr.append(names[i])
    return within_thr


# Question 6
def meeting_message(i_name, time, place, s_name):
    """
    takes in the name of the invitee, time of day, place and the name of
     the message creator, as strings. Then, return a string of invitation
     that contain those infomation.

    >>> print(meeting_message("Penny", "3:15pm", "Cheesecake Factory", \
        "Sheldon"))
    Dear Penny,
    Please join our meeting at 3:15pm, at the Cheesecake Factory.
    <BLANKLINE>
    See you soon: Sheldon

    >>> print(meeting_message("Freya", "", "Dog Park", "Marina"))
    Dear Freya,
    Please join our meeting at , at the Dog Park.
    <BLANKLINE>
    See you soon: Marina

    # Add your own doctests below
    >>> print(meeting_message("", "3:15pm", "Dog Park", "Marina"))
    Dear ,
    Please join our meeting at 3:15pm, at the Dog Park.
    <BLANKLINE>
    See you soon: Marina
    >>> print(meeting_message("Freya", "3:15pm", "", "Marina"))
    Dear Freya,
    Please join our meeting at 3:15pm, at the .
    <BLANKLINE>
    See you soon: Marina
    >>> print(meeting_message("Freya", "3:15pm", "Dog Park", "Marina"))
    Dear Freya,
    Please join our meeting at 3:15pm, at the Dog Park.
    <BLANKLINE>
    See you soon: Marina
    """
    greeting = "Dear " + i_name + ",\n"
    text = ("Please join our meeting at " + time + ", at the "
            + place + ".\n\n")
    sign = "See you soon: " + s_name
    return greeting + text + sign


# Question 7
def seat_number(lst):
    """
    assign seat for people and the seaat_number is the length
    of their name. If the seat is taken, return the string
    taken instead.

    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]

    # Add your own doctests below
    >>> seat_number(["Sue", "Tom", "abd"])
    [3, 'taken', 'taken']
    >>> seat_number(["Marina", "Tom", "B", "a", "Sue"])
    [6, 3, 1, 'taken', 'taken']
    >>> seat_number(["Marina"])
    [6]
    """
    assign_seat = []
    for i in lst:
        if len(i) in assign_seat:
            assign_seat.append('taken')
        else:
            assign_seat.append(len(i))
    return assign_seat


# Question 8
def computers(choices):
    """
    compare the amount of DESKtop and LAPtop been voted,
    Return True if `DESKtop` occurs more often and False
    otherwise.

    >>> computers(["DESKtop", "LAPtop", "DESKtop"])
    True
    >>> computers(["LAPtop", "LAPtop"])
    False
    >>> computers(["DESKtop", "Pager", "Tablet", "LAPtop"])
    False

    # Add your own doctests below
    >>> computers(["DESKtop", "", "", "LAPtop"])
    False
    >>> computers(["", "", "", ""])
    False
    >>> computers(["DESKtop", "DESKtop", "DESKtop"])
    True
    """
    desktop_count = choices.count("DESKtop")
    laptop_count = choices.count("LAPtop")
    return desktop_count > laptop_count


# Question 9
def age_average(lst):
    """
    take the average of positive ages.

    >>> age_average(["20", "21", "22"])
    '21.0'
    >>> age_average(["50", "25", "30"])
    '35.0'
    >>> age_average(["40", "-999", "45"])
    '42.5'
    >>> age_average([])
    '0.0'

    # Add your own doctests below
    >>> age_average(["20", "21", "22", "50", "25", "30"])
    '28.0'
    >>> age_average(["-40", "-999", "-45"])
    '0.0'
    >>> age_average(["40", "0"])
    '40.0'
    """
    positive_lst = []
    for i in lst:
        i = int(i)
        if i > 0:
            positive_lst.append(i)
    if len(positive_lst) == 0:
        return '0.0'
    else:
        return str(sum(positive_lst) / len(positive_lst))


# Question 10
def supervision_teams(team, company_name):
    """
    split the people into two supervision teams.
    The first team contains the company name and then the even number
    personnel.
    The second team contains odd number personnel and then the company
    name.

    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])

    # Add your own doctests below
    >>> supervision_teams([], "Marina")
    (['Marina'], ['Marina'])
    >>> supervision_teams(["p1", "p2"], "Marina")
    (['Marina', 'p1'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "1")
    (['1', 'p1'], ['1'])
    """
    even = 2
    team1 = [company_name]
    team2 = []
    for i in range(len(team)):
        if i % even == 0:
            team1.append(team[i])
        else:
            team2.append(team[i])
    team2.append(company_name)
    return (team1, team2)