"""Model answer"""


class Album:
    """A class representing an album.

    Attributes:
        album_name (str): The name of the album.
        album_artist (str): The artist or band of the album.
        number_of_songs (int): The number of songs in the album.
    """

    def __init__(self, album_name, album_artist, number_of_songs):
        """Initialise an Album object.

        Args:
            album_name (str): The name of the album.
            album_artist (str): The artist or band of the album.
            number_of_songs (int): The number of songs in the album.
        """
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        """Return a string representation of the Album object.

        Returns:
            str: A string representation in the format
                (album_name, album_artist, number_of_songs).
        """
        return (
            f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
        )


def display_albums(albums):
    """Display the contents of a list of albums.

    Args:
        albums (list): The list of Album objects to display.
    """
    for album in albums:
        print(album)


def sort_number_of_songs(albums):
    """Sort a list of albums by number of songs in ascending order
    and display it.

    Args:
        albums (list): The list of Album objects to sort by number of songs.
    """
    albums.sort(key=lambda album: album.number_of_songs)
    print("\nAlbums sorted by number of songs:")
    display_albums(albums)


def swap_positions(albums, position1, position2):
    """Swap two albums in a list based on their positions
    and display the result.

    Args:
        albums (list): The list of Album objects.
        position1 (int): The position of the first album to swap.
        position2 (int): The position of the second album to swap.
    """
    albums[position1 - 1], albums[position2 - 1] = (
        albums[position2 - 1],
        albums[position1 - 1],
    )
    print(f"\nAlbums after swapping positions {position1} and {position2}:")
    display_albums(albums)


def find_index(albums, album_name):
    """Find and display the index of a specific album in a list.

    Args:
        albums (list): The list of Album objects to search.
        album_name (str): The name of the album to find.
    """
    for index, album in enumerate(albums):
        if album.album_name == album_name:
            print(f"\nIndex of '{album_name}' in the list: {index}")


# Example usage:

albums1 = [
    Album("Album1", "Artist1", 12),
    Album("Album2", "Artist2", 18),
    Album("Album3", "Artist3", 16),
    Album("Album4", "Artist4", 10),
    Album("Album5", "Artist5", 20),
]

albums2 = [
    Album("Album6", "Artist6", 14),
    Album("Album7", "Artist7", 15),
    Album("Album8", "Artist8", 17),
    Album("Album9", "Artist9", 11),
    Album("Album10", "Artist10", 13),
]

print("Album 1:")
display_albums(albums1)

sort_number_of_songs(albums1)

swap_positions(albums1, 1, 2)

print("\nAlbum 2:")
display_albums(albums2)

albums2.extend(albums1)
print("\nAlbum 2 after copying Album 1 into it:")
display_albums(albums2)

albums2.extend(
    [
        Album("Dark Side of the Moon", "Pink Floyd", 9),
        Album("Oops!... I Did It Again", "Britney Spears", 16),
    ]
)

albums2.sort(key=lambda album: album.album_name)
print("\nAlbum 2 sorted alphabetically:")
display_albums(albums2)

find_index(albums2, "Dark Side of the Moon")
