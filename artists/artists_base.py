# Create base/parent class which all other artist classes/child classes (e.g: drake.py,travis.py ...) will inherit
class ArtistBase:
    def __init__(self, name, genre, top_songs):
        self.name = name
        self.genre = genre
        self.top_songs = top_songs

    #BASIC INFORMATION ABOUT ARTIST(1 line)
    def get_info(self):
        return f"{self.name} is a {self.genre} artist."

    #DETAILED SUMMARY REGARDING ARTIST
    def get_bio(self):
        return (
            f"Artist: {self.name}\n"
            f"Genre: {self.genre}\n"
            f"Top songs: {', '.join(self.top_songs)}"
        )

    #RETURN GENRE(/S) OF MUSIC OF ARTIST
    def get_genre(self):
        return f"Genre: {self.genre}"
    
    #LIST MOST STREAMED SONGS OF ARTIST
    def get_top_songs(self):
        return f"Top songs by {self.name}: {', '.join(self.top_songs)}"

    def respond(self, query):
        query = query.lower()
        if "genre" in query:
            return self.get_genre()
        elif "song" in query:
            return self.get_top_songs()
        elif "info" in query:
            return self.get_info()
        elif "bio" in query:
            return self.get_bio()
        else:
            return f"Sorry, I don’t understand your request about {self.name}."
