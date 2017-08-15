import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Behavior: initialize the movie instance
        Inputs:
            movie_title         -> title of the movie
            movie_storyline     -> summary of the movie
            poster_image        -> url of the poster image
            trailer_youtube     -> url of the youtube trailer
        Outputs: none
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
