#Constructor used to create class
class Drake:
    def __init__(self):
        self.name = "Aubrey 'Drake' Graham"
        self.genre = "Hip-Hop"
        self.top_songs = ["God's Plan", "Hotline Bling", "Life is Good"]

    def get_bio(self):
        return f"{self.name} is a {self.genre} artist."

    def respond(self, query):
        return self.get_bio()
