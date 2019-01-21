from ud036_StarterCode import media, fresh_tomatoes

# The favorite movies instances
source_code = media.Movie(
    'Source Code',
    'http://www.impawards.com/2011/posters/source_code_ver2.jpg',
    'https://www.youtube.com/watch?v=mnJegNyAb1w'
)
predestination = media.Movie(
    'Predestination ',
    'http://www.impawards.com/intl/australia/2014/posters/predestination_ver2.jpg',
    'https://www.youtube.com/watch?v=-FcK_UiVV40'
)
triangle = media.Movie(
    'Triangle ',
    'http://www.impawards.com/intl/australia/2009/posters/triangle.jpg',
    'https://www.youtube.com/watch?v=17XqBdCiHOI'
)
the_great_debaters = media.Movie(
    'The Great Debaters',
    'http://www.impawards.com/2007/posters/great_debaters.jpg',
    'https://www.youtube.com/watch?v=IN2AGZThL-8'
)

# The list of the favorite movies
favorite_movies = [
    source_code,
    predestination,
    triangle,
    the_great_debaters,
]

# Create the page that includes the favorite movie page and open it
fresh_tomatoes.open_movies_page(favorite_movies)
