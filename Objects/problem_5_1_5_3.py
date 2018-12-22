

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


def get_song_string(song_object):
    return '"' + song_object.name + '"' + ' - ' + song_object.artist.name + '(' + str(song_object.year) + ')'

newArtist = Artist("Taylor Swift", "Big Machine Records, LLC")
newSong = Song("You Belong With Me", "Fearless", 2008, newArtist)
print(get_song_string(newSong))


