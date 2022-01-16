class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = [x for x in songs]
        self.published = False

    def add_song(self, new_song):
        if new_song.single:
            return f"Cannot add {new_song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'
        for song in self.songs:
            if song.name == new_song.name:
                return f'Song is already in the album.'
        self.songs.append(new_song)
        return f'Song {new_song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        for sg in self.songs:
            if sg.name == song_name:
                self.songs.remove(sg)
                return f'Removed song {song_name} from album {self.name}.'
        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        output_album = ''
        output_album += f'Album {self.name}\n'
        for song in self.songs:
            output_album += f'== {song.get_info()}\n'
        return output_album
