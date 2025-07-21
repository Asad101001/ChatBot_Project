class Carti:
          def __init__(self, name, genre):      # __init__ is used as constructor method in Python. Only assignment operations
              self.name = "Playboi Carti"       #self.xxx --> CLASS VARIABLE , = xxx --> INSTANCE/OBJECT VARIABLE
              self.genre = "Hip-Hop/Trap"
              self.top_songs = ["Sky", "Magnolia", "Long Time(intro)"]

          def set(self, name, genre):           #Similar to the constructor method,usually used multiple times in a class
              set.name = "Jordan Carter"        #1 less assignment statement than arguments/parameters in set() fucntion
              set.genre = "Rap"

          def get_bio( self ):                                #This is get() function and can there can be multiple instances of it in class
              return f"{self.name} is a {self.genre} artist." #NEVER contains any argument (other than 'self')
              # return method is better suited than print() followed by class variable --> return self.xxx