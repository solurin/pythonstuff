#Nick Soluri

class LinkedList:
	class Node:
		def __init__(self, payload):
			self.payload = payload
			self.next = None

	def __init__(self):
		self.head = None

	def addNode(self, newpayload, where="end"):
		if self.head == None:
			self.head = LinkedList.Node(newpayload)
			return
		if where == "beginning":
			node = LinkedList.Node(newpayload)
			node.next = self.head
			self.head = node
		elif where == "sorted":
			pass         # insert into list in proper (sorted) ascending order
				   # that is, find two nodes whose payloads "surround" this new
		 		   # payload and insert it after the first node.  If new=42, then
				   # suppose you find 40 and 47, then insert 42 after 40.
		else:    # insert at the end
			node = LinkedList.Node(payload)
			runner = self.head
			while runner.next != None:
                            runner = runner.next
                        runner.next = node

	def print(self):
		runner = self.head
		while runner != None:
			print(runner.payload, id(runner.next), ", ", sep = "", end = "")
			runner = runner.next
		print()

if __name__ == "__main__":
	links = LinkedList()
	links.addNode(26, "beginning")
	links.addNode(99, "beginning")
	links.addNode(127, "end")
	links.addNode(12, "beginning")
	links.addNode(34)    # defaults to end
	links.print()
