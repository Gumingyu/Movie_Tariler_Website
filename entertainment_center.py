import fresh_tomatoes
import media

toy_story = media.Movie(
                "Toy Story",
                "A story of a boy and his toys that come to life.",
                "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                "http://www.imdb.com/title/tt0114709/videoplayer/vi2052129305")
# print(toy_story.storyline)

avatar = media.Movie(
        "Avatar",
        "A marine on a alien planet.",
        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/" +
        "Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
        "http://www.imdb.com/title/tt0499549/videoplayer/vi531039513")


# print(avatar.storyline)
# avatar.show_trailer()

godfather = media.Movie(
        "The Godfather",
        "he aging patriarch of an organized crime dynasty transfers" +
        "control of his clandestine empire to his reluctant son.",
        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
        "https://www.imdb.com/title/tt0068646/videoplayer/vi1348706585")

# godfather.show_trailer()
transformers = media.Movie(
        "Transformers",
        "An ancient struggle between two Cybertronian races, the heroic" +
        "Autobots and the evil Decepticons, comes to Earth, with a " +
        "clue to the ultimate power held by a teenager.",
        "https://ia.media-imdb.com/images/M/MV5BNDg1NTU2OWEtM2UzYi00ZWRmLWE" +
        "wMTktZWNjYWQ1NWM1OThjXkEyXkFqcGdeQXVyMTQxNzMzNDI" +
        "@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
        "http://www.imdb.com/title/tt0418279/videoplayer/vi513779993")
the_Shawshank_Redemption = media.Movie(
        "The Shawshank Redemption",
        "Two imprisoned men bond over a number of years, finding " +
        "solace and eventual redemption through acts of common decency.",
        "https://ia.media-imdb.com/images/M/MV5BMDFkYTc0MGEtZmNhMC" +
        "00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        "http://www.imdb.com/title/tt0111161/videoplayer/vi3877612057")

movies = [toy_story, avatar, godfather, transformers, the_Shawshank_Redemption]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
