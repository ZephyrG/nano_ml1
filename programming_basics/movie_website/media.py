import webbrowser

class Movie():
    '''
    Store related information for movies
    '''

    def __init__(self,movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    ## open the trail link
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
