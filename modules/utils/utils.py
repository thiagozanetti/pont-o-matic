#! /usr/bin/env python

from datetime import datetime, timedelta
import os
import settings

"""
Sends messages to console when debug is enabled.
"""
def log(message):
    if settings.DEBUG:
        print(message)
        
def now():
    return datetime.now().strftime(settings.TIME_FORMAT)

def today():
    return datetime.today().strftime(settings.DATE_FORMAT)
        
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

def string_to_datetime(string_time, string_date=datetime.today(), mask=settings.TIME_FORMAT):
    return datetime.combine(string_date, datetime.strptime(string_time, mask).time())

def print_contents(col1, col2, col3, col4, col5):
    print("__________________________________________________")
    print("|            |         |_____ALMOCO______|       |")
    print("|    DATA    | ENTRADA |       |         | SAIDA |")
    print("|            |         |_SAIDA_|_RETORNO_|       |")
    print("|____________|_________|_______|_________|_______|")
    print("|            |         |       |         |       |")
    print("| %s |  %s  | %s |  %s  | %s |" % (col1, col2, col3, col4, col5))
    print("|____________|_________|_______|_________|_______|")
    print("")

#if __name__ == "__main__":
#    s1 = sys.argv[1] #Begin
#    s2 = sys.argv[2] #Lunch break
#    s3 = sys.argv[3] #Return from break
#    try:
#        s4 = sys.argv[4] #Estimative for exit
#    except:
#        pass
#    
#    h1 = string_to_datetime(s1, settings.TIME_FORMAT)
#    h2 = string_to_datetime(s2, settings.TIME_FORMAT)
#    h3 = string_to_datetime(s3, settings.TIME_FORMAT)
#    h4 = h1 + (h3 - h2) + timedelta(hours=settings.HOURS_PER_DAY) #<Begin> + (<Return from break> - <Lunch break>) + <Hours per day>
#    
#    print_contents(h1.strftime(settings.DATE_FORMAT), h1.strftime(settings.TIME_FORMAT), 
#                   h2.strftime(settings.TIME_FORMAT), h3.strftime(settings.TIME_FORMAT), 
#                   h4.strftime(settings.TIME_FORMAT))
