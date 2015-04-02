#! /usr/bin/env python

from flask import Flask, render_template
import jinja2
from modules.utils import settings, utils
from modules.robots.driver import AhgoraDriver
from modules.robots.scrapper import AhgoraScrapper
from modules.utils.utils import log
from modules.utils.stopwatch import StopWatch

app = Flask(__name__, static_folder=settings.ASSETS_PATH, template_folder=settings.TEMPLATE_PATH)

#little hack to make custom template folder works
app.jinja_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader([settings.ASSETS_PATH, settings.TEMPLATE_PATH]),])

@app.route("/")
def index():
    data = {}
    
    watch = StopWatch() #tracking elapsed time
    watch.start()
    driver = AhgoraDriver("460", "460")

    result = driver.login()
    watch.split()
    log("Logged in!" if result else "Login was not possible!")

    if result:
        log("Success! Into Appointment page." if driver.access_appointment_page() else "Could not access appointment page!")
        watch.split()
        
#        log(driver.month())
#        log(driver.name())
        
        scrapper = AhgoraScrapper(driver.source())
        rows = scrapper.appointment_rows()
        
        data["month"] = driver.month()
        data["real_name"] = driver.name().title()
        data["rows"] = rows
        
        watch.split()
        
        driver.close_driver()
        
    watch.stop()
    
#    log(watch.split_list())
    print("Elapsed time: %ss" % (watch.elapsed()))
    
    return render_template("index.tpl", data=data)
