class InfiniteInt:
	def __init__(self, thestring):
		self.mystring = thestring

	def padout(somestring, n):
		while len(somestring) < n:
			somestring = "0" + somestring
		return somestring

	def add(self, othernumber):
		otherstring = ""
		if type(othernumber) is int:
			otherstring= str(int)
		elif type(othernumber) is str:
			otherstring = othernumber
		elif type(othernumber) is InfiniteInt:
			otherstring = othernumber.getString()
		# now we have two strings (mystring and otherstring)
		tempmystring = self.mystring
		len1 = len(tempmystring)
		len2 = len(otherstring)
		if len1 < len2:
			tempmystring = InfiniteInt.padout(tempmystring, len2)
		elif len1 > len2:
			otherstring = InfiniteInt.padout(otherstring, len1)
		tempmystring = tempmystring[::-1]
		otherstring = otherstring[::-1]
		carry = 0
		newstring = ""
		for i in range(len(tempmystring)):
			digit1 = int(tempmystring[i])
			digit2 = int(otherstring[i])
			column_sum = digit1 + digit2 + carry
			if column_sum >= 10:
				carry = 1
				column_sum %= 10
			else:
				carry = 0
			newstring += str(column_sum)
		if carry == 1:
			newstring += "1"
		newstring = newstring[::-1]
		#print(newstring)
		return InfiniteInt(newstring)
		
	def getString(self):
		return self.mystring

# main code (uses the above class)

n1 = InfiniteInt("81673")
n2 = InfiniteInt("3242")

n3 = n1.add(n2)
print(n3.mystring)

n1 = InfiniteInt("999")
n2 = InfiniteInt("1")

n3 = n1.add(n2)
print(n3.mystring)