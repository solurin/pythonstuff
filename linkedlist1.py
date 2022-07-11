class LinkedList:
	class Node:
		def __init__(self, payload):
			self.payload = payload
			self.next = None

	def __init__(self):
		self.head = None

	def addNode(self, newpayload, where="end"):
		newnode = LinkedList.Node(newpayload)
		if self.head == None:
			self.head = newnode
			return
		if where == "beginning":
			newnode.next = self.head
			self.head = newnode
		else:   # at the end
			runner = self.head
			while runner.next != None:
				runner = runner.next
			runner.next = newnode

	def print(self):
		runner = self.head
		while runner != None:
			if runner.next == None:
				print (id(runner), "    payload: ", runner.payload, "   next: None")
			else:
				print(id(runner), "    payload: ", runner.payload, "   next: ", id(runner.next))
			runner = runner.next
		print()

if __name__ == "__main__":
	links = LinkedList()
	links.addNode(26, "beginning")
	links.addNode(99, "beginning")
	links.addNode(127, "end")
	links.addNode(42, "beginning")
	links.addNode(367)
	links.print()