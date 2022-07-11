#Nick Soluri
#eventually paste into gameworld.py


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + "," + str(self.y)
### don't include below in gameworld
if __name__ == "__main__":
    
    point1 = Point(1,2)
    print(point1)


class GameCharacter:
    next_id = 1
    def __init__(self, species, position, name=''):
        self.species = species
        self.position = position
        self.name = name
        self.year_born = World.year
        self.year_died = World.year - 1
        self.id = GameCharacter.next_id
        GameCharacter.next_id +=1
        
        
