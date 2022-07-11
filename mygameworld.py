#Nick Soluri
#Lab Project 1
#Dr. Meyer CSC 112 Lab




import math
import random

class Point:
        '''   Represents on 2D point.  We wrote this in the last lab.
                Creates the framework for the game board by creating instance variables
                which are assigned to integer values which are the parameters.
                These numbers represent points on the board, with x
                representing the horizontal axis and y representing the
                axis, with the intehger values representing either
                horizonal and/or vertical distance from the origin.
                
        '''
        def __init__(self, x, y):
                assert type(x) is int and type(y) is int, "Point's constructor requires 2 ints, the x and y coordinates"
                self.x = x
                self.y = y

        def __str__(self):
                return "(x=" + str(self.x) + ",y=" + str(self.y) + ")"

class World:
        ''' This class contains functions pertaining to the gameworld, and allows users
               to interact with the gameworld in ways such as plotting characters on the
               game board, viewing character stats, and counting the amount of live
               characters. It also allows users to search for certain characters through
               find and find_by_name. This class is fundamental in creating the game board,
               ,and the position values of these characters
               are used in various class methods, such as near_to and move_all_randomly.
        '''
        next_id = 0
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
                if species == "orc":
                        
                        if World.orcs == []:
                                print("there are no orcs!")
                        else:
                
                        
                                for item in World.orcs:
                                        print(item.name, item.id, item.position, item.year_born, item.year_died, item.num_arrows, item.alive)
                if species == "hobbit":
                        

                        if World.hobbits == []:
                                print("there are no hobbits!")
                        else:
                        
                                for item in World.hobbits:
                                        print(item.name, item.id, item.position, item.year_born, item.year_died, item.num_arrows, item.alive)                                
                        
                

        def plot():
                '''  This plots the 21 x 21 world, showing O for Orc and H for hobbit.  The grid lines are drawn, too.
                '''
                plot2 = [['.' for i in range(21)] for k in range(21)]   # fill the 2d array with periods

                for gc in World.orcs:
                        if gc.alive == True:
                                plot2[gc.position.y][gc.position.x] = "O"
                        else:
                                plot2[gc.position.y][gc.position.x] = "X"
                                
                for gc in World.hobbits:
                        if gc.alive == True:
                                plot2[gc.position.y][gc.position.x] = "H"
                        else:
                                plot2[gc.position.y][gc.position.x] = "X"

                for row in range(20,-1,-1):
                        for col in range(0,21):
                                print(plot2[row][col], end="")
                        print()

        def count(species, dead):
                ''' print out the amount of game characters that are alive and how many are dead of the indicated species.'''

                

                assert type(species) is str, "world.count() requires 1st parm be a string"
                assert species in ["orc", "hobbit"], 'world.count() requires species be "orc" or "hobbit"'
                assert type(dead) is bool, "world.count() requires 2nd parameter be a boolean"

                index = 0
                deceased = 0
                alive = 0
                if species == "orc":
                        
                        while index < len(World.orcs):
                                if World.orcs[index].alive == True:
                                        alive +=1
                                        index +=1
                                elif World.orcs[index].alive == False:
                                        deceased +=1
                                        index +=1

                        if dead == True:
                                print(deceased, "orc(s) is/are dead.")

                        if dead == False:

                                print(alive, "orc(s) is/are alive.") 
                                        
                                
                if species == "hobbit":
                        
                        while index < len(World.hobbits):
                                if World.hobbits[index].alive == True:
                                        alive +=1
                                        index +=1
                                elif World.hobbits[index].alive == False:
                                        deceased +=1
                                        index +=1

                        if dead == True:
                                print(deceased, "hobbit(s) is/are dead.")

                        if dead == False:

                                print(alive, "hobbit(s) is/are alive.")





                

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
                ''' makes a random point on the gameboard'''
                return Point(random.randint(0,20), random.randint(0,20))

        def find(my_id):
                '''   This finds a game character (either an orc or a hobbit) whose id is this parameter.
                     It returns a pointer to the gamecharacter.  If there is no character with this id number,
                     return None.
                '''
                
                for i in World.hobbits:
                        if i.id == my_id:
                                return i
                for i in World.orcs:
                        if i.id == my_id:
                                return i

                return None
                
                        

        def find_by_name(name):
                '''  Go through both the orcs and the hobbits list and see if one of the characters has this
                    name.  If so, return that character's id number.  If not found, return -1.
                '''

                
                for item in World.hobbits:
                        if name == item.name:
                                return item.id
                for item in World.orcs:
                        if name == item.name:
                                return item.id

                return -1
                        
                        



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
                ''' moves all randomly'''
                for orc in World.orcs:
                        orc.move_random()
                for hobbit in World.hobbits:
                        hobbit.move_random()

        def populate_randomly():
                ''' populates randomly'''
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
        ''' creates the framework the creation of various game characters. These characters are assigned various attributes
                such as their living status, number of arrows, etc, all of which are assigned as either class or instance variables
                below. Also, a method is found here which is used to find the distance between two characters. This class
                also contains various methods that may be used to move characters around the game board in various ways, and allows
                characters to interact with each other, for example through the kill() function, where one character 'kills' another
                and loses one arrow in the process.
                '''
                
        next_id = 1


        def distance(point1, point2):
                ''' determines distance between two points'''
                x1 = point1.x
                y1 = point1.y
                x2 = point2.x
                y2 = point2.y
                Side1 = (x2 - x1) **2
                Side2 = (y2 - y1) **2

                total = Side1 + Side2
                return math.sqrt(total)
        
        def __init__(self, species, position, name=''):
                World.next_id += 1
                self.species = species
                self.position = position
                self.name = name
                self.year_born = World.year
                self.year_died = 1
                self.id = World.next_id
                self.alive = True
                self.num_arrows = 0
                

        
        def __str__(self):
                if self.species == "hobbit":
                        return "Hobbits " + str(self.id) + " " + "Name: " + self.name + "Year Born:" + str(self.year_born) + "Position: " + str(self.position) + "# of arrows" + str(self.num_arrows)
                else:
                        return "Orcs " +str(self.id) +" " + "Name: " + self.name + "Year Born:" + str(self.year_born) + "Position: " + str(self.position) + "# of arrows" + str(self.num_arrows)

        
        def die(self):
                '''to kill off a game character and change their living status to dead'''
                self.year_died = World.year
                self.alive = False

        def move_right(self, num):
                '''to move a character up on the y axis by adding 1 to their y position value'''
                self.position.x = (self.position.x + num)
                if self.position.x > 20:
                        self.position.x = 20


        def move_left(self, num):
                ''' to move a character down on the y axis by subtracting 1 from their y position value'''
                self.position.x = (self.position.x - num)
                if self.position.x < 0:
                        self.position.x = 0

        def move_down(self, num):
                ''' to move a character left on the x axis by subtracting 1 from their x position value'''
                self.position.y = (self.position.y - num)
                if self.position.y < 0:
                        self.position.y = 0

        def move_up(self, num):
                ''' to move a character right on the x axis 1 by adding 1 to their x position value'''
                assert type(num) is int
                self.position.y = (self.position.y + num)
                if self.position.y > 20:
                        self.position.y = 20

        def near_to(self, other_gc):
                ''' to determine if the magnitude of the vector distance from one character to another is less than (near to each other) or greater than (not near each other) 2'''
                if GameCharacter.distance(self.position, other_gc.position) <= 2:
                        return True
                else:
                        return False
        def kill(self, other_gc):
                ''' to simulate one character killing another by subtracting 1 from their arrows count and changing the other character's alive status to false'''
                if self.num_arrows != 0 and self.species != other_gc.species:
                        self.num_arrows = self.num_arrows - 1
                        other_gc.die()
                        
        def move_random(self):
                ''' to change a character's co-ordinates randomly within a specified realm of possible levels of change'''
                direction = random.randint(1,4)
                points = random.randint(1,2)

                if direction == 1:
                        self.move_up((points))
                if direction == 2:
                        self.move_down((points))
                if direction == 3:
                        self.move_left((points))
                else:
                        self.move_right((points))
        
                                
                




















        

        
#
