import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	def __init__(self, movie_title, movie_storyline, poster_image, youtube_url, movie_main_cast, movie_rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_url
		self.cast = movie_main_cast
		self.rating = movie_rating

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

