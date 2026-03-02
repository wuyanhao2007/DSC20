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
        if self.magic_power > 0:
            self.magic_power -= 1
            self.speed = int(((self.speed + charm_power) ** 2
                          + (self.speed - charm_power) ** 2 ) ** 0.5)
            if self.high_score() >= 2 * prev_score:
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
        if other_broom.size < self.size:
            other_broom.speed -= 50
            self.speed += 50
            if other_broom.speed <= 0:
                other_broom.lives -= 1
                other_broom.speed = 50
                self.size += 1
            return True
        elif other_broom.size > self.size:
            self.speed -= 50
            other_broom.speed += 50
            if self.speed <= 0:
                self.lives -= 1
                self.speed = 50
                other_broom.size += 1
            return False
        else:
            return False

    def high_score(self):
        """
        Formula for high score and returns it.
        """
        return self.speed * 100 + self.lives * 500

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
            other_broom.speed += 50
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
        return self.speed * 200 + self.lives * 300 + 250


# Question 2
# Q2, Part 1
def fix_1(lst1, lst2):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
            out.append(num / div) # add try-catch block
    return out

# Q2, Part 2
def fix_2(*filepaths):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found
    >>> fix_2('docs.txt')
    docs.txt not found
    
    # NO DOCTESTS NEEDED #
    """
    for filepath in filepaths:
        cur_file = open(filepath, "r") # add try-catch block
        cur_file.close()

# Q2, Part 3
def fix_3(lst):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
        sum_of_pairs.append(lst[i] + lst[i + 1]) # add try-catch block
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    return


# Question 4
def load_file(filepath):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    return