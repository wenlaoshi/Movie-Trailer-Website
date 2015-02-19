import fresh_tomatoes
import media

kingsman = media.Movie("Kingsman", 
	"Eggsy lives in a South London housing estate and seems headed for a life behind bars. However, dapper agent Harry Hart recognizes potential in the youth and recruits him to be a trainee in the secret service.", 
	"http://images.hngn.com/data/images/full/44322/kingsman-poster.jpg", 
	"http://youtu.be/kl8F-8tR8to",
	"Colin Firth, Taron Egerton, Samuel L. Jackson",
	4
)

intersteller = media.Movie("Interstellar",
	"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole.",
	"http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",
	"http://youtu.be/0vxOhd4qlnA",
	"Matthew McConaughey, Anne Hathaway, Jessica Chastain",
	4.5
)

imitation_game = media.Movie("The Imitation Game",
	"In 1939, newly created British intelligence agency MI6 recruits Cambridge mathematics alumnus Alan Turing to crack Nazi codes.",
	"http://www.farawayentertainment.com/wp-content/uploads/2015/01/Imitation-Game-Poster.jpg",
	"http://youtu.be/S5CjKEFb-sM",
	"Benedict Cumberbatch, Keira Knightley, Matthew Goode",
	4
)

shades = media.Movie("Fifty Shades of Grey", 
	"When college senior Anastasia Steele steps in for her sick roommate to interview prominent businessman for their campus paper, little does she realize the path her life will take.", 
	"http://assets-s3.usmagazine.com/uploads/assets/articles/69891-fifty-shades-of-grey-first-movie-poster-revealed-features-jamie-dornan-picture-/1390662975_50-shades-of-grey-official-movie-poster_1.jpg", 
	"http://youtu.be/SyEfhP2zrhA",
	"Dakota Johnson, Jamie Dornan, Jennifer Ehle",
	2
)

birdman = media.Movie("Birdman",
	"Former cinema superhero Riggan Thomson is mounting an ambitious Broadway production that he hopes will breathe new life into his stagnant career.",
	"http://upload.wikimedia.org/wikipedia/en/a/a3/Birdman_poster.jpg",
	"http://youtu.be/uJfLoE6hanc",
	"Michael Keaton, Zach Galifianakis, Edward Norton",
	4
)

big_hero = media.Movie("Big Hero 6",
	"Robotics prodigy Hiro lives in the city of San Fransokyo. Hiro's closest companion is Baymax, a robot whose sole purpose is to take care of people.",
	"http://vignette2.wikia.nocookie.net/marvelmovies/images/5/55/Big_Hero_6_poster.jpg/revision/latest?cb=20140611014916",
	"http://youtu.be/bT8qmoCgxZg",
	"Ryan Potter, Scott Adsit, Jamie Chung",
	4
)

sniper = media.Movie("American Sniper",
	"A former boy-genius and a gifted teenager set out on a dangerous mission to unearth the secrets of Tomorrowland, an enigmatic location caught between time and space.",
	"http://ia.media-imdb.com/images/M/MV5BMTkxNzI3ODI4Nl5BMl5BanBnXkFtZTgwMjkwMjY4MjE@._V1_SX640_SY720_.jpg",
	"http://youtu.be/mIvT7nBvQmw",
	"Bradley Cooper, Sienna Miller, Kyle Gallner",
	4
)

movies = [kingsman, intersteller, imitation_game, birdman, big_hero, sniper, shades]
fresh_tomatoes.open_movies_page(movies)

