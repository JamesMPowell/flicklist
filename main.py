import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
	<title>FlickList</title>
</head>
<body>
	<h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
	""" Handles requests coming in to '/' (the root of our site)
		e.g. www.flicklist.com/
	"""

	def get(self):

		edit_header = "<h3>Edit My Watchlist</h3>"

		# a form for adding new movies
		add_form =""" 
		<form action="/add" method="post">
			<label>
				I want to add
				<select type="text" name="new-movie">
					<option>Super Troopers</option>
					<option>Tommy Boy</option>
					<option>Black Sheep</option>
					<option>Jay Silent Bob Strike Back</option>
				</select>
				to my watchlist.
			</label>
			<input type="submit" value="Add It"/>
		</form>
		<form action="/crossOff" method="post">
			<label>
				I want to cross off
				<select type="text" name="remove-movie">
					<option>Super Troopers</option>
					<option>Tommy Boy</option>
					<option>Black Sheep</option>
					<option>Jay Silent Bob Strike Back</option>
				</select>
				from my watchlist.
			</label>
			<input type="submit" value="Cross Off"/>
			</form>
		"""

		# TODO 1
		# Include another form so the user can "cross off" a movie from their list.


		# TODO 4 (Extra Credit)
		# modify your form to use a dropdown (<select>) instead a
		# text box (<input type="text"/>)


		content = page_header + edit_header + add_form + page_footer
		self.response.write(content)


class AddMovie(webapp2.RequestHandler):
	""" Handles requests coming in to '/add'
		e.g. www.flicklist.com/add
	"""

	def post(self):
		# look inside the request to figure out what the user typed
		new_movie = self.request.get("new-movie")

		# build response content
		new_movie_element = "<strong>" + new_movie + "</strong>"
		sentence = new_movie_element + " has been added to your Watchlist!"

		content = page_header + "<p>" + sentence + "</p>" + page_footer
		self.response.write(content)


# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".
class CrossOffMovie(webapp2.RequestHandler):
	"""Handles requests coming in to '/crossOff'
	"""
	def post(self):
		# look inside the request to figure out what the user typed
		remove_movie = self.request.get("remove-movie")

		# build response content
		remove_movie_element = "<strike>" + remove_movie + "</strike>"
		sentence = remove_movie_element + " has been crossed off your Watchlist!"

		content = page_header + "<p>" + sentence + "</p>" + page_footer
		self.response.write(content)


# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
	('/', Index),
	('/add', AddMovie),
	('/crossOff', CrossOffMovie)
], debug=True)