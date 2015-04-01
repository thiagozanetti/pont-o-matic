#! /usr/bin/env python

from modules.controller import routes
from modules.utils import settings
from modules.robots.driver import AhgoraDriver
from modules.robots.scrapper import AhgoraScrapper
from modules.utils.utils import log
from modules.utils.stopwatch import StopWatch

if __name__ == "__main__":
    routes.app.run(debug=settings.debug)

#    watch = StopWatch() #tracking elapsed time
#    watch.start()
#    driver = AhgoraDriver("460", "460")
#
#    result = driver.login()
#    watch.split()
#    log("Logged in!" if result else "Login was not possible!")
#
#    if result:
#        log("Success! Into Appointment page." if driver.access_appointment_page() else "Could not access appointment page!")
#        watch.split()
#        log(driver.month())
#        log(driver.name())
#        
#        scrapper = AhgoraScrapper(driver.source())
#        log(scrapper.appointment_rows())
#        watch.split()
#        
#    driver.close_driver()
#    watch.stop()
#    
#    log(watch.split_list())
#    print("Elapsed time: %ss" % (watch.elapsed()))
