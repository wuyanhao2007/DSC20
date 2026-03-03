"""
DSC 20 Winter 2026 Homework 08
Name: Yanhao Wu
PID: A19061338
Source: 
"""

def q1_doctests():
    """
    Doctests for Question 1.
    
    >>> broom_1 = FlyingBroom()
    >>> broom_2 = NormalBroom()
    >>> broom_3 = CursedBroom()
    >>> broom_2.boost(20)
    True
    >>> broom_1.duel(broom_2)
    False
    >>> broom_2.high_score()
    9100
    >>> broom_2.duel(broom_3)
    False
    >>> broom_2.speed
    30
    >>> broom_3.high_score()
    25750
    >>> broom_4 = CursedBroom()
    >>> broom_3.duel(broom_4)
    True
    >>> broom_4.size
    7
    >>> broom_4.speed
    20
    >>> broom_3.size
    8
    >>> broom_4.boost(40)
    True
    >>> broom_4.lives
    6
    >>> broom_4.duel(broom_2)
    True
    >>> broom_4.high_score()
    24650
    >>> broom_4.size
    8
    >>> broom_2.speed
    50
    
    
    # ADD DOCTESTS HERE. Do NOT delete this line. #

    >>> fb1 = FlyingBroom()
    >>> fb2 = FlyingBroom()
    >>> fb3 = FlyingBroom()
    >>> fb1.speed, fb1.size, fb1.magic_power, fb1.lives
    (50, 5, 3, 3)
    >>> fb2.set_speed(80)
    >>> fb2.set_size(10)
    >>> fb2.set_lives()
    >>> (fb2.speed, fb2.size, fb2.lives)
    (80, 10, 4)

    >>> nb1 = NormalBroom()
    >>> nb2 = NormalBroom()
    >>> nb3 = NormalBroom()
    >>> nb1.speed, nb1.size
    (50, 5)

    >>> cb1 = CursedBroom()
    >>> cb2 = CursedBroom()
    >>> cb3 = CursedBroom()
    >>> cb1.speed, cb1.size, cb1.magic_power, cb1.lives
    (70, 7, 5, 5)

    >>> b = FlyingBroom()
    >>> b.boost(5)
    True
    >>> b.magic_power
    2

    >>> b2 = FlyingBroom()
    >>> b2.magic_power = 0
    >>> b2.boost(10)
    False

    >>> cb = CursedBroom()
    >>> old_lives = cb.lives
    >>> cb.boost(10)
    True
    >>> cb.lives >= old_lives
    True

    >>> a = FlyingBroom()
    >>> c = CursedBroom()
    >>> a.duel(c)
    False

    >>> c2 = CursedBroom()
    >>> a2 = FlyingBroom()
    >>> c2.duel(a2)
    True

    >>> n = NormalBroom()
    >>> c3 = CursedBroom()
    >>> n.duel(c3)
    False

    >>> fb = FlyingBroom()
    >>> fb.high_score()
    6500

    >>> cb_test = CursedBroom()
    >>> cb_test.high_score()
    15750

    >>> fb.set_speed(60)
    >>> fb.set_lives()
    >>> fb.high_score()
    8000
    """
    return

class FlyingBroom:
    """
    Implementation of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of FlyingBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): current speed of broom, default is 50
        - size (positive int): physical size of broom, default is 5
        - magic_power (non-negative int): number of magic boosts remaining
          for this broom, default is 3
        - lives (non-negative int): number of lives a wizard has while
          flying this broom, default is 3
        """
        self.speed = 50
        self.size = 5
        self.magic_power = 3
        self.lives = 3


    def boost(self, charm_power):
        """
        Boosts the speed of the broom by using a magical
        charm. Speed boost is calculated using the formula
        specified in the write-up. If boost is successfully
        applied (enough magic power to perform boost), return True.
        Otherwise (no remaining magic power to perform boost), return False.
        
        Parameters:
        - charm_power (int): used to calcualte speed boost formula.
          Applied as long the broom still has some magic power
          remaining.
        """
        prev_score = self.high_score()
        square = 2
        root = 0.5
        if self.magic_power > 0:
            self.magic_power -= 1
            self.speed = int(((self.speed + charm_power) ** square
                          + (self.speed - charm_power) ** square ) ** root)
            if self.high_score() >= square * prev_score:
                self.lives += 1
            return True
        return False


    def set_speed(self, new_speed):
        """
        Setter method that assigns given speed value to 
        speed attribute.
        
        Parameters:
        - new_speed (int): new speed value
        """
        self.speed = new_speed

    def set_lives(self, gains = True):
        """
        Setter method that increments lives attribute 
        by 1 if gains is True, otherwise decrement by 1.
        
        Parameters:
        - gains (bool): decides whether to increment/decrement
          lives attribute by 1.
        """
        if gains:
            self.lives += 1
        else:
            self.lives -= 1

    def set_size(self, new_size):
        """
        Setter method that assigns given size value
        (non-negative) to size attribute.
        
        Parameters:
        - new_size (non-negative int): new size value
        """
        self.size = new_size

    def duel(self, other_broom):
        """
        Determines if a duel can occur between
        current broom and other_broom. If so,
        the following happens as specified in
        the write-up. Return True if current
        broom successfully performs duel, otherwise
        False.
        
        Parameters:
        - other_broom (object): Broom object
        """
        speed = 50
        if other_broom.size < self.size:
            other_broom.speed -= speed
            self.speed += speed
            if other_broom.speed <= 0:
                other_broom.lives -= 1
                other_broom.speed = speed
                self.size += 1
            return True
        elif other_broom.size > self.size:
            self.speed -= speed
            other_broom.speed += speed
            if self.speed <= 0:
                self.lives -= 1
                self.speed = speed
                other_broom.size += 1
            return False
        else:
            return False

    def high_score(self):
        """
        Formula for high score and returns it.
        """
        para_one = 100
        para_two = 500
        return self.speed * para_one + self.lives * para_two

class NormalBroom(FlyingBroom):
    """
    Implementation of NormalBroom. Subclass of FlyingBroom.
    """
    def duel(self, other_broom):
        """
        Duel method for NormalBroom.
        - If other_broom is an instance of CursedBroom,
          current NormalBroom loses one life, and its speed 
          resets to 30.
        - CursedBroom object gains a size, and its speed
          increases by 50.
        - Attack is thus considered unsuccessful, function
          returns False.
        - If other_broom is not a CursedBroom object, duel
          method is the same as in the parent class.
        
        Parameters:
        - other_broom (object): Broom object
        """
        if isinstance(other_broom, CursedBroom):
            self.lives -= 1
            self.speed = 30
            speed = 50
            other_broom.speed += speed
            other_broom.size += 1
            return False
        else:
            return super().duel(other_broom)

class CursedBroom(FlyingBroom):
    """
    Implementation of CursedBroom. Subclass of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of CursedBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): default is 70
        - size (positive int): default is 7
        - magic_power (non-negative int): default is 5
        - lives (non-negative int): default is 5
        """
        self.speed = 70
        self.size = 7
        self.magic_power = 5
        self.lives = 5

    def high_score(self):
        """
        Formula for a CursedBroom high score and returns it.
        """
        para_one = 200
        para_two = 300
        para_three = 250
        return (self.speed * para_one + self.lives
                * para_two + para_three)


# Question 2
# Q2, Part 1
def fix_1(lst1, lst2):
    """
    divide each element in lst1 by each element
    in lst2, and append each result to an output list.

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    
    # NO DOCTESTS NEEDED #
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div) # add try-catch block
            except ZeroDivisionError:
                continue
    return out

# Q2, Part 2
def fix_2(*filepaths):
    """
    If we are able to open the file, we should print a
    string '{filepath} opened'. If we are not able to
     open the file, we should print '{filepath} not found'

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found
    >>> fix_2('docs.txt')
    docs.txt not found
    
    # NO DOCTESTS NEEDED #
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r") # add try-catch block
            print(filepath + " opened")
            cur_file.close()
        except FileNotFoundError:
            print(filepath + " not found")


# Q2, Part 3
def fix_3(lst):
    """
    add each element with its following element
     in the list and return all of the summed values
     in a list.


    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []
    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]
    >>> fix_3([])
    []
    
    # NO DOCTESTS NEEDED #
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1]) # add try-catch block
        except IndexError as e:
            print(type(e))
        except TypeError as e:
            print(type(e))
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    Checks (in this order):
    input1 should be a list
    All of the values in input1 should be numeric.
    It is ok if input1 is empty
    If there are multiple non-numeric values, you only
     need to throw an exception for the first non-numeric
     value encountered
    input2 should be numeric
    input2 should be contained in input1


    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'
    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    
    # Add at least 3 doctests below here. Do NOT delete this line. #
    >>> check_inputs([5, 6, 7], 5)
    'Input validated'

    >>> check_inputs([1, 2, 3], 10)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1

    >>> check_inputs([1, 2, None], 1)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    """
    if not isinstance(input1, list):
        raise TypeError("input1 is not the correct type")
    for i, j in enumerate(input1):
        if not isinstance(j, (int, float)):
            raise TypeError(f"The element at index {i} "
                            f"is not numeric")
    if not isinstance(input2, (int, float)):
        raise TypeError("input2 is not the correct type")
    if not input2 in input1:
        raise TypeError("input2 not in input1")
    return "Input validated"



# Question 4
def load_file(filepath):
    """
     checking the correctness of a given filepath and its
      corresponding file

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/ten_words.txt')
    10
    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    
    # Add at least 3 doctests below here. Do NOT delete this line. #
    >>> load_file('files/one_word.txt')
    1

    >>> load_file('files/b.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/b.txt does not exist

    >>> load_file(None)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath is not a string")
    try:
        with open(filepath, "r") as f:
            lines = f.read()
            if len(lines) == 0:
                raise ValueError("File is empty")
            content = lines.strip()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        raise FileNotFoundError(f"{filepath} does not exist")