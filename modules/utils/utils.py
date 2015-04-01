#! /usr/bin/env python

from datetime import datetime, timedelta
import os
import settings

"""
Sends messages to console when debug is enabled.
"""
def log(message):
    if settings.debug:
        print(message)
        
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

def string_to_time(string_time, mask=settings.time_format):
    return datetime.combine(datetime.today(), datetime.strptime(string_time, mask).time())

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
#    h1 = string_to_time(s1, settings.time_format)
#    h2 = string_to_time(s2, settings.time_format)
#    h3 = string_to_time(s3, settings.time_format)
#    h4 = h1 + (h3 - h2) + timedelta(hours=settings.hours_per_day) #<Begin> + (<Return from break> - <Lunch break>) + <Hours per day>
#    
#    print_contents(h1.strftime(settings.date_format), h1.strftime(settings.time_format), 
#                   h2.strftime(settings.time_format), h3.strftime(settings.time_format), 
#                   h4.strftime(settings.time_format))
