import sys
import Crypto

#python main.py -u Seller360.Support@lumen.com -p Seller360_2

a = sys.path


import sqlite3

import csv
 
# Open the db3 file

conn = sqlite3.connect('audit.db3')
 
# Create a cursor

cur = conn.cursor()
 
# Get the table names

tables = cur.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall()
 
# Iterate over the tables

for table in tables:
 
  # Get the table data

  data = cur.execute('SELECT * FROM {}'.format(table[0])).fetchall()
 
  # Write the data to a csv file

  with open('{}.csv'.format(table[0]), 'w') as f:

    writer = csv.writer(f)

    writer.writerows(data)
 
# Close the connection

conn.close()
