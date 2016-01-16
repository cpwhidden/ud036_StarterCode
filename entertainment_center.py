import media
import fresh_tomatoes

# Instantiate all movies objects to be shown within the web page
toy_story = media.Movie(
    "Toy Story",
    "1995",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie(
    "Avatar",
    "2009",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=-9ceBgWV8io")

shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "1994",
    "A banker is sentenced to life in prison despite his claims of innocence",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", # NOQA
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

science_of_sleep = media.Movie(
    "The Science of Sleep",
    "2006",
    "A man's vivid dreams and imagination interfere" +
        "with his ability to interact with reality",
    "https://upload.wikimedia.org/wikipedia/en/1/1e/Scienceofsleeppromo.jpg",
    "https://www.youtube.com/watch?v=L0TyuLIfKgU")

# Array of all movies to be shown
movies = [toy_story, avatar, shawshank_redemption, science_of_sleep]

# Create web page from movie data and open it
fresh_tomatoes.open_movies_page(movies)
