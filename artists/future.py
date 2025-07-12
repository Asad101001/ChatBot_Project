#Constructor used to create class
class Drake:
    def __init__(self):
        self.name = "Future"
        self.genre = "Hip-Hop, Trap, Mumble Rap"
        self.top_songs = ["Mask Off ", "Life is Good ft. Drake", "Low Life ft. The Weeknd"]

    def get_bio(self):
        return f"{self.name} is a {self.genre} artist.\n \n"

    def respond(self, query):
        return self.get_bio()
    
    #Output objects using either display()/show() method
    def display(self):
        print(f"Artist : {self.name}")
        print(f"Genre : {self.genre}")
        print(f"Top 3 Most streamed songs : {self.top_songs}")