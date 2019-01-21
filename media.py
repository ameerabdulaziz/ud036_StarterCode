class Movie:
    """The movie detail that shares with all the movies"""
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """The main attributes of every movie"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
