from .artists_base import ArtistBase

class Future(ArtistBase):
    def __init__(self):
        super().__init__(
            "Future",
            "Trap, Hip-Hop",
            ["Life is Good ft. Drake", "Mask Off", "WAIT FOR U ft. Drake & Tems"]
        )