from .artists_base import ArtistBase

class Drake(ArtistBase):
    def __init__(self):
        super().__init__(
            "Drake",
            "Hip-Hop, RnB, Pop, Trap",
            ["One Dance ft. Wizkid & Kyla", "God's Plan", "Passionfruit"]
        )