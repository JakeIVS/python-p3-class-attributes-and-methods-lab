class Song:
    
    count = 0
    artists = []
    artist_count = dict()
    genres = []
    genre_count = dict()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.update_genres(self.genre)
        Song.update_artists(self.artist)
    

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def update_genres(cls, genre):
        if not genre in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def update_artists(cls, artist):
        if not artist in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
