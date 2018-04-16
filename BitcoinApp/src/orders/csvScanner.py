'''
Created on 16/04/2018

@author: sammagrath
'''

import csv
targetFile  = open('sample_orders.csv', "r")

read = csv.reader(targetFile)
for row in read :
    print (row[7])
        