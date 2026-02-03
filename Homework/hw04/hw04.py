"""
DSC 20 Winter 2026 Homework 04
Name: Yanhao Wu
PID: A19061338
Source:
"""

# Question 1
def place_of_birth(file_in):
    """
    take the text in the file and take the location
    in each line as dictionary keys, and the name as
    the list of values

    >>> place_of_birth('files/info_1.txt')
    {'Chicago': ['Rob'], 'New York': ['Ella'], 'New York.': ['Mary']}
    >>> place_of_birth('files/info_2.txt')
    {'Chicago': ['Rob'], 'London': ['Ezra'], 'Paris': \
['Mary'], 'paris': ['Ron', 'Harry']}
    >>> place_of_birth('files/header.txt')
    {}

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> place_of_birth('files/info_3.txt')
    {'San Diego': ['Sue'], 'London': ['Ben']}

    >>> place_of_birth('files/info_4.txt')
    {'Paris': ['Kate']}

    >>> place_of_birth('files/empty_out.txt')
    {}
    """
    with open(file_in, "r") as f:
        lines = f.readlines()[1:]
    ini_dic = {i.split(", ")[1].strip(" "): [] for i in lines}
    for i in lines:
        ini_dic[i.split(", ")[1].strip(" ")].append(
            i.split(", ")[0].strip(" "))
    return ini_dic


# Question 2
def age_groups(file_in, file_out):
    """
    categorize people into three groups: older than 35,
    younger than 35, or exactly 35 years old. You may use
    only the year to determine age (for simplicity). The
    function should not return anything. If the input file
     contains only the header, the output file should also
     contain only the header.


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
    >>> age_groups('files/info_3.txt', 'files/age_3_out.txt')
    >>> with open('files/age_3_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Sue,-1
    Ben,1

    >>> age_groups('files/info_4.txt', 'files/age_4_out.txt')
    >>> with open('files/age_4_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Kate,1

    >>> age_groups('files/empty_out.txt', 'files/empty.txt')
    >>> with open('files/empty.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    """
    header = "name,older than 35\n"
    age = 35
    year = 2024
    second_lst = 2
    fourth_lst = -4
    with open(file_in, "r") as fi:
        lines = fi.readlines()[1:]  # skip header
        if lines:
            lst_info = [[j.strip() for j in i.split(",")] for i in lines]
            modi_lst = list(
                map(
                    lambda lst:
                    lst[0] + ",1" if year - int(lst[second_lst]
                                                [fourth_lst:]) > age
                    else lst[0] + ",0" if year - int(lst[second_lst]
                                                     [fourth_lst:])
                                          == age
                    else lst[0] + ",-1",
                    lst_info))
            header += "\n".join(modi_lst)
    with open(file_out, "w") as fo:
        fo.write(header)


# Question 3
def several_files(files_lst, file_out, min_year):
    """
    change the month in the file list to
    to the first 3 letter of that mouth and
    write it in to file_out file

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
    >>> lst_2 = ['files/info_3.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_3_out.txt', 1980)
    >>> with open('files/several_3_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Sue,San Diego,Mar 19 2015

    >>> lst_2 = ['files/info_2.txt','files/info_3.txt']
    >>> several_files(lst_2, 'files/several_4_out.txt', 1980)
    >>> with open('files/several_4_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989
    Sue,San Diego,Mar 19 2015

    >>> lst_2 = ['files/header.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_5_out.txt', 1980)
    >>> with open('files/several_5_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    """
    header = "name,city,DOB\n"
    second_lst = 2
    month_dict = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
        5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
    out_lst = []
    for fname in files_lst:
        with open(fname, "r") as f:
            lines = f.readlines()[1:]  # skip header
            for line in lines:
                parts = [i.strip() for i in line.split(",")]
                dob = parts[second_lst]
                month, day, year = dob.split("/")
                year = int(year)
                if year >= min_year:
                    new_dob = (month_dict[int(month)]+ " "
                            + day+ " "+ str(year))
                    out_lst.append(parts[0] + "," + parts[1] +
                                   "," + new_dob)
    header += "\n".join(out_lst)
    with open(file_out, "w") as fo:
        fo.write(header)


# Question 4
def postcards(info_list):
    """
    generates postcards as strings only for people with “priority”
     delivery type (case-insensitive). The output must be a dictionary
      with names as keys and postcards as their corresponding values.
      Each postcard should include the following components, all in lowercase:
    The first three letters of the person's first name (if the first
     name has fewer than three letters, use the entire first name)
    The age
    The person's full last name
    A dollar sign ($) followed by the last digit of the price
    The reversed place

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
    >>> postcards(
    ...     ('Mari Noh', 155, 18, 'tram', 'vip'),
    ... )
    Traceback (most recent call last):
    ...
    AssertionError

    >>> postcards([
    ...     ('Mari Noh', 155, 18, 'tram', 'vip'),
    ...     ('Gwen Am', 34, 54, 'Venetian', 'Priority'),
    ...     ['Freya Dog', 34, 1, 'The Strip', 'priority']
    ... ])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> postcards(["a", "b"])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    third_lst = 3
    second_lst = 2
    assert isinstance(info_list, list)
    assert all(list(map(lambda x: True if isinstance(x, tuple)
    else False,info_list)))
    strip_name = lambda x : x[0].split(" ")
    filter_lst = list(filter(lambda x: str.lower(x[-1]) ==
                                       "priority", info_list))
    return dict(map(
        lambda x: (
            x[0] , str.lower(strip_name(x)[0][0:third_lst]
                             + str(x[second_lst])+ strip_name(x)[1]
                             + "$" + str(x[1])[-1]+ x[third_lst][::-1]
                             )), filter_lst
    ))


# Question 5
def win_or_lose(lst, operations):
    """
    apply all the specified outcomes to the list in the given
     order and return the transformed list. Your function should
      execute the operations in order.
    advance: ('advance', amount): Adds amount to each number in a list.
     Returns a list.
    lost:  ('lost', amount): Subtracts amount from each number in a
     list. Returns a list.
    tie: ('tie', threshold): Remove all numbers less than a threshold.
     Returns a list.
    eliminate: ('eliminate', symbol): symbol should be added to the
     output string:
    If a number is positive, return symbol + ‘won’. Otherwise, return
    symbol + 'lost’.
     Returns a list of strings.
    win: ('win', message): message should be added to the output string
    representing the total amount of points. Returns a string.

    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('advance', 5), ('lost', 3), ('tie', 4)]
    >>> win_or_lose(lst, operations_1)
    [14, 125, 1236, 12347, 123458]

    >>> operations_2 = [('lost', 200), ('eliminate', 'Team ')]
    >>> win_or_lose(lst, operations_2)
    ['Team lost', 'Team lost', 'Team lost', 'Team won', 'Team won', 'Team won']

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> operations_3 = (('lost', 200), ('eliminate', 'Team '))
    >>> win_or_lose(lst, operations_3)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> lst2 = 33
    >>> win_or_lose(lst2, operations_1)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> lst3 = [1]
    >>> win_or_lose(lst3, operations_1)
    []
    """
    assert isinstance(lst, list)
    assert isinstance(operations, list)
    # TODO: Fill out the lambda functions as dictionary values
    # Break lines if go past 79 characters
    commands = {
            'advance': lambda lst, amount: list(map(lambda x:
                                                    x + amount, lst)),
            'lost': lambda lst, amount: list(map(lambda x:
                                                 x - amount, lst)),
            'tie': lambda lst, threshold: list(filter
                                               (lambda x:
                                              x >= threshold, lst)),
            'eliminate':  lambda lst, symbol: list(map(lambda x:
                                                       symbol + "won"
            if x > 0 else symbol + "lost", lst)),
            'win': lambda lst, message: message + str(sum(lst)),
    }
    ope_lst = lst
    for i in operations:
        ope_lst = commands[i[0]](ope_lst, i[1])
    return ope_lst
