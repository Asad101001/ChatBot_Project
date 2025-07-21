from artists.carti import Carti
from artists.drake import Drake

#Object creation (the 'new' keyword isn't conventionally present in Python)
drake = Drake()

#Child function and its functionality testing
print(drake.get_bio())       # Calling child function get_bio()

#Output objects using either display()/show() method
drake.display()

#Creating second object this time by using class along with arguments
carti = Carti("Playboi Carti", "Hip-Hop/Trap")
print(carti.get_bio())

