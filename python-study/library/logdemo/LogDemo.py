#!usr/bin/env python
#coding:utf-8

import logging

def func1():
    LOG_FILENAME = ".\\log\\log_test.txt"
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    logging.debug("This message should go to log file")

def func2():
    logger=logging.getLogger()
    handler=logging.FileHandler("log_test.txt")
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.error("This is an error message")
    logger.info("This is an info message")
    logger.critical("This is a critical message")
            
def func3():
    logger=logging.getLogger()
    #handler=logging.FileHandler("log_test.txt")
    handler=logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.error("This is an error message")
    logger.info("This is an info message")
    logger.critical("This is a critical message")

class DebugHandler(logging.StreamHandler):
    pass
    def emit(self, record):
        pass
        #None
        logging.StreamHandler.emit(self, record) #if app.debug else None
        
def func4():
    pass
    print dir(logging.StreamHandler)
    #print self
    logger=logging.getLogger()
    #handler=logging.FileHandler("log_test.txt")
    #handler=logging.StreamHandler()
    handler=DebugHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.error("This is an error message")
    logger.info("This is an info message")
    logger.critical("This is a critical message")
    
if __name__ == '__main__':
    #func2()
    #func3()
    func4()
