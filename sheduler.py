import schedule
import time
from Models.Citilink import Citilink
from Models.NotebookSpecs import NotebookSpecs


def another_job():
    print("actually works")


def job_parse_every_day():
    pass


schedule.every().day.at("01:00").do(job_parse_every_day)
schedule.every().minuteh.do(another_job)

while True:
    schedule.run_pending()
    time.sleep(10)