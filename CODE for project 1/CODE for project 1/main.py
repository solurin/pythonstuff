from gameworld import *

print(World.make_random_point())

World.advance_year()
print(World.year)

World.new("orc", "Troll1")
World.new("orc", "Gollum")
World.new("orc", "Gnish")
World.new("orc", "Gnash")

World.new("hobbit", "Bilbo")
World.new("hobbit", "Pippin")
World.new("hobbit", "Merry")
World.new("hobbit", "Sam")

World.plot()