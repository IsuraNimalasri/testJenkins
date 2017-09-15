from pymongo import MongoClient
import CutReportMaker as crm
import time
import pandas as pd


#  create mongo client .

client = MongoClient('localhost', 27017)
db = client['blzdb']

# Make CutReport

scd_dates = []
    # get Today
date = (time.strftime("%Y-%m-%d"))
d = map(str, date.split('-'))

# get weekday info
now = time.strftime("%c")
day = (now.split(" "))[0] # get Mon Thu ,Wen or ....

if day == "Fri":
    for i in range(0, 4):
        scd_date = str(d[0]) + "-" + str(d[1]) + "-" + str(int(d[2]) + i)
        scd_dates.append(scd_date)
elif day == "Sat":
    for i in range(0, 3):
        scd_date = str(d[0]) + "-" + str(d[1]) + "-" + str(int(d[2]) + i)
        scd_dates.append(scd_date)
elif day == "Sun":
    for i in range(0, 2):
        scd_date = str(d[0]) + "-" + str(d[1]) + "-" + str(int(d[2]) + i)
        scd_dates.append(scd_date)
else:
    for i in range(0, 2):
        scd_date = str(d[0]) + "-" + str(d[1]) + "-" + str(int(d[2]) + i)
        scd_dates.append(scd_date)

fileName = "cutting_job_report_" + scd_dates[0] + "to" + scd_dates[len(scd_dates) - 1]
print scd_dates
print fileName

# Run CutReport
crm.MakeCutReport(db, scd_dates, fileName)

# df = pd.read_json(fileName)





