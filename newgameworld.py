


import math


import random

class Point:
	'''   Represents on 2D point.  We wrote this in the last lab.
	'''
	def __init__(self, x, y):
		assert type(x) is int and type(y) is int, "Point's constructor requires 2 ints, the x and y coordinates"
		self.x = x
		self.y = y

	def __str__(self):
		return "(x=" + str(self.x) + ",y=" + str(self.y) + ")"

class World:
	year = 1
	orcs = []
	hobbits = []
	orig_hobbit_names = "Sam,Merry,Pippin,Frodo,Bilbo,Balbo,Mungo,Laura,Rufus,Gorbadoc,Milo,Hildigard,Mirabella,Hamfest,Pansy,Pongo,Largo,Lily," + \
		          "Rudigar,Gerontius,Hildigrim,Marmadoc"
	hobbit_names = orig_hobbit_names.split(",")

	def restart():
		year = 1
		orcs = []
		hobbits = []
		World.hobbit_names = World.orig_hobbit_names.split(",")

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

	def find(id):
		'''   This finds a game character (either an orc or a hobbit) whose id is this parameter.
		     It returns a pointer to the gamecharacter.  If there is no character with this id number,
		     return None.
		'''
		pass

	def find_by_name(name):
		'''  Go through both the orcs and the hobbits list and see if one of the characters has this
		    name.  If so, return that character's id number.  If not found, return -1.
		'''
		pass

	def parse(csv):
                
		'''
		
                        This parses a CSV string to reconstruct a gamecharacter.  It only expects one gamecharacter.
                        If species is orc, it appends to the orc list.  If hobbit, it appends to the hobbits list.
                        
		'''
		
		pieces = csv.split(",")
		gamechar = GameCharacter("", None)    #  can't assume the position or species
		gamechar.species = pieces[0]
		
		gamechar.id_number = int(pieces[1])
		if gamechar.id_number > GameCharacter.next_id:
                        GameCharacter.next_id = gamechar.id_number + 1
		gamechar.name = pieces[2]
		gamechar.position = Point(int(pieces[3]), int(pieces[4]))
		gamechar.year_born = int(pieces[5])
		gamechar.year_died = int(pieces[6])
		gamechar.num_arrows = int(pieces[7])
		gamechar.alive = True if pieces[8] == "True" else False
		if gamechar.species == "orc":
			World.orcs.append(gamechar)
		else:
			World.hobbits.append(gamechar)

	def move_all_randomly():
		for orc in World.orcs:
			orc.move_random()
		for hobbit in World.hobbits:
			hobbit.move_random()

	def populate_randomly():
		n = int(input("How many orcs? "))
		for i in range(n):
			new_name = "orc" + str(random.randint(100000,999999))
			World.new("orc", new_name)
		m = int(input("How many hobbits? "))
		for i in range(m):
			if len(World.hobbit_names) == 0:
				World.hobbit_names = World.orig_hobbit_names.split(",")
			name_index = random.randint(0,len(World.hobbit_names)-1)
			World.new("hobbit", World.hobbit_names[name_index])
			del World.hobbit_names[name_index]

class GameCharacter:
        next_id = 1


        def distance(x1, y1, x2, y2):
                s1 = y2 - y1
                s2 = x2 - x1
                dist = math.sqrt(s2**2 + s1**2)
                return dist
        
        def __init__(self, species, position, name=''):
            
                self.species = species
                self.position = position
                self.name = name
                self.year_born = World.year
                self.year_died = World.year + 1
                self.id = GameCharacter.next_id
                GameCharacter.next_id +=1
                species = ['Hobbit', 'Orc']
                self.species = random.choice(species)
                self.alive = True
                self.position = World.makeRandomPoint
                self.numArrows = 0
                self.posiition = position

        
        def __str__(self):
		s = self.species + "   " + str(self.id_number) + "  name="+self.name+"  born="+str(self.year_born)
		if not self.alive:
			s += "   DEAD!  died on="+str(self.year_died) + "  "
		s += "  position: " + str(self.position)
		s += "  #arrows=" + str(self.num_arrows)
		return s

	
        def die(self):
                GameCharacter.year_died = world.year
                self.alive = False

        def move_up(self, num):
                assert type(num) is int
                self.position.y = self.position.y + num
                if self.position.y > 20:
                        self.position.y = 20


        def move_down(self, num):
                assert type(num) is int
                self.position.y = self.position.y - num
                if self.position.y < 0:
                        self.position.y = 0

        def move_left(self, num):
                assert type(num) is int
                self.position.x = self.position.x - num
                if self.position.x < 0:
                        self.position.x = 0

        def move_right(self, num):
                assert type(num) is int
                self.position.x = self.position.x + num
                if self.position.x > 20:
                        self.position.x = 20

        def near_to(self, GameCharacter(other_gc)):
                if distance(self.position.x, self.position.y, other_gc.position.x, other_gc.position.y) < 2:
                        return True
                else:
                        return False
        def kill(self, GameCharacter(other_gc)):
                assert self.numArrows > 0
                self.numArrows -= 1
                if self.species = hobbit:
                        if other_gc.species = orc:
                                other_gc.die
                else:
                        other_gc.die

        def move_random(self):
                self.position.x = self.position.x + randint(1,2)
                slef.position.y = self.position.y
                        

        
                                
                





















        
	pass   #lots here, including a class variable, a class method and many instance methods
