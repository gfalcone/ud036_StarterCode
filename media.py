class Movie():
    """
    Class representing movie
    """

    def __init__(self, title, poster_image_url, trailer):
        """
        Constructor
        :param title (string): title of the movies
        :param poster_image_url (string): url of the poster images
        :param trailer (string): url of the trailer video
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer
