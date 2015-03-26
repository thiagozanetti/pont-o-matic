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

import sys
from datetime import datetime, timedelta

if __name__ == "__main__":

  __time_format = "%H:%M"
  __date_format = "%d/%m/%Y"
  s1 = sys.argv[1]
  s2 = sys.argv[2]
  s3 = sys.argv[3]
  
  h1 = datetime.combine(datetime.today(), datetime.strptime(s1, __time_format).time())
  h2 = datetime.combine(datetime.today(), datetime.strptime(s2, __time_format).time())
  h3 = datetime.combine(datetime.today(), datetime.strptime(s3, __time_format).time())
  h4 = h1 + (h3 - h2) + timedelta(hours=9)
  
  print("__________________________________________________")
  print("|            |         |_____ALMOCO______|       |")
  print("|    DATA    | ENTRADA |       |         | SAIDA |")
  print("|            |         |_SAIDA_|_RETORNO_|       |")
  print("|____________|_________|_______|_________|_______|")
  print("|            |         |       |         |       |")
  
  print("| %s |  %s  | %s |  %s  | %s |" % (h1.strftime(__date_format), h1.strftime(__time_format), 
  h2.strftime(__time_format), h3.strftime(__time_format), h4.strftime(__time_format)))

  print("|____________|_________|_______|_________|_______|")
  print("")
