from multiprocessing import Process, Pool
import csv
from geopy.geocoders import Nominatim
from combined_csv import writeCSV

#list of states
def get_states():
	return ['Alabama']
	#return ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

#gets lines from a file. each line is a dictionary
def getLinesCSV(s,f="rU"):
	lines = []
	try:
		with open(s,f) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				lines.append(row)
	except IOError:
		return None
	return lines

def addCoordinates(state):
	Towns = getLinesCSV("Files/CSV/" + state.replace(" ", "").lower() + ".csv")
	if Towns is None:
		print "Failed: " + state
		return -1
	gl = Nominatim()
	for town in Towns:
		#get location, repeat if connection fails
		for a in range(10):
			try:
				location = gl.geocode(town["Name"] + ", " + town["State"])
				break
			except Exception:
				print "GeocoderTimedOut"
				continue
		else:
			print "Failed on 10 attempts"
			return -1
		if location:
			print location.address
			[town["Latitude"], town["Longitude"]] = [location.latitude, location.longitude]
		else:
			print "Not found: " + town["Name"] + ", " + town["State"]
			[town["Latitude"], town["Longitude"]] = ["nf", "nf"]

	writeCSV(Towns, "Files/CSV/" + state.replace(" ", "").lower() + "_ll.csv", ["Name", "State", "Date", "Latitude", "Longitude"])
	print "Finished state: " + state
	return 1

print __name__
if __name__ == "__main__":
	States = get_states()
	p = Pool(5)
	print (p.map(addCoordinates, States))
	# P = []
	# for state in States:
	# 	p = Process(target=addCoordinates, args=(state,))
	# 	p.start()
	# 	P.append(p)
	# for p in P:
	# 	p.join()