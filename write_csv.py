import csv

def csv_writer(data, path):
	with open(path, "wb") as csv_file:
		writer = csv.writer(csv_file, delimiter = ',')
		for line in data:
			writer.writerow(line)

if __name__ == "__main__":
	data = ["first_name,last_name,city".split(","),
		"Tyrese,Hirthe,Strackport".split(","),
		"Jules,Dicki,Lake_Nickolasville".split(","),
		"Dedric,Medhurst,Stiedemannberg".split(",")
		]

path = "output.csv"
csv_writer(data, path)
