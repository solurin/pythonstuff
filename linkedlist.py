#Nick Soluri
#Project 2 Linked Lists
#Dr. Meyer CSC 112



class CustomerList:
	class CustomerNode:
		next_id = 1001           # a class variable to make customer_idnumber

		def __init__(self, name, homecity, creditcard):
			''' Create a customer node, set the customer_idnumber to 
			   CustomerList.CustomerNode.next_id and then bump that up by 1. '''
			self.name = name
			self.homecity = city
			self.creditcard = creditcard
			self.customer_idnumber = CustomerList.CustomerNode.next_id
			CustomerList.CustomerNode.next_id +=1





			
			pass

	def __init__(self):
		self.head = None

	def addCustomer(self, newname, homecity, creditcard):
		'''   Create a CustomerNode and attach it to this linked list of customers. '''
		customer = CustomerNode(self, newname, homecity, creditcard)
		CustomerList.head = customer



		
		#runner?
		#compare runner.newname alphabetically
		



		
		pass
        def find_by_name(self, name_to_find):
                
                ''' Run through the list of customer nodes and return the one pointer that belongs
                        to the customer with the name 'name_to_find'   If not found, return None. '''
                if self.head == None:
                        return None
                runner = self.head
                if runner.name == name_to_find:
                        return runner
                elif runner.name != name_to_find:
                        
                        if runner.next != None:
                                runner = runner.next
                        elif runner.next == None:
                                return None
                
                        
                        

	def find_by_id(self, idnum):
		''' Run through the list of customer nodes and return the one pointer that belongs 
		   to the customer with the customer_idnumber that equals id.
		   If not found, return None. '''
                if self.head == None:
                        return None
		runner = self.head
		if runner.customer_idnumber == idnum:
                        return runner
                elif runner.customer_idnumber != idnum:
                        if runner.next != None:
                                runner = runner.next
                        elif runner.next == None:
                                return None
		

	def print(self):
		''' Run through the list of customer nodes and prints out each customer's
		   information. Do not return anything. '''
		if self.head == None:
                        return None
                
                runner = self.head
                while runner.next != None:
                        
                        print(runner.name, runner.homecity, runner.creditcard, runner.customer_idnumber)
                        runner = runner.next
                
                
class FlightList:
	class SeatNode:
		'''
		This describes one reserved seat.  One of the instance variables is a pointer to a customer node
		on the customers list.
		'''
		def __init__(self, customer, seatnumber, priority):
			self.customer = customer  #one of these instance vars is a pointer to a customer node
			self.seat_number = seatnumber
			self.priority = priority
			self.next = None

	class FlightNode:
		'''
		This describes one flight.  Hanging off each flight is a list of SeatNodes.
		'''

		def __init__(self, flightNumber, source, dest, starttime, duration):
			self.flight_number = flightNumber
			self.source_city = source
			self.dest_city = dest
			self.starttime = starttime
			self.duration = duration
			self.seatlist = None
			self.next = None

		def __str__(self):
			return str(self.flight_number) + " from " + self.source_city + " to " + self.dest_city + " starting at " + \
				 str(self.starttime) + " for " + str(self.duration) + " minutes."

		def is_booked(self, flightptr, customerptr):
                        ''' determine if the flight is booked and create a pointer to the customer node'''
                        if self.head == None:
                                return None
                        runner = self.head
                        if runner.customer == customerptr:
                                return runner
                        elif runner.customer != customerptr:
                                if runner.next != None:
                                        runner = runner.next
                                elif runner.next == None:
                                        return None
			

		def book(self, customer_ptr, seat, priority_level):
			''' Make a new FlightList.SeatNode and fill in with the 3 parameters above.
			   Then attach to the end of the linked list that is pointed to by self.seatlist. '''
			FlightNode(customer_ptr, seat, priority_level)
			runner = self.head
			while runner.next != None:
                                runner = runner.next
                        return runner

		def unbook(self, customerptr):
			''' Remove the seat node whose customer pointer matches customerptr.  If there are no
			   passengers on this flight, then self.seatlist will be None. '''
			runner = self.seatlist.head
			while runner.next != None:
                                if runner.customer = customerptr.customer:
                                        runner = None
                                else:
                                        runner = runner.next
			

		def print_seats(self):
			''' This prints the manifest for one flight, namely a list of of seat reservations.
			'''
			runner = self.seatlist.head
			While runner.next != None:
                                print(runner.seatnumber)
                                runner = runner.next
			

	def __init__(self):
		self.head = None

	def addFlight(self, flightNumber, source, dest, starttime, duration):
		'''   This adds a new flight to the flight list.
		'''
                FlightList(flightNumber, source, dest, starttime, duration)

	def find_by_flightnum(self, flightnum):
		'''  This finds the flightnode whose flight_number matches fightnum.
		'''
		runner = self.head
		while runner.next != None:
                        if runner.flight_number == flightnum:
                                return runner
                        else:
                                runner = runner.next

	def print(self):
		'''   This runs through the list of flight nodes and prints data about each flight.
		'''
		runner = self.head
		while runner.next != None:
                        print(FlightList(), self.flight_number, self.source, self.dest, self.starttime, self.duration)
                        runner = runner.next
                

if __name__ == "__main__":
	flights = FlightList()
	customers = CustomerList()
