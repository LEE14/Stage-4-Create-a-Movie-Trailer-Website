import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A stroy of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

secret = media.Movie("Secret",
            "A piano prodigy encounters two mysterious students at a college of arts.",
            "https://upload.wikimedia.org/wikipedia/en/c/c6/Secret-Bunengshuodemimi2.jpg",
            "https://www.youtube.com/watch?v=Ceoe2wf-bbo")

a_better_tomorrow = media.Movie("A Better Tomorrow",
                                "A Hong Kong policeman blames his reformed-gangster brother for the death of their father.",
                                "https://upload.wikimedia.org/wikipedia/en/a/af/ABetterTomorrowPosterHK.jpg",
                                "https://www.youtube.com/watch?v=M7ZBsUf986E")

saving_private_ryan = media.Movie("Saving Private Ryan",
                                "Captain John Miller takes his men behind enemy lines to find Private James Ryan.",
                                "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                                "https://www.youtube.com/watch?v=zwhP5b4tD6g")

the_face_reader = media.Movie("The Face Reader",
                            "A Korean face-reader learns of a prince's plan to seize his country's throne.",
                            "https://upload.wikimedia.org/wikipedia/en/f/fb/The_Face_Reader_poster.jpg",
                            "https://www.youtube.com/watch?v=yrCexQHI3Ss")

movies = [toy_story, avatar, secret, a_better_tomorrow, saving_private_ryan, the_face_reader]
fresh_tomatoes.open_movies_page(movies)
