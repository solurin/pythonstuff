from mygameworld import *

World.new("hobbit", "Frodo")
World.new("hobbit", "Sam")
World.display("hobbit")

World.new("orc", "")
World.display("orc")

World.count("orc", False)
o = World.find(3)
o.die()
World.count("orc", True)
World.display("orc")

print("Does Merry exist? ", World.find_by_name("Merry"))

hob1 = World.find(World.find_by_name("Sam"))
hob2 = World.find(World.find_by_name("Frodo"))


hob1.position = Point(5,6)
hob2.position = Point(5,7)

print(hob1.near_to(hob2))

hob2.position = Point(10,15)

print(hob1.near_to(hob2))

print(GameCharacter.distance(hob1.position, hob2.position))

World.new("orc", "Shrak")
World.display("orc")
neworc = World.find(World.find_by_name("Shrak"))

#import sys; sys.exit()

hob1.num_arrows = 5
orc1 = World.find(3)
print(orc1)
neworc.num_arrows = 2
neworc.kill(hob1)
World.display("orc")
World.display("hobbit")

print(hob2)
print("----Now move randomly----")
hob2.move_random()
print(hob2)

hob2.position = Point(5,5)
hob2.move_up(5)
print("----Now move up by 5----")
print(hob2)

hob2.move_down(1)
print("----Now move down by 1----")
print(hob2)

hob2.move_left(1)
print("----Now move left by 1----")
print(hob2)

hob2.move_right(3)
print("----Now move right by 3----")
print(hob2)

hob2.move_right(30)
print("----Now try moving right by 30----")
print(hob2)
