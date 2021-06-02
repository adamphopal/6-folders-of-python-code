import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
print(toy_story.storyline)


avatar = media.Movie("Avatar",
                     "A marine on  an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
print(avatar.storyline)

the_place = media.Movie("The Place Beyond the Pines",
                     " A motorcycle stunt rider turns to robbing banks as a way to provide for his lover and their newborn child",
                     "https://images.genius.com/13e03b1875bd12032c2e873098c36e92.658x658x1.jpg",
                     "https://www.youtube.com/watch?v=jDcGYFYwDnU")

print(the_place.storyline)

ex_machina = media.Movie("Ex Machina",
                     "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence ",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",
                     "https://www.youtube.com/watch?v=3hAlv0xLJJ4")


kendrick = media.Movie("Kendrick Lamar",
                  "DNA",
                  "http://cache.umusic.com/_sites/kendricklamar.com/images/og.jpg",
                  "https://www.youtube.com/watch?v=NLZRYQMLDW4")







movies = [toy_story, avatar, the_place, ex_machina, kendrick]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)



