from .artists_base import ArtistBase

class Travis(ArtistBase):
    def __init__(self):
        super().__init__(
            "Travis Scott",
            "Hip-Hop, Trap, Psychedelic Rap",
            ["goosebumps ft. Kendrick Lamar", "SICKO MODE ft. Drake",  "Highest in the Room"]
        )