import media
import fresh_tomatoes


# Creating movie instances for display

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")



how_to_train_dragon = media.Movie("HowToTrainYourDragon",
                        "A young Viking teenager Hiccup makes friedns with dragons",
                        "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                        "https://www.youtube.com/watch?v=oKiYuIsPxYk")

despicable_me = media.Movie("Despicable Me",
                        "Gru and the minions and three litter girls",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Despicable_Me_Poster.jpg/220px-Despicable_Me_Poster.jpg",
                        "https://www.youtube.com/watch?v=euz-KBBfAAo")

monsters_inc = media.Movie("Monsters, Inc",
                        "Sulley and Mike",
                        "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
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

fresh_tomatoes.open_movies_page(movies)
