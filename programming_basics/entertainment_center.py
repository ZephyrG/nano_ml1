import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")



how_to_train_dragon = media.Movie("How to Train Your Dragon",
                        "A young Viking teenager Hiccup makes friedns with dragons",
                        "https://en.wikipedia.org/wiki/File:How_to_Train_Your_Dragon_Poster.jpg",
                        "https://www.youtube.com/watch?v=oKiYuIsPxYk")

despicable_me = media.Movie("Despicable Me",
                        "Gru and the minions and three litter girls",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Despicable_Me_Poster.jpg/220px-Despicable_Me_Poster.jpg",
                        "https://www.youtube.com/watch?v=euz-KBBfAAo")

monsters_inc = media.Movie("Monsters, Inc",
                        "Sulley and Mike",
                        "https://en.wikipedia.org/wiki/File:Monsters_Inc.JPG",
                        "https://www.youtube.com/watch?v=cvOQeozL4S0")

doraemon = media.Movie("Doraemon",
                        "Blue machine cat",
                        "https://upload.wikimedia.org/wikipedia/en/c/c8/Doraemon_volume_1_cover.jpg",
                        "https://www.youtube.com/watch?v=ghjF37V1cW0")

penguins_madagascar = media.Movie("Penguins of Madagascar",
                        "Cute and cuddly",
                        "https://upload.wikimedia.org/wikipedia/en/5/5f/Penguins_of_Madagascar_poster.jpg",
                        "https://www.youtube.com/watch?v=retX8Wj7JdM")



movies = [toy_story,how_to_train_dragon,despicable_me,monsters_inc, doraemon, penguins_madagascar]
# fresh_tomatoes.open_movies_page(movies)


# print media.Movie.VALID_RATINGS
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__













###
