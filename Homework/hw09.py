"""
DSC 20 Winter 2026 Homework 09
Name: Yanhao Wu
PID: A19061338
Source:
"""

# Question 1
def question_1():
    """
    1 if a method mutates an object 
	0 otherwise

	>>> answer = question_1()
	>>> len(answer) == 10
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer])
	False
    """
    return [0, 0, 0, 1, 1, 0, 0, 1, 0, 1]


# Question 2
def question_2():
    """
    1 if a method is in place
	0 otherwise

	>>> answer = question_2()
	>>> len(answer)==5
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer ])
	False
    """
    return [1, 1, 1, 1, 1]


# Question 3
def reverse_list(lst):
    """ 
    reverse the list without creating a new list


    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE. #
    >>> x = [1, 2]
    >>> reverse_list(x)
    >>> x
    [2, 1]
    >>> x = [7, 8, 9]
    >>> reverse_list(x)
    >>> x
    [9, 8, 7]
    >>> x = [10, 20, 30, 40]
    >>> reverse_list(x)
    >>> x
    [40, 30, 20, 10]
    """
    demo = 2
    for i in range(len(lst) // demo):
        temp = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst) -1- i] = temp



# Question 4
def swap_lists(alist1, alist2):
    """
   swap two lists without creating a new list

    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]

    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE. #
    >>> list1 = [5]
    >>> list2 = [9]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [9]
    >>> print(list2)
    [5]

    >>> list1 = [1, 1]
    >>> list2 = [2, 2]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [2, 2]
    >>> print(list2)
    [1, 1]

    >>> list1 = [7, 8, 9]
    >>> list2 = [1, 2, 3]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [1, 2, 3]
    >>> print(list2)
    [7, 8, 9]
    """
    for i in range(len(alist1)):
        for j in range(len(alist2)):
            temp = alist1[i]
            alist1[i] = alist2[len(alist2) - 1 - j]
            alist2[len(alist2) - 1 - j] = temp