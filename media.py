import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, move_title, move_storyline, poster_image, trailer_youtube):
        self.title = move_title
        self.storyline = move_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
