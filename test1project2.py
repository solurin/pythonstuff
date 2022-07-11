from linkedlistproject import *
import sys
import os
import traceback

flights = FlightList()
customers = CustomerList()

flights.addFlight(1234, "Omaha", "Denver", 1200, 95)
flights.addFlight(5567, "Toronto", "Calgary", 800, 360)

customers.addCustomer("Mark", "Buffalo", "1353234532")
customers.addCustomer("Dracula", "Clujnapoca", "666")
customers.addCustomer("Sheila", "Denver", "38463234")
f = flights.find_by_flightnum(1234)
cust = customers.find_by_name("Mark")
f.book(cust, "16A", 3)
cust = customers.find_by_name("Sheila")
f.book(cust, "5B", 2)
f2 = flights.find_by_flightnum(5567)
f2.book(cust, "3A", 1)

flights.print()
customers.print()

f.print_seats()

customers.addCustomer("Ruff", "New York", "1253-2534-2332-5555")
c = customers.find_by_name("Ruff")

f.book(c, "27C", 3)
f.print_seats()

c = customers.find_by_name("Sheila")
f.unbook(c)

f.print_seats()
