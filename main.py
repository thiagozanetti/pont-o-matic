#! /usr/bin/env python

"""

Usage: 
    $ python ponto.py <HORA_ENTRADA> <HORA_SAIDA_ALMOCO> <HORA_RETORNO_ALMOCO>

Ex:
    $ python ponto.py 09:00 11:45 12:45

Result:
    __________________________________________________
    |            |         |_____ALMOCO______|       |
    |    DATA    | ENTRADA |       |         | SAIDA |
    |            |         |_SAIDA_|_RETORNO_|       |
    |____________|_________|_______|_________|_______|
    |            |         |       |         |       |
    | 25/03/2015 |  09:00  | 11:45 |  12:45  | 19:00 |
    |____________|_________|_______|_________|_______|

"""

import sys, os
from datetime import datetime, timedelta
from modules.robots.driver import AhgoraDriver
from modules.robots.scrapper import AhgoraScrapper

#sys.path.insert(0, os.path.join(base_dir, os.path.dirname(__file__)))

__time_format = "%H:%M"
__date_format = "%d/%m/%Y"
__hours_per_day = 9

def __string_to_time(string_time, mask=__time_format):
    return datetime.combine(datetime.today(), datetime.strptime(string_time, mask).time())

def __print_contents(col1, col2, col3, col4, col5):
    print("__________________________________________________")
    print("|            |         |_____ALMOCO______|       |")
    print("|    DATA    | ENTRADA |       |         | SAIDA |")
    print("|            |         |_SAIDA_|_RETORNO_|       |")
    print("|____________|_________|_______|_________|_______|")
    print("|            |         |       |         |       |")
    print("| %s |  %s  | %s |  %s  | %s |" % (col1, col2, col3, col4, col5))
    print("|____________|_________|_______|_________|_______|")
    print("")
    
if __name__ == "__main__":
    driver = AhgoraDriver("460", "460")
#    driver = AhgoraDriver("", "")
    
    result = driver.login()
    print("Logged in!" if result else "Login was not possible!")

    if result:
        print("Success! Into Appointment page." if driver.access_appointment_page() else "Could not access appointment page!")
        print(driver.month())
        print(driver.name())
        
        scrapper = AhgoraScrapper(driver.source())
#        print(scrapper.appointments_table())
        print(scrapper.appointment_rows())
        
    driver.close_driver()

#    s1 = sys.argv[1] #Begin
#    s2 = sys.argv[2] #Lunch break
#    s3 = sys.argv[3] #Return from break
#    try:
#        s4 = sys.argv[4] #Estimative for exit
#    except:
#        pass
#    
#    h1 = __string_to_time(s1, __time_format)
#    h2 = __string_to_time(s2, __time_format)
#    h3 = __string_to_time(s3, __time_format)
#    h4 = h1 + (h3 - h2) + timedelta(hours=__hours_per_day) #<Begin> + (<Return from break> - <Lunch break>) + <Hours per day>
#    
#    __print_contents(h1.strftime(__date_format), h1.strftime(__time_format), 
#                     h2.strftime(__time_format), h3.strftime(__time_format), 
#                     h4.strftime(__time_format))
