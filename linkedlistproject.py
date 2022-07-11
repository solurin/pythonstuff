#Nick Soluri
#Project 2 Linked Lists
#Dr. Meyer CSC 112



class CustomerList:
        ''' creates a list of customer nodes. This acts as a linked list which contains each customer node
                and also allows for various operations/searches to be performed, such as finding
                a customer by id number or adding a customer'''
        class CustomerNode:
                ''' holds information for each customer node. This includes name, homecity, creditcard, and id number,
                        which will be assigned to an individual customer '''
                        
                next_id = 1001           # a class variable to make customer_idnumber

                def __init__(self, name, homecity, creditcard):
                        ''' Create a customer node, set the customer_idnumber to 
                           CustomerList.CustomerNode.next_id and then bump that up by 1. '''
                        self.name = name
                        self.homecity = homecity
                        self.creditcard = creditcard
                        self.customer_idnumber = CustomerList.CustomerNode.next_id
                        CustomerList.CustomerNode.next_id +=1
                        self.next = None


                def __str__(self):
                        return str(self.customer_idnumber) + "  " + str( self.name )+ " from " + str(self.homecity )+ "  cc#:  " + str(self.creditcard)


                        
                        

        def __init__(self):
                self.head = None

        def addCustomer(self, newname, homecity, creditcard):
                '''   Create a CustomerNode and attach it to this linked list of customers. '''
                customer = CustomerList.CustomerNode(newname, homecity, creditcard)
                if self.head == None:
                        self.head = customer
                elif customer.name < self.head.name:
                        customer.next = self.head
                        self.head = customer
                else:
                        runner = self.head
                        added = False
                        while runner.next != None and runner.next.name < customer.name:
                                runner = runner.next
                        customer.next = runner.next
                        runner.next = customer

                



                
                
        def find_by_name(self, name_to_find):
                ''' Run through the list of customer nodes and return the one pointer that belongs
                        to the customer with the name 'name_to_find'   If not found, return None. '''
                if self.head == None:
                        return None
                runner = self.head
                while runner != None:
                        if runner.name == name_to_find:
                                return runner
                        runner = runner.next
                return None

        def find_by_id(self, idnum):
                ''' Run through the list of customer nodes and return the one pointer that belongs 
                   to the customer with the customer_idnumber that equals id.
                   If not found, return None. '''
                if self.head == None:
                        return None
                runner = self.head
                while runner != None:
                        id = runner.customer_idnumber
                        
                        if id == idnum:
                                return runner
                        runner = runner.next
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
        ''' this class holds the flights, and acts as a linked list for each seat and flight node
                also, within this class it can be determined if a flight is booked, and a flight can also
                be booked or unbooked '''
        def __init__(self):
                self.head = None

        
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
                        if self.seatlist == None:
                                return None
                        runner = flightptr.seatlist
                        while runner != None:
                                if runner.customer == customerptr:
                                        return runner
                                runner = runner.next
                        return None
                        

                def book(self, customer_ptr, seat, priority_level):
                        ''' Make a new FlightList.SeatNode and fill in with the 3 parameters above.
                           Then attach to the end of the linked list that is pointed to by self.seatlist. '''
                        myseat = FlightList.SeatNode(customer_ptr, seat, priority_level)
                        if self.seatlist == None:
                                self.seatlist = myseat
                        else:
                                runner = self.seatlist
                                while runner.next != None:
                                        runner = runner.next
                                runner.next = myseat
                        

                def unbook(self, customerptr):
                        ''' Remove the seat node whose customer pointer matches customerptr.  If there are no
                           passengers on this flight, then self.seatlist will be None. '''
                        if self.seatlist.customer == customerptr:
                                self.seatlist = self.seatlist.next
                                return
                        
                        runner = self.seatlist
                        while runner != None:
                                if runner.customer == customerptr:
                                        prev.next = runner.next
                                        return
                                prev = runner
                                runner = runner.next
                        runner = None
                        

                def print_seats(self):
                        ''' This prints the manifest for one flight, namely a list of of seat reservations.
                        '''
                        if self.seatlist == None:
                                return None
                        runner = self.seatlist
                        print("------------People booked on flight", self.flight_number, "---------")
                        while runner != None:
                                print(runner.seat_number,": ", runner.customer.name,'            ', runner.priority)
                                runner = runner.next
                        print()

        def __init__(self):
                self.head = None


        def addFlight(self, flightNumber, source, dest, starttime, duration):
                '''   This adds a new flight to the flight list.
                '''
                count = 0
                myflight = FlightList.FlightNode(flightNumber, source, dest, starttime, duration)
                if self.head == None:
                        self.head = myflight
                        return
                runner = self.head
                while runner.next != None:
                        runner = runner.next
                runner.next = myflight
                count += 1

                
                
                        
               

        def find_by_flightnum(self, flightnum):
                '''  This finds the flightnode whose flight_number matches fightnum.
                '''
                if self.head == None:
                        return None
                
                runner = self.head
                while runner != None:
                        if runner.flight_number == flightnum:
                                return runner
                        runner = runner.next
                print("Not Found")
                return None
                        
                                
                        

        def print(self):
                '''   This runs through the list of flight nodes and prints data about each flight.
                '''
                count = 0
                if self.head == None:
                        return None
                runner = self.head
                while runner != None:
                        print("Flight # ",runner.flight_number)
                        print("Source City:     ",runner.source_city)
                        print("Dest City:  ",runner.dest_city )
                        print("Start Time", runner.starttime)
                        print("Duration: ", runner.duration)
                        print()
                        print("    There are customer boooked on this flight" )
                        print()
                        runner = runner.next

                        count += 1
                print(count,"Flight Total" )
                print()
                        
                

if __name__ == "__main__":
        flights = FlightList()
        customers = CustomerList()
