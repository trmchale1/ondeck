import psycopg2
import sys
import csv

def csv_writer(data, path):
	with open(path, "wb") as csv_file:
		writer = csv.writer(csv_file, delimiter = ' ')
		for line in data:
			writer.writerow(line)


con = None
fout = None
path = "output.csv"

try:
	con = psycopg2.connect("dbname='mydb'")
	cur = con.cursor()
	cur.execute("SELECT * FROM Cars")
	rows = cur.fetchall()

	data = []
	list = []	

	for row in rows:
#		row = list(row)
#		row.pop(0)
		list.append(row)

	print list
	if __name__ == "__main__":
		csv_writer(list, path)

except psycopg2.DatabaseError, e:
	print 'Error %s' % e
	sys.exit(1)

except IOError, e:
	print 'Error %s' % e
	sys.exit(1)

finally:
	if con:
		con.close()
	if fout:
		fout.close()
