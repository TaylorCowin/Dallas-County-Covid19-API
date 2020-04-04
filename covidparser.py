#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import datetime
import os

#Get the file and feed it to BS4
covidPage = requests.get('https://www.dallascounty.org/departments/dchhs/2019-novel-coronavirus.php')

soup = BeautifulSoup(covidPage.text, 'html.parser')

allTables = soup.find_all("td")
confirmedCases = allTables[5].text
confirmedCases = confirmedCases.replace(',','')
totalDead = allTables[6].text
totalDead = totalDead.replace(',','')
lengthWithoutAsterisk = len(confirmedCases) - 2;
confirmedCases = confirmedCases[:lengthWithoutAsterisk]

dateTimeVar = datetime.datetime.now()
dateTimeFormatted = dateTimeVar.strftime("%x")

f = open ("/var/www/html/CovidList.csv", "r+")
allLines = f.readlines()
f.close()
lastLineIndex = len(allLines) - 1
lastLine = allLines[lastLineIndex].split(",")
lastDate = lastLine[0]
lastCases = lastLine[1]
lastDeaths = lastLine[2]

print ('Debug:\n\nDate: ' + dateTimeFormatted + '\nNew Confirmed Cases Value: ' + confirmedCases + '\nNew Deaths Value: ' + totalDead + '\n\nLast Date: ' + lastDate + '\nLast Case Value: ' + lastCases + '\nLast Deaths Value: ' + lastDeaths)

#If different numbers and different dates, add the values and calll the plotter
if (lastCases != confirmedCases and lastDeaths != totalDead):
	print('Debug: Numbers updated on Dallas County Website')
	if (dateTimeFormatted != lastDate):
		print('Debug: New date is different - adding stats')
		f = open ("/var/www/html/CovidList.csv", "a")
		f.write(dateTimeFormatted + "," + confirmedCases + "," + totalDead + "\n")
		f.close()
		os.system('/usr/bin/gnuplot /var/www/html/run_gnuplot.gp')
		print('Debug: Graph successfully updated.')
	else:
		print('Debug: Date is the same. Exiting')
else:
	print('Debug: Numbers are the same. Exiting')
