#! /usr/bin/env python

from bs4 import BeautifulSoup

class AhgoraScrapper(object):
    __source = ""
    __scrapper = None
    __table = None
    
    def __init__(self, source=""):
        self.__source = source
        
        self.__scrapper = BeautifulSoup(self.__source)
    
    def appointments_table(self):
        if self.__table is None:
            self.__table = self.__scrapper.find_all("table")[1] #Its the second
            
        return self.__table
    
    def appointment_rows(self):
        tr = self.appointments_table().find_all("tr")
        print(tr)
        rows = []
        for row in tr[2:]:
            cols = row.find_all("td")
            date = cols[0].text.strip()
            appointments = cols[2].text.split(", ") if cols[2].text != "" else []
            rows.append({"date":date, "appointments":appointments})

        return rows