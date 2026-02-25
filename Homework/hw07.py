"""
DSC 20 Fall 2025 Homework 07
Name: Yanhao Wu
PID: A19061338
Source:
"""


# Question 1
def type_with_number(message):
    """
    takes in a string and returns the sequence of digits
     you need to press on your phone, as a string. Your
     function should be case insensitive.

    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'

    # Add at least 3 doctests below here, DO NOT delete this line #
    >>> type_with_number('a')
    '2'
    >>> type_with_number('Z')
    '9'
    >>> type_with_number(' ')
    '0'
    """
    if len(message) == 0:
        return ""
    if message[0].lower() in ",.?!":
        return "1" + type_with_number(message[1:])
    elif message[0].lower() in "abc":
        return "2" + type_with_number(message[1:])
    elif message[0].lower() in "def":
        return "3" + type_with_number(message[1:])
    elif message[0].lower() in "ghi":
        return "4" + type_with_number(message[1:])
    elif message[0].lower() in "jkl":
        return "5" + type_with_number(message[1:])
    elif message[0].lower() in "mno":
        return "6" + type_with_number(message[1:])
    elif message[0].lower() in "pqrs":
        return "7" + type_with_number(message[1:])
    elif message[0].lower() in "tuv":
        return "8" + type_with_number(message[1:])
    elif message[0].lower() in "wxyz":
        return "9" + type_with_number(message[1:])
    elif message[0].lower() in " ":
        return "0" + type_with_number(message[1:])
    return None


# Question 2
def make_palindrome(start, stop):
    """
    create a palindrome and return it as a string.

    >>> make_palindrome(1, 1)
    '1'
    >>> make_palindrome(3, 5)
    '34543'
    >>> make_palindrome(5, 2)
    '5432345'

    # Add at least 3 doctests below here, DO NOT delete this line #
    >>> make_palindrome(2, 2)
    '2'
    >>> make_palindrome(2, 3)
    '232'
    >>> make_palindrome(4, 3)
    '434'
    """
    if start == stop:
        result = str(start)
    elif start < stop:
        result = (str(start) + make_palindrome(start + 1, stop)
                  + str(start))
    else:
        result = (str(start) + make_palindrome(start - 1, stop)
                  + str(start))
    return result


# Question 3
def doctests_q3():
    """
    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Spotify')
    'App installed'
    >>> my_phone.apps
    {'Spotify'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    >>> my_phone.install(1000, 'Spotify')
    'App already installed'

    # Add your own doctests below, DO NOT delete this line #
        >>> p = Phone('Apple', 4000, 64000)
    >>> p.brand
    'Apple'
    >>> p.battery
    4000
    >>> p.charge
    2000
    >>> p.drain_rate
    10
    >>> p.charge_rate
    20
    >>> p.storage
    64000
    >>> p.num_apps
    0
    >>> p.apps
    set()

    >>> p.use(50)
    >>> p.charge
    1500

    >>> p.recharge(10)
    >>> p.charge
    1700

    >>> p.install(1000, 'Maps')
    'App installed'
    >>> p.storage
    63000
    >>> p.num_apps
    1
    >>> p.apps
    {'Maps'}

    >>> p.install(1000, 'Maps')
    'App already installed'

    >>> p.use(1000)
    'Out of charge'
    >>> p.charge
    0

    >>> p.install(500, 'Mail')
    'Out of charge'

    >>> p.recharge(500)
    >>> p.charge
    4000

    >>> p.install(70000, 'Game')
    'Not enough storage'
    """
    return

class Phone:
    """
    Implementation of Phone
    """
    def __init__(self, brand, battery, storage):
        c_rate = 20
        d_rate_apple = 10
        d_rate_oneplus = 12
        d_rate_samsung = 8
        d_rate_else = 15
        self.brand = brand
        self.battery = battery
        self.storage = storage
        self.charge = battery // 2
        self.charge_rate = c_rate
        self.drain_rate = d_rate_apple if brand == "Apple" else d_rate_oneplus \
            if brand == "OnePlus" else d_rate_samsung if brand == "Samsung"\
            else d_rate_else
        self.apps = set()
        self.num_apps = len(self.apps)

    def use(self, minutes):
        if self.charge - minutes * self.drain_rate <= 0:
            self.charge = 0
            return "Out of charge"
        else:
            self.charge -= minutes * self.drain_rate
            return None

    def recharge(self, minutes):
        self.charge += minutes * self.charge_rate
        if self.charge >= self.battery:
            self.charge = self.battery

    def install(self, app_size, app_name):
        if self.charge <= 0:
            return "Out of charge"
        elif self.storage - app_size < 0:
            return "Not enough storage"
        elif app_name in self.apps:
            return "App already installed"
        else:
            self.apps.add(app_name)
            self.num_apps = len(self.apps)
            self.storage -= app_size
            return "App installed"
    pass


################ CLASS PART ##################

# Question 4

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with 1220980 streams
    >>> track1.get_artist()
    'Cordae'
    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'
    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False
    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']
    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759
    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA
    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799
    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'
    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'
    >>> play3 = Playlist('test', 'ab')
    >>> play3.get_most_played_song()
    ''
    >>> play3.get_total_streams()
    0
    >>> play3.get_total_length()
    0
    >>> play3.sort_songs('length')
    >>> play3.songs
    []
    >>> play2.combine_playlists(play3)
    True

    >>> TS = Song('Shake it Off', 1.23, '1989', 'Taylor Swift', 12345)
    >>> BC = Song('Halo', 2.34, 'I Am... Sasha Fierce', 'Beyoncé', 23456)
    >>> JB = Song('Baby', 3.45, 'Okay', 'Justin Bieber', 34567)
    >>> LG = Song('Bad Romance', 4.53, 'Talk You Back', 'Lady Gaga', 45678)
    >>> AG = Song('Side to Side', 1.01, 'Dangerous Woman', 'Ariana Grande', 56432)
    >>> SG = Song('BiggieBig', 3.22, 'The Album', 'Selena Gomez', 987)
    >>> WG = Song('God is Fair', 32.43, 'GOD IS AROUND US', 'Windaco God', 99999999)
    >>> BM = Song('Talking to the Moon', 3.38, 'Doo-Wops & Hooligans', 'Bruno Mars', 2814901)
    >>> NB = Song('Long Song', 99999.99, 'Billy Boy', 'Nobody Billy', 7654321)
    >>> Playlist1 = Playlist('God Spoken!', 'Yes sir')
    >>> Playlist2 = Playlist('Do you still love me if I am DJ', 'Xiaozi')
    >>> Playlist3 = Playlist('Best Song', 'Ye')
    >>> lst = [TS,BC,JB,LG,AG,SG,WG,BM,NB]

    # Add your own doctests below, DO NOT delete this line #
    >>> Playlist1.add_song(TS)
    True
    >>> Playlist1.add_song(BC)
    True
    >>> Playlist1.add_song(JB)
    True
    >>> Playlist1.get_total_streams()
    70368
    >>> Playlist1.get_total_length()
    7.02

    >>> Playlist2.add_song(LG)
    True
    >>> Playlist2.add_song(AG)
    True
    >>> Playlist2.remove_song(LG)
    True
    >>> Playlist2.remove_song(LG)
    False
    >>> Playlist2.get_total_streams()
    56432

    >>> Playlist3.add_song(SG)
    True
    >>> Playlist3.add_song(WG)
    True
    >>> Playlist3.sort_songs('streams')
    >>> [s.get_name() for s in Playlist3.get_songs()]
    ['BiggieBig', 'God is Fair']
    >>> Playlist3.get_most_played_song()
    'God is Fair'

    >>> print(TS.listen())
    Listening to 'Shake it Off' by Taylor Swift
    >>> TS.get_streams()
    12346

    >>> SG.add_to_playlist(Playlist1)
    True
    >>> SG.add_to_playlist(Playlist1)
    False
    """
    return


class Song:
    """
    Implementation of a song
    """
    platform = "Spotify"

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song
        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        self.name = name
        self.length = length
        self.album = album
        self.artist = artist
        self.streams = streams
        pass


    def get_name(self):
        """ Getter for name attribute """
        return self.name


    def get_length(self):
        """ Getter for length attribute """
        return self.length


    def get_album(self):
        """ Getter for album attribute """
        return self.album


    def get_artist(self):
        """ Getter for artist attribute """
        return self.artist


    def get_streams(self):
        """ Getter for streams attribute """
        return self.streams


    def __str__(self):
        """
        String representation of Song
        """
        return (f"'{self.name}' by {self.artist} on '{self.album}' "
                f"is {self.length} minutes long with "
                f"{self.streams} streams")


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        self.streams += 1
        return f"Listening to '{self.name}' by {self.artist}"


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(playlist, Playlist)
        return playlist.add_song(self)

# Question 5

class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist
        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist
        Attributes:
        songs (list): list used to store songs in playlist
        """
        self.title = title
        self.user = user
        self.songs = []
        pass


    def get_title(self):
        """ Getter for title attribute """
        return self.title


    def get_user(self):
        """ Getter for user attribute """
        return self.user
    

    def get_songs(self):
        """ Getter for songs attribute """
        return self.songs


    def __str__(self):
        """
        String representation of Playlist
        """
        return (f"Playlist '{self.title}' by "
                f"{self.user} has {len(self.songs)} songs")


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(song, Song)
        if song in self.songs:
            return False
        self.songs.append(song)
        return True


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        assert isinstance(song, Song)
        if song in self.songs:
            self.songs.remove(song)
            return True
        else:
            return False


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        assert isinstance(sort_by, str)
        self.songs.sort(key = lambda song: getattr(song, sort_by))



    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        return sum([song.get_streams() for song in self.songs])


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        return sum([song.get_length() for song in self.songs])


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that records all the songs played.
        If the playlist is empty, return "Empty"
        """
        if len(self.songs) <= 0:
            return "Empty"
        else:
            result = []
            for song in self.songs:
                result.append(song.listen())
            return "\n".join(result)


    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        assert isinstance(other_playlist, Playlist)
        assert all([isinstance(song, Song) for song in other_playlist.songs])
        new_plst = [self.add_song(song) for song in other_playlist.songs]
        if all(new_plst):
            return True
        else:
            return new_plst.count(False)
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        max_stream = 0
        max_name = ""
        for song in self.songs:
            if song.get_streams() > max_stream:
                max_stream = song.get_streams()
                max_name = song.get_name()
        return max_name