#how to create a CSV file using the CSV python module.

import csv

#content we want written to the the csv file.
clients = [['webserver','singapore'],['azure','North America',],['oracle','Europe']]

with open('eras.csv','w') as myfile:
  result = csv.writer(myfile)
  result.writerows(clients)
