import os
import syntax_analyzer as syntax
import math

filename ='output.txt'

if os.path.exists(filename):
	open(filename, 'w').close()

pie = math.pi

print("WuGui")

with open("library.txt", "r") as library:
    content = library.read().splitlines()

table = []
dict = {}

for line in content:
	string = line.split()
	dict[string[0]] = string[1]

while True:
	analyzee = input("Please input your input: ")
	flag = 0
	for x in analyzee:
		for y in dict:
			if x in dict:
				flag = 1
			else:
				flag = 0
		if flag==0:
			print("Lexical Not OK")
			break
	if flag==1:
		print("Lexical OK")
		output = syntax.analyze_syntax(analyzee)
		if os.path.exists(filename):
		    append_write = 'a' # append if already exists
		else:
		    append_write = 'w' # make a new file if not
		print(output)

		if output[1][0] == "g":
			print("g")

			value = str(''.join(output[2])).split(",")


			logo = open(filename,append_write)
			# logo.write("Username: " + '\n')

		elif output[1][0] == "c":
			print("c")

			logo = open(filename,append_write)

			logo.write("PU" + '\n')
			logo.write("FD " + ''.join(output[2]) + '\n')
			logo.write("RT 90" + '\n')		
			logo.write("PD" + '\n')		
			logo.write("repeat 180 [FD "+ str((2*pie*int(''.join(output[2])))/180) + " RT 2]" '\n')		
			logo.write("PU" + '\n')
			logo.write("RT 90" + '\n')
			logo.write("FD " + ''.join(output[2]) + '\n')
			logo.write("LT 180" + '\n')
			logo.write("PD" + '\n')

		elif output[1][0] == "r":
			print("r")

			value = str(''.join(output[2])).split(",")

			H = int(value[0])
			W = int(value[1])

			logo = open(filename,append_write)

			logo.write("PU" + '\n')
			logo.write("LT 90" + '\n')
			logo.write("FD "+ str(W/2) + '\n')
			logo.write("RT 90" + '\n')
			logo.write("PD" + '\n')
			logo.write("FD "+ str(H/2) + '\n')
			logo.write("RT 90" + '\n')
			logo.write("FD "+ str(W) + '\n')
			logo.write("RT 90" + '\n')
			logo.write("FD "+ str(H) + '\n')
			logo.write("RT 90" + '\n')
			logo.write("FD "+ str(W) + '\n')
			logo.write("RT 90" + '\n')
			logo.write("FD "+ str(H/2) + '\n')
			logo.write("PU" + '\n')
			logo.write("RT 90" + '\n')
			logo.write("FD "+ str(W/2) + '\n')
			logo.write("LT 90" + '\n')
			logo.write("PD" + '\n')




		elif output[1][0] == "l":
			print("l")

			value = str(''.join(output[2])).split(",")

			L = int(value[0])
			deg = int(value[1])

			logo = open(filename,append_write)

			logo.write("PD" + '\n')
			logo.write("RT 90" + '\n')
			logo.write("LT " + str(deg) + '\n')
			logo.write("FD "+ str(L) + '\n')
			logo.write("LT 180" + '\n')
			logo.write("FD "+ str(L) + '\n')
			logo.write("RT 180" + '\n')
			logo.write("RT " + str(deg) + '\n')
			logo.write("LT 90" + '\n')
			logo.write("PD" + '\n')

		logo.close()