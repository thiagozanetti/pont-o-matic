#! /usr/bin/env python

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import modules.utils.settings as settings
from modules.utils.utils import log

class AhgoraDriver(object):
    __driver = webdriver.PhantomJS() #PhantomJS: headless webkit based browser.
    __site_url = "https://www.ahgora.com.br/externo/index/a665612" #Main site url
    __dashboard_url = "https://www.ahgora.com.br/externo/dashboard" #Dashboard page url from where we can access the appointments table
    __appointment_url = "https://www.ahgora.com.br/externo/batidas" #Appointments page url where the table is.
    __id_user = "" #User id
    __pw_user = "" #User password
  
    def __init__(self, id_user, pw_user):
        self.__id_user = id_user
        self.__pw_user = pw_user
        self.__driver.set_window_size(1024, 768) #To make better snapshots :)
    
    """
    Returns a WebdriverWait object with default parameters loaded.
    """
    def wait(self, page_to_wait, driver=__driver, timeout=10):
        result = False
        
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, page_to_wait)))
            
            result = True
        except:
            pass
        
        return result
    
    """
    Takes snapshots from the browser screen
    """
    def snapshot(self, verbose=False):
        if settings.debug:
            snapshot_name = "%s.png" % (datetime.now().strftime("%Y%m%d%H%M%S%f"))
            result = self.__driver.save_screenshot(snapshot_name)

            if verbose:
                log("Snapshot %s successfully taken!" % (snapshot_name) if result else "Could not take the snapshot.")
        else:
            result = False
        
        return result
    
    """
    Retrieves the current URL.
    """
    def current_url(self):
        return self.__driver.current_url
    
    def source(self):
        return self.__driver.page_source
    
    """
    Performs a login into the application
    """
    def login(self):
        match = False
        
        if self.__id_user != "" and self.__pw_user != "":
            self.__driver.get(self.__site_url)

            match = self.current_url() == self.__site_url
            self.snapshot()

            if match:
                form = self.__driver.find_element_by_id("boxLogin")
                form.find_element_by_id("matricula").send_keys(self.__id_user)
                form.find_element_by_id("senha").send_keys(self.__pw_user)

                self.snapshot()

                form.submit()

                self.wait("espelho_ponto_menu")

                match = self.current_url() == self.__dashboard_url
            
        return match

    def access_appointment_page(self):
        log(self.current_url())
        match = self.current_url() == self.__dashboard_url
        self.snapshot()
        
        if match:
            self.__driver.find_element_by_id("espelho_ponto_menu").click()
            self.wait("titulo_mes")

        return match
    
    def month(self):
        log(self.current_url())
        match = self.current_url() == self.__appointment_url
        self.snapshot()
        
        if match:
            result = self.__driver.find_element_by_id("titulo_mes").text
            result = result.split(" ")[4]#.split("/")
        else:
            result = "NO MATCH!"

        return result
    
    def name(self):
        log(self.current_url())
        match = self.current_url() == self.__appointment_url
        self.snapshot()
        
        if match:
            result = self.__driver.find_element_by_class_name(
                "infoUser").find_element_by_class_name(
                "text-primary").text
            
            result = result.split("\n")[0]
        else:
            result = "NO MATCH!"

        return result        
    
    def close_driver(self):
        self.__driver.quit()

if __name__ == "__main__":
    pass
#    ahgora = AhgoraDriver("460", "460")
#    
#    result = ahgora.login()
#    print("Logged in!" if result else "Login was not possible!")
#
#    if result:
#        print("Success! Into Appointment page." if ahgora.access_appointment_page() else "Could not access appointment page!")
#        print(ahgora.month())
#   
#    ahgora.close_driver()
