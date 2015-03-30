#! /usr/bin/env python

from datetime import datetime

class StopWatch(object):
    __split_list = []
    __running = False
    
    def start(self):
        self.__split_list = []
        self.__running = True

        result = datetime.now()
        self.__split_list.append(result)
        
        return result
    
    def split(self):
        result = None
        
        if self.__running:
            result = datetime.now()
            self.__split_list.append(result)

        return result
    
    def stop(self):
        self.__running = False

        result = datetime.now()
        self.__split_list.append(result)

        return result
        
    def elapsed(self):
        last = datetime.now() if self.__running else self.__split_list[-1]
        
        return (last - self.__split_list[0]).seconds
    
    def split_list(self):
        return self.__split_list