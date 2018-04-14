class Movie():
    """
    Class representing movie
    """

    def __init__(self, title, poster_image_url, trailer):
        """
        Constructor
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer