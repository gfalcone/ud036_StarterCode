import media

from fresh_tomatoes import open_movies_page

def display():
    """
    Main function that instantiates 3 movies and
    display them in a webbrowser
    """

    # instantiate movies
    star_wars = media.Movie(
    'Star Wars',
    'https://ia.media-imdb.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,643,1000_AL_.jpg',
    'https://youtu.be/1g3_CFmnU7k'
    )

    bttf = media.Movie(
    'Back to the future',
    'https://ia.media-imdb.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg',
    'https://youtu.be/qvsgGtivCgs'
    )

    bttf4 = media.Movie(
    'Back to the future 4',
    'https://ia.media-imdb.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg',
    'https://youtu.be/Qu2GGUo-Mu0'
    )

    # call open_movies_page with a list of movies
    open_movies_page([star_wars, bttf, bttf4])

if __name__ == '__main__':
    display()
