import math
import random

class Point:
	
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def __str__(self):
                return str(self.x) + "," + str(self.y)

class World:
	year = 1
	orcs = []
	hobbits = []

	def advance_year():
		'''  Advance the year by 1 '''
		World.year += 1

	def display(species):
		'''  Print the details of the indicated species.  Use either the orcs list or the hobbits list. 
		    If there are 0 game characters in a list, say so.  If there is 1 or more, print out the number
		    of characters in the list and then details of each one.
		'''
		assert type(species) is str, "world.display() requires 1st parm be a string"
		assert species in ["orc", "hobbit"], 'world.display() requires species be "orc" or "hobbit"'
		pass

	def plot():
		'''  This plots the 21 x 21 world, showing O for Orc and H for hobbit.  The grid lines are drawn, too.
		'''
		plot = [['.' for i in range(21)] for k in range(21)]   # fill the 2d array with periods

		for gc in World.orcs:
			plot[gc.position.x][gc.position.y] = "O"
		for gc in World.hobbits:
			plot[gc.position.x][gc.position.y] = "H"

		for row in range(20,-1,-1):
			for col in range(0,21):
				print(plot[row][col], end="")
			print()

	def count(species, dead):
		assert type(species) is str, "world.count() requires 1st parm be a string"
		assert species in ["orc", "hobbit"], 'world.count() requires species be "orc" or "hobbit"'
		assert type(dead) is bool, "world.count() requires 2nd parameter be a boolean"
		pass

	def battle():
		'''   The biggest, most important method of the bunch! '''
		pass

	def new(species, name):
		assert type(species) is str, "world.new() requires 1st parm be a string"
		assert species in ["orc", "hobbit"], 'world.new() requires species be "orc" or "hobbit"'
		gc = GameCharacter(species, World.make_random_point(), name)
		if species == "orc":
			World.orcs.append(gc)
		else:
			World.hobbits.append(gc)

	def make_random_point():
		return Point(random.randint(0,20), random.randint(0,20))


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
        
        
