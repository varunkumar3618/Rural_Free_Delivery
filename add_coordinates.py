import csv
from geopy.geocoders import Nominatim
from combined_csv import writeCSV
import sys
#gets lines from a file. each line is a dictionary
def getLinesCSV(s,f="rU"):
	lines = []
	with open(s,f) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			lines.append(row)
	return lines

print __name__
if __name__ == "__main__":
	state = sys.argv[1]
	Towns = getLinesCSV("Files/CSV/" + state.replace(" ", "").lower() + ".csv")
	gl = Nominatim()
	for town in Towns:
		location = gl.geocode(town["Name"] + ", " + town["State"])
		if location:
			print location.address
			[town["Latitude"], town["Longitude"]] = [location.latitude, location.longitude]
		else:
			print "Not found: " + town["Name"] + ", " + town["State"]
			[town["Latitude"], town["Longitude"]] = ["nf", "nf"]

	writeCSV(Towns, "Files/CSV/" + state.replace(" ", "").lower() + "_ll.csv", ["Name", "State", "Date", "Latitude", "Longitude"])
	print "Finished state: " + state