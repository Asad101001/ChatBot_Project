#Constructor used to create class
class Drake:
    def __init__(self):
        self.name = "Aubrey 'Drake' Graham"
        self.genre = "Hip-Hop"
        self.top_songs = ["One Dance", "God's Plan", "Passionfruit"]

    def get_bio(self):
        return f"{self.name} is a {self.genre} artist.\n \n"

    def respond(self, query):
        return self.get_bio()
    
    #Output objects using either display()/show() method
    def display(self):
        print(f"Artist : {self.name}")
        print(f"Genre : {self.genre}")
        print(f"Top 3 Most streamed songs : {self.top_songs}")
              
