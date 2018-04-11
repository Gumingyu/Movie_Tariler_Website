import fresh_tomatoes
import media

rudy = media.Movie("Rudy",
                        "Rudy grew up in a steel mill town where most people ended up working, but wanted to play football at Notre Dame instead. There were only a couple of problems. His grades were a little low, his athletic skills were poor, and he was only half the size of the other players. But he had the drive and the spirit of 5 people and has set his sights upon joining the team.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f1/Rudy_%281993_movie_poster%29.jpg",
                        "https://youtu.be/eDKOlH0I0nQ")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on a alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")


#print(avatar.storyline)
#avatar.show_trailer()

godfather = media.Movie("The Godfather",
                        "he aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://youtu.be/sY1S34973zA")

#godfather.show_trailer()
transformers = media.Movie("Transformers",
                           "An ancient struggle between two Cybertronian races, the heroic Autobots and the evil Decepticons, comes to Earth, with a clue to the ultimate power held by a teenager.",
                           "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",
                           "https://youtu.be/sgnO5fO46pE")
the_Shawshank_Redemption = media.Movie("The Shawshank Redemption",
                           "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                           "https://ia.media-imdb.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                           "https://youtu.be/6hB3S9bIaco")

big_hero = media.Movie("Big Hero 6",
                       "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                       "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                       "https://youtu.be/z3biFxZIJOQ")

movies = [rudy, avatar, godfather,transformers, the_Shawshank_Redemption, big_hero]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)


