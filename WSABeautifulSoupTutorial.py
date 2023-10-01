#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:20:06 2023

@author: abhiattaluri
"""

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    
    url = requests.get("https://www.nfl.com/stats/player-stats/")
    soup = BeautifulSoup(url.text, 'html.parser')
    #print(soup)
    
    statsTable = soup.find("div", attrs = {'class' : 'd3-o-table--horizontal-scroll'}).find('table')
    #print(statsTable)
    
    tableRows = soup.find_all("tr")
    #print(tableRows)
    #print(tableRows[1])
    
    #indexes for 1st row of player info and beyond
    for row in tableRows[1:]:
        
        #print(row)
        #print("------------")
        
        columns = row.find_all('td')
        
        playerName = columns[0].text
        passYds = int(columns[1].text)
        completionPerc = float(columns[5].text)
        touchdowns = int(columns[6].text)
        interceptions = int(columns[7].text)
        sacks = int(columns[14].text)
        
        playerStats = [playerName, passYds, completionPerc, touchdowns, interceptions, sacks]
        print(playerStats)
        
        
        
    
    


