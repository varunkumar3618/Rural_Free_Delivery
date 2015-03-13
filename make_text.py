from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter
import sys
import re
import csv

def writeCSV(Obj, s, fieldnames):
	f_obj = open(s,"wb")
	writer = csv.DictWriter(f_obj, delimiter=',',fieldnames=fieldnames);
	f = dict(zip(fieldnames,fieldnames))
	writer.writerow(f)
	for row in Obj:
		writer.writerow(row)
	f_obj.close()

def get_states():
	return ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def convert_state(state):
	print "Started writing, state: " + state
	ts = "through 1904"
	rep = ["[Text(\'[", "", "]\' {})]", ""]
	flag = 0
	
	filename = "Files/" + state.replace(" ", "").lower() +".rtf"

	try:
		doc = Rtf15Reader.read(open(filename, "rb"))
	except IOError:
		print "Failed"
		return

	plaintext = PlaintextWriter.write(doc).getvalue()

	#remove header and footer
	ind = plaintext.find(ts)
	ind = plaintext.find("\n", ind + 1)
	plaintext = plaintext[ind:]
	plaintext = plaintext.lstrip()

	ind = plaintext.find("\n\n")
	plaintext = plaintext[0:ind]

	#split text into lines
	plaintext = plaintext.split("\n")

	#split line into town and date
	Towns = []
	for line in plaintext:
		m = re.search("\d", line)
		if m:
			ind = m.start()
			Towns.append({"Name" : line[0:ind], "Date" : line[ind:], "State" : state})
		else:
			print "Not found " + line

	#write out csv file
	writeCSV(Towns, "Files/CSV/" + state.replace(" ", "").lower() + ".csv", ["Name", "Date", "State"])
	print "Finished state"

print __name__
if __name__ == "__main__":
	ts = "Dates That First Rural Routes Were Established"
	states = get_states()
	for state in states:
		convert_state(state)
