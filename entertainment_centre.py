import media
import freshtomatoes


toy_story = media.Movie(
    "Toy story", "The story of a boy and Toys",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
    "https://www.youtube.com/watch?v=Gzf8CWIfiz0"
    )
# Object for Toy story created

avatar = media.Movie(
    "Avatar", "a story of vietnam colony",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
    )
# Object for Avatar created

true_detective = media.Movie(
    "True Detective", "a story of jaw",
    "https://upload.wikimedia.org/wikipedia/en/5/5a/True_Detective_2014_Intertitle.jpg",
    "https://www.youtube.com/watch?v=mXG1netn9_g"
    )
# Object for True Detective created

mani_chithram = media.Movie(
    "Manichithrathazhu", "a story of a ghost",
    "http://www.whykol.com/wp-content/uploads/2014/10/manichitrathazhu-122.jpg?72f32c",
    "https://www.youtube.com/watch?v=F0P1RzIlRMM"
    )
# object for Manichithram created

friends = media.Movie(
    "Friends", "a story of friends",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Friends_building.jpg/170px-Friends_building.jpg",
    "https://www.youtube.com/watch?v=8mP5xOg7ijs"
    )
# Object for Friends created

inception = media.Movie(
    "Inception", "a story of thieves",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0"
    )
# Object for Inception created

movies = [toy_story, avatar, true_detective, mani_chithram, friends, inception]

freshtomatoes.open_movies_page(movies)
