import sys
import re
import csv
from combined_csv import writeCSV
from add_coordinates import getLinesCSV

def get_states():
	return ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def get_lines_from_state (state):
	print "Files/CSV/" + state.replace(" ", "").lower() + "_ll.csv"
	T = []
	try:
		T = getLinesCSV ("Files/CSV/" + state.replace(" ", "").lower() + "_ll.csv")
		return T
	except Exception:
		print "Failed"
		return []

print __name__
if __name__ == "__main__":
	Towns = []
	states = get_states ()
	for state in states:
		T = get_lines_from_state (state)
		for town in T:
			Towns.append (town)
	writeCSV (Towns, "Files/CSV/combined_ll.csv", ["Name", "State", "Date", "Latitude", "Longitude"])