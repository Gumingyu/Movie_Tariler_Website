import webbrowser


class Movie():

    """This class provides a way to store movie related information.
    It allows us to call out the information of many different movies.
    The Movie class holds the fllowing attributes: the title, storyline,
    poster image and trailer of the movie. The data type is string."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
