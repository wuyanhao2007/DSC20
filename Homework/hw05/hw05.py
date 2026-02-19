"""
DSC 20 Winter 2026 Homework 05
Name: Yanhao Wu
PID: A19061338
Source:
"""

# Question 1

def get_qualified_customers(data, max_avg, min_range):
    """
    take a dictionary of ID and the name and
    return the name of the ID have satisfied
    three requirement below:
    The average score should be less than or equal to a
    specified max_avg.
    The range (difference between the largest and
    smallest score) should be greater than or equal to
     a specified min_range.
    There should be no duplicate scores in the list.


    >>> data = { \
        "Jayden": [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    ['Terry']

    >>> data = { \
        "Caleb": [0, 1, 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 2)
    ['Caleb', 'Keenan', 'Rome']

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> data = { \
        "Caleb": [0, 1, 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, -1, 2)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> data = { \
        "Caleb": 1, \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 1)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> data = { \
        "Jayden": [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    []
    """
    assert isinstance(data, dict)
    assert all([isinstance(max_avg, int), isinstance(min_range, int)])
    assert all([max_avg > 0, min_range > 0])
    assert all([isinstance(i, list) for i in data.values()])
    mean = lambda x: sum(x) / len(x) if len(x) != 0 else 0
    range_lst = lambda x: max(x) - min(x) if len(x) != 0 else 0
    return [i for i, j in data.items() if len(set(j)) == len(j)
            and mean(j) <= max_avg and range_lst(j) >= min_range]


# Question 2

def message_to_customers(customer_file, decision, message):
    """
    return a list of messages to the customers based on
    the decision. If the decision is “s” you should send
    a message to all the customers who are staying. If
    the decision is “w” you should send a message to all
    the customers who are waitlisted.

    >>> msg = "unfortunately we cannot work with you."
    >>> message_to_customers("files/customers.txt", "w", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, \
unfortunately we cannot work with you.', \
'(to: jensen@nvidia.com) Dear Jensen at NVIDIA, \
unfortunately we cannot work with you.']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers.txt", "s", msg)
    ['(to: jeff@amazon.com) Dear Jeff at Amazon, \
we are excited to work with you!', \
'(to: mark@fb.com) Dear Mark at Facebook, \
we are excited to work with you!']

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> msg = 1
    >>> message_to_customers("files/customers.txt", "s", msg)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers.txt", "a", msg)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> msg = "hello"
    >>> message_to_customers("files/customers.txt", "s", msg)
    ['(to: jeff@amazon.com) Dear Jeff at Amazon, \
hello', \
'(to: mark@fb.com) Dear Mark at Facebook, \
hello']
    """
    assert isinstance(customer_file, str)
    assert isinstance(decision, str)
    assert decision == 'w' or decision == 's'
    assert isinstance(message, str)
    second_num = 2
    with open(customer_file, 'r') as f:
        cus_lst = []
        for i in f:
            cus_lst.append(i.strip("\n").split(","))
    def format_lst(lst):
        '''
        returns the message to the customers
        '''
        return (f"(to: {lst[second_num]}) Dear {lst[1]} "
                f"at {lst[0]},"
                f" {message}")
    in_lst = list(filter(lambda x: x[-1] == decision,
                         cus_lst))
    return [format_lst(i) for i in in_lst]


# Question 3

def forge_votes(vote_file):
    """
    Make sure in the file, the amount of people
    vote for yes which is 1 is strictly more
    than half of the total people

    >>> forge_votes("files/vote1.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,0
    Clyde,1
    Andy,1

    >>> forge_votes("files/vote2.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote3.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Andy,1

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> forge_votes("files/vote4.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote5.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,1
    Maxx,1
    Tre,1
    Jakobi,1

    >>> forge_votes("files/vote6.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,1
    Maxx,1
    Tre,0
    Jakobi,0
    """
    second_num = 2
    with open(vote_file, "r") as fr:
        lines = fr.readlines()
    vote_prev = [int(i.strip("\n").split(",")[1]) for i in lines]
    if sum(vote_prev) > len(vote_prev) / second_num:
        return_txt = "".join(lines)
    else:
        change = (len(vote_prev) // second_num + 1) - sum(vote_prev)
        return_txt = "".join(lines).replace(
            "0", "1", change)
    with open("files/forged.txt", "w") as fw:
        fw.write(return_txt)


# Question 4

def make_greeter(prefix):
    """
    returns a method that can make a greeting message
    combining by the prefix and the name.

    >>> hello_greeter = make_greeter("Hello")
    >>> hello_greeter("Anna")
    'Hello, Anna!'
    >>> hello_greeter("Yu")
    'Hello, Yu!'
    >>> welcome_greeter = make_greeter("Welcome")
    >>> welcome_greeter("Anna")
    'Welcome, Anna!'
    >>> welcome_greeter("Pooja")
    'Welcome, Pooja!'

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> hello_greeter = make_greeter("wassup")
    >>> hello_greeter("Anna")
    'wassup, Anna!'

    >>> hello_greeter = make_greeter("")
    >>> hello_greeter("")
    ', !'

    >>> hello_greeter = make_greeter("hi")
    >>> hello_greeter("Brandon")
    'hi, Brandon!'
    """
    def return_func(name):
        '''
        return the greeting message
        '''
        return prefix + ", " + name + "!"
    return return_func

# Question 5

def make_another_greeter(user_type):
    """
    form a greeting message depending on the user
    types, formal or friendly.

    >>> greeter1 = make_another_greeter("friendly")
    >>> greeter1("Anna")
    'Hey Anna! How’s it going?'
    >>> greeter1("Missy")
    'Hey Missy! How’s it going?'
    >>> greeter2 = make_another_greeter("formal")
    >>> greeter2("Smith", "Mr.")
    'Good day, Mr. Smith.'
    >>> greeter2("Langlois", "Mrs.")
    'Good day, Mrs. Langlois.'

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> greeter3 = make_another_greeter("friendly")
    >>> greeter3("Brandon")
    'Hey Brandon! How’s it going?'

    >>> greeter4 = make_another_greeter("formal")
    >>> greeter4("I", "Mr.")
    'Good day, Mr. I.'

    >>> greeter5 = make_another_greeter("formal")
    >>> greeter5("A", "Mrs.")
    'Good day, Mrs. A.'
    """
    def friend_func(name):
        '''
            return the greeting message in friendly format
        '''
        return 'Hey ' + name + '! How’s it going?'
    def formal_func(l_name, name):
        '''
            return the greeting message in formal format
        '''
        return "Good day, " + name + " " + l_name + "."
    if user_type == "friendly":
        return friend_func
    else:
        return formal_func


# Question 6

def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [False, True, False, True, True, False, True, False, False, False]