#


class Playlist:
    def __init__(self, songs: list) -> None:
        self._songs = songs

    @property
    def songs(self):
        return self._songs

    @songs.setter
    def songs(self, new_songs: list):
        if new_songs == []:
            raise ValueError("Playlist cannot be empty")
        self._songs = new_songs

    def list_song(self):
        return self.songs

    def add_song(self, song_name: str):
        self.songs.append(song_name)
        return self.songs

    def remove_song(self, song_name: str):
        self.songs.remove(song_name)
        return self.songs
