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

#https://community.anaplan.com/discussion/155754/part-3-anaplan-audit-history-data-in-an-anaplan-reporting-model
#https://community.anaplan.com/discussion/155744/part-1-enhanced-reporting-of-the-anaplan-audit-log-summary
#https://community.anaplan.com/discussion/155745/part-2-enhancing-anaplan-audit-log-data-extraction-with-a-streamlined-python-solution
