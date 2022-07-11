#Nick Soluri
# Dr. Meyer CSC 112
# Lab 1 Due 1/23/19




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
			otherstring= str(othernumber)
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






	def subtract(self, othernumber):
		otherstring = ""
		if type(othernumber) is int:
			otherstring= str(othernumber)
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
			column_sum = digit1 - digit2 - carry
			if column_sum >= 10:
				carry = 1
				column_sum %= 10
			else:
				carry = 0
			newstring -= str(column_sum)
		if carry == 1:
			newstring -= "1"
		newstring = newstring[::-1]
		#print(newstring)
		return InfiniteInt(newstring)


		
	def getString(self):
		return self.mystring

	def commaize(self, mystring):
                index = -1
                counter = 0
                revstring = ''
                while counter < len(mystring):
                        revstring = revstring + mystring[index]
                        index -=1
                        counter +=1
                index2 = 0
                commzaizedrevstring = ''
                while index2 < len(mystring):
                        if ((index2 + 1) % 3) != 0:
                                commzaizedrevstring = commzaizedrevstring + revstring[index2]
                                index2 +=1
                        else:
                                commzaizedrevstring = commzaizedrevstring + ','
                                commzaizedrevstring = commzaizedrevstring + revstring[index2]
                 index = -1
                counter = 0
                finalstring = ''
                while counter < len(commaizedrevstring):
                        finalstring = finalstring + commaizedrevstring[index]
                        index -=1
                        counter +=1
		return self.finalstring   #this is just a placeholder!

	def toscientific(self):
		return self.mystring   #this is just a placeholder!
