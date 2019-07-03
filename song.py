class Song:
    """ Class to represent a song

    Attributes:
        title(str): The title of the song
        artist(str): An artist object representing the songs creator.
        duration(int): The duration of the song in seconds. May be Zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        name(str): The name of the album
        year(int): The year was album was released
        artist: (str) : The name of the artist responsible for the album. If not specified,
        the artist will default to an artist with the name "various artist".
        tracks(List(song)): A list of songs on the album

    Methods:
          add_song: Used to add a new song to the album's track list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "various artist"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track List

        Args:
        :param song:(Song): A title of a song to add.
        :param position:(Optional [int]):  It specified, the song will be added to that position
        in the track list = inserting it between other songs if necessary.
        Otherwise, the song will be added to the end of the list.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store artist data.

    Attributes:
        name(str): Name of the artist.
        albums( List[album]): A list of the album by artist.
            The list includes only those albums in this collection, it is not an
            exhaustive list of the artist's publishd albums.

        Methods:
            add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add new album to the albums list.
        Args:
        :param album:Album object to add to the list
            if the album exist, it will not added again this is yet to implemented.
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Add a new song to the collection of albums

        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't already exist.

        Args:
            name(str): The name of the album
            year(int): The year the album wsa produced
            title(str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album" + name)
        album_found.add_song(title)



def find_object(field, object_list):
    """ check object list to see if an abject with a 'name' attribute equal to 'field' exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums.txt", "r")as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_song(album_field, year_field, song_field)
    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
