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
totalDead = allTables[6].text
lengthWithoutAsterisk = len(confirmedCases) - 2;
confirmedCases = confirmedCases[:lengthWithoutAsterisk]
print (allTables)
print (confirmedCases)
print (totalDead)
