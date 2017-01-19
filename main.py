import webapp2
import random 

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
		movies = ['The Matrix','Lethal Weapon','DeadPool','Hell or High Water','Jurassic Park','Forest Gump','The GodFather']
		
        # TODO: randomly choose one of the movies, and return it
		return(random.choice(movies))

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
		
        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"
        self.response.write(content)
		
		# TODO: pick a different random movie, and display it under
        movietwo = self.getRandomMovie()
		
        # build the response string
        contenttwo = "<h1>Tomorrow's Movie</h1>"
        contenttwo += "<p>" + movietwo + "</p>"
        self.response.write(contenttwo)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)