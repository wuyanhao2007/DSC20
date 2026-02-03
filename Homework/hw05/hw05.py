"""
DSC 20 Winter 2026 Homework 05
Name: TODO
PID: TODO
Source: TODO
"""

# Question 1

def get_qualified_customers(data, max_avg, min_range):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    # YOUR CODE GOES HERE # 
    


# Question 2

def message_to_customers(customer_file, decision, message):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    # YOUR CODE GOES HERE #
            


# Question 3

def forge_votes(vote_file):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    # YOUR CODE GOES HERE #
    

# Question 4

def make_greeter(prefix):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    # YOUR CODE GOES HERE #

# Question 5

def make_another_greeter(user_type):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    # YOUR CODE GOES HERE #


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
    return [..., ..., ..., ..., ..., ..., ..., ..., ..., ...]