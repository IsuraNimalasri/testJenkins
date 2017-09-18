from pymongo import MongoClient
import CutReportMaker as crm
import time
import pandas as pd


#  create mongo client .

client = MongoClient('localhost', 27777)
# client = MongoClient('localhost', 27017)
db = client['blzdb']

# Make CutReport for given scd dates

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
    for i in range(0, 3):
        scd_date = str(d[0]) + "-" + str(d[1]) + "-" + str(int(d[2]) + i)
        scd_dates.append(scd_date)
nw = now.split(" ")

fileName = scd_dates[0] + "_"+time.strftime('%H-%M') +"_cutting_job_report"
# fileName = "test"
# print scd_dates
# print fileName

# Run CutReport
crm.MakeCutReport(db, scd_dates, fileName)
# csv convter
cjf = fileName+".json"
csvFile = fileName + ".xlsx"
dff = pd.read_json(cjf)
# print dff

dff.to_excel(csvFile)
print scd_dates






