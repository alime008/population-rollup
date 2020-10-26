#!/usr/bin/env python

import csv


#initialize list
items=[]
CBSA09=[]
CBSA_T=[]
GEOID=[]
POP00=[]
POP10=[]
PPCHG=[]

#import/input csv file from the directory. Use a list to record everyrow.
with open ('input\censustract-00-10.csv','r') as file:
    my_reader =csv.reader(file, delimiter=',')
    for row in my_reader:
        items.append(row)


#item picker is meant to identify the columns we're interested to look at.
for i in range(1,len(items)):
    CBSA09.append(items[i][7])
    CBSA_T.append(items[i][8])
    GEOID.append(items[i][0])
    POP00.append(items[i][12])
    POP10.append(items[i][14])
    PPCHG.append(items[i][17])

#zip (combine) the columns together to form a similar dataframe.
df=list(zip(CBSA09,CBSA_T,GEOID,POP00,POP10,PPCHG))

# Using sorted and lambda to sort based on the first column.
df = sorted(df, key=lambda x: x[0])

#create seperate lists for each of the interested columns.
CBSA09 = [(row[0]) for row in df]
CBSA_T = [row[1] for row in df]
GEOID = [row[2] for row in df]
POP00 = [int(row[3]) for row in df]
POP10 = [int(row[4]) for row in df]
PPCHG = [(float(row[5].replace(",", "").replace('(X)', "0.00"))) for row in df]


#initialize output and last variable.
output = []
last = None

#create the output zipfile.
for CBSA_ID,CBSA_T,GEO_ID, POP2000, POP2010, POPCHANGE in zip(CBSA09,CBSA_T,GEOID, POP00, POP10, PPCHG):
    if CBSA_ID != last:
        output.append([CBSA_ID, CBSA_T, 0, 0, 0, 0, 0])
        last = CBSA_ID
        ids = set()
        avg_ids = set()
    if GEO_ID not in ids:
        output[-1][2] += 1
        output[-1][3] += POP2000
        output[-1][4] += POP2010
        output[-1][5] += (POPCHANGE)
    output[-1][6]= round(output[-1][5]/output[-1][2], 2)

CBSA09=[]
CBSA_T=[]
GEOID=[]
POP00=[]
POP10=[]
AVGPPCHG=[]

for i in range(0,len(output)):
    CBSA09.append(output[i][0])
    CBSA_T.append(output[i][1])
    GEOID.append(output[i][2])
    POP00.append(output[i][3])
    POP10.append(output[i][4])
    AVGPPCHG.append(output[i][6])

#Create the output file in the output directory.
with open('output\\report.csv', 'w', encoding="ISO-8859-1", newline='') as file:
    wr = csv.writer(file)
    wr.writerows([["CBSA09","CBSA_T","GEOID", "POP00", "POP10", "AVGPPCHG"]])
    wr.writerows(zip(CBSA09,CBSA_T,GEOID,POP00,POP10,AVGPPCHG))
