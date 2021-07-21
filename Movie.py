class Movie(object):
    def __init__(self, title, genres, mpaa_rating, duration, directors, stars):
        self.title = title
        self.genres = genres
        self.mpaa_rating = mpaa_rating
        self.duration = duration
        self.directors = directors
        self.stars = stars



    def __repr__(self):
        return self.title + "|" + ", ".join(self.genres) + "|" + self.mpaa_rating + "|" \
               + self.duration + "|" + ", ".join(self.directors) + "|" + ", ".join(self.stars)+"\n"
