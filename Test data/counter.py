# File prints dimesions of csv file

import csv
import sys
reader = csv.reader(open(sys.argv[1],"r"))

#columns
c_data = list(reader.next())
column_count = len(c_data)

#rows
r_data = list(reader)
row_count = len(r_data)

print "rows: ",row_count
print "column: ",column_count