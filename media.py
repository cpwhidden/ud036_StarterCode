class Movie():
    """This class contains properties for the display
    of a movie"""

    def __init__(self,
                 movie_title,
                 release_year,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        """ Initializes the movie object"""
        self.title = movie_title
        self.release_year = release_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
