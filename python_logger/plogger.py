import logging  #by default warning se print hota hain 
# logging.debug("this is debug level")
# logging.info("this is info level")
# logging.warning("this is warning level")
# logging.error("this is error level")
# logging.critical("this is critical level")


# level : root_logger = msg

# Logger_File_Path = r"E:\aniket mate\python_logger\first_log.log"
# logging.basicConfig(format = "[%(asctime)s] -%(name)s-%(process)d-[%(levelname)s]--%(message)s",filename=Logger_File_Path, level = logging.DEBUG, datefmt='%d/%b/%y %I:%M:%S')
# name = "Aniket"
# logging.debug(f"{name} this is debug level")
# logging.info('%s before you %s','Look','leap')
# logging.warning("this is warning level")
# logging.error("this is error level")
# logging.critical("this is critical level")
# name = input("Enter your name:-  ")
# try:
#     logging.info("Task Started")
#     logging.debug(f"{name}")
#     inp1 = int(input("Enter first number:-  "))
#     inp2 = int(input("Enter second number:-  "))
#     logging.debug(f"first number:- {inp1}")
#     logging.debug(f"second number:- {inp2}")
#     print(inp1 / inp2)
#     logging.info("Task Ended")

# except Exception as msg:
#     logging.error(msg,exc_info=True)


# testlogger = logging.getLogger(__name__)
# f_handler = logging.FileHandler(Logger_File_Path)
# c_handler = logging.StreamHandler()
# testlogger.setLevel(logging.NOTSET)

# c_format = logging.Formatter( "%(asctime)s--[%(levelname)s]--%(message)s")

# f_format = logging.Formatter( "%(asctime)s--[%(levelname)s]--%(message)s")

# c_handler.setFormatter(c_format)

# f_handler.setFormatter(f_format)

# testlogger.addHandler(f_handler)

# testlogger.addHandler(c_handler)

# testlogger.debug("this is debug level")
# testlogger.info("this is info level")
# testlogger.warning("this is warning level")
# testlogger.error("this is error level")
# testlogger.critical("this is critical level")

# Logger_File_Path = r"E:\aniket mate\python_logger\timedrotatehandler_log.log"
# from logging.handlers import TimedRotatingFileHandler
# # from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# rotate_handler = TimedRotatingFileHandler(Logger_File_Path,when='S',interval=1,backupCount=10)

# rotate_handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter("[%(asctime)s]--%(levelname)s--%(message)s")

# rotate_handler.setFormatter(formatter)

# logger.addHandler(rotate_handler)
# import time
# a = time.time()
# for i in range(1,11):
#     logger.debug("this is debug level")
#     logger.info("this is info level")
#     logger.warning("this is warning level")
#     logger.error("this is error level")
#     logger.critical("this is critical level")
#     time.sleep(1)

# b = time.time()

# print(b-a)

import logging
import logging.config

logging.config.fileConfig(fname=r"E:\aniket mate\python_logger\file_config.txt", disable_existing_loggers=False)

logger = logging.getLogger(__name__)

logger.debug("this is debug level")
logger.info("this is info level")
logger.warning("this is warning level")
logger.error("this is error level")
logger.critical("this is critical level")
