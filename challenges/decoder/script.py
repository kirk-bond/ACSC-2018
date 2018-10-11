import base64
import codecs
import binascii
import random

def encode(string):     #encode with base64
	output = base64.b64encode(bytes(string, 'utf-8')).decode("utf-8")
	scheme = 'base64... <'	
	complete = scheme+output+'>'
#	print(complete)
	return(complete)

def encode32(string):    #encode with base32
	output = base64.b32encode(bytes(string, 'utf-8')).decode("utf-8")
	scheme = 'base32... <'
	complete = scheme+output+'>'
#	print(complete)	
	return(complete)


def reverse(string): #reverse the order of the entire string
	output = string[::-1] 
	scheme = 'reverse... <'
	complete = scheme+output+'>'
#	print(complete)	
	return(complete)

def swap(string):  	#flips upper and lower case
	output = string.swapcase()
	scheme = 'CaseInvert... <'
	complete = scheme+output+'>'
#	print(complete)	
	return(complete)

def rot13(string):	#simpler rotation 13
	output = codecs.encode(string, 'rot_13')
	scheme = 'Rot13... <'
	complete = scheme+output+'>'
#	print(complete)	
	return(complete)



	
string =  "acsc18{ItsOnlySlightlyScrambled}"
f = open("output.txt", "w")
print(string)
f.write(string)
f.write("\n")
output = string
for i in range(1,3):
	selection = random.randint(1,6)
	if selection == 1:
		output = encode(output)
	elif selection == 2:
		output = encode32(output)
	elif selection == 3:
		output = reverse(output)
	elif selection == 4:
		output = swap(output)
	elif selection == 5:
		output = rot13(output)
	f.write(output)
	f.write("\n")

f.write("This is the final output   :    " + output)
f.write("after " + i + " interations")
f.close()
