class InfiniteInt:
	def __init__(self, thestring):
		self.mystring = thestring

	def padout(somestring, n):
		while len(somestring) < n:
			somestring = "0" + somestring
		return somestring

	def add(self, othernumber):
		'''  Add another InfiniteInt onto this one and produce a completely new (a third) InfiniteInt, whose
		    value is the sum of this one and the other number. '''

		otherstring = othernumber.getString()   # get the string rep of the other number
		tempmystring = self.mystring    # get my string rep

		# Now find out which one is longer and pad the shorter one out with zeros so they will be the same length

		len1 = len(tempmystring)           
		len2 = len(otherstring)
		if len1 < len2:
			tempmystring = InfiniteInt.padout(tempmystring, len2)
		elif len1 > len2:
			otherstring = InfiniteInt.padout(otherstring, len1)

		tempmystring = tempmystring[::-1]   # reverse both of them
		otherstring = otherstring[::-1]

		# Now go through the pair of strings and add the numeric value of each digit.  If this is greater than
		# 10, set carry to 1 and subtract 10.  Oh, when adding the 2 digits, add the previous carry in as well.
		#     For example:     "3" + "2" is "5", no carry
		#     But:                   "7" + "6" s "13", so the sum is "3" plus carry is set to 1

		carry = 0
		newstring = ""
		for i in range(len(tempmystring)):
			digit1 = int(tempmystring[i])  # get the integer value of both digits (which are characters)
			digit2 = int(otherstring[i])
			column_sum = digit1 + digit2 + carry   # add these plus the previous carry
			if column_sum >= 10:            # set the new carry and reduce by 10
				carry = 1
				column_sum %= 10
			else:
				carry = 0
			newstring += str(column_sum)    # save the sum as a character
		if carry == 1:     # at the end if there was a carry, append "1"
			newstring += "1"
		newstring = newstring[::-1]    # reverse this so it is in the normal left to right order of MSD to LSD
		return InfiniteInt(newstring)    # create a new InfiniteInt with the result string as its internal rep and return that
		
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