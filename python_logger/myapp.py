import logging
import mylib

def main():
    logging.basicConfig(filename=r"E:\aniket mate\python_logger\myapp_log.log", level = logging.INFO)
    logging.info("started")
    mylib.do_something()
    logging.info("Finished")


if __name__ =='__main__':
    main()