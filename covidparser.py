#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import datetime

#Get the file and feed it to BS4
covidPage = requests.get('https://www.dallascounty.org/departments/dchhs/2019-novel-coronavirus.php')

soup = BeautifulSoup(covidPage.text, 'html.parser')

allTables = soup.find_all("td")
confirmedCases = allTables[6].text
totalDead = allTables[7].text
lengthWithoutAsterisk = len(confirmedCases) - 2;
confirmedCases = confirmedCases[:lengthWithoutAsterisk]

dateTimeVar = datetime.datetime.now()
dateTimeFormatted = dateTimeVar.strftime("%x")

f = open ("/var/www/html/Dallas-County-Covid19-API/CovidList.csv", "a")
f.write(dateTimeFormatted + "," + confirmedCases + "," + totalDead + "\n")
f.close()
