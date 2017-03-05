import csv
import sys
reader = csv.reader(open(sys.argv[1],"r"))
data = list(reader.next())
row_count = len(data)

print row_count