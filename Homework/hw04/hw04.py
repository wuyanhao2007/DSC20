"""
DSC 20 Winter 2026 Homework 04
Name: TODO
PID: TODO
Source: TODO
"""

# Question 1
def place_of_birth(file_in):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> place_of_birth('files/info_1.txt')
    {'Chicago': ['Rob'], 'New York': ['Ella'], 'New York.': ['Mary']}
    >>> place_of_birth('files/info_2.txt')
    {'Chicago': ['Rob'], 'London': ['Ezra'], 'Paris': \
['Mary'], 'paris': ['Ron', 'Harry']}
    >>> place_of_birth('files/header.txt')
    {}

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    """
    # YOUR CODE GOES HERE #
    return


# Question 2
def age_groups(file_in, file_out):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> age_groups('files/info_1.txt', 'files/age_1_out.txt')
    >>> with open('files/age_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ella,1
    Mary,-1
    
    >>> age_groups('files/info_2.txt', 'files/age_2_out.txt')
    >>> with open('files/age_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ezra,1
    Mary,1
    Ron,0
    Harry,0

    >>> age_groups('files/header.txt', 'files/empty_out.txt')
    >>> with open('files/empty_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    """
    # YOUR CODE GOES HERE #
    return
                

# Question 3
def several_files(files_lst, file_out, min_year):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> lst_1 = ['files/info_1.txt','files/info_3.txt', 'files/info_4.txt']
    >>> several_files(lst_1, 'files/several_1_out.txt', 1945)
    >>> with open('files/several_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945

    >>> lst_2 = ['files/info_2.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_2_out.txt', 1980)
    >>> with open('files/several_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989


    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    """
    # YOUR CODE GOES HERE #
    return


# Question 4
def postcards(info_list):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> postcards([
    ...     ('Yue Wang', 96, 18, 'Hoover Dam', 'ordinary'),
    ...     ('Cleo Patra', 10, 32, 'Bellagios', 'priority')
    ... ])
    {'Cleo Patra': 'cle32patra$0soigalleb'}
    >>> postcards([])
    {}
    >>> postcards([
    ...     ('Mari Noh', 155, 18, 'tram', 'vip'),
    ...     ('Gwen Am', 34, 54, 'Venetian', 'Priority'),
    ...     ('Freya Dog', 34, 1, 'The Strip', 'priority')
    ... ])
    {'Gwen Am': 'gwe54am$4naitenev', 'Freya Dog': 'fre1dog$4pirts eht'}

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    """
    return


# Question 5
def win_or_lose(lst, operations):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('advance', 5), ('lost', 3), ('tie', 4)]
    >>> win_or_lose(lst, operations_1)
    [14, 125, 1236, 12347, 123458]
    >>> operations_2 = [('lost', 200), ('eliminate', 'Team ')]
    >>> win_or_lose(lst, operations_2)
    ['Team lost', 'Team lost', 'Team lost', 'Team won', 'Team won', 'Team won']

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    """
    # TODO: Fill out the lambda functions as dictionary values
    # Break lines if go past 79 characters
    commands = {
            'advance': lambda lst, amount: ...,
            'lost': lambda lst, amount: ...,
            'tie': lambda lst, threshold: ...,
            'eliminate':  lambda lst, symbol: ...,
            'win': lambda lst, message: ...,
    }
    # YOUR CODE GOES HERE #
    return
