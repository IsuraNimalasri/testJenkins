from pymongo import MongoClient
import CutReportMaker as crm


#  create mongo client .

client = MongoClient('localhost', 27017)
db = client['blzdb']

# Make CutReport

scd_dates = ["2017-09-15"]
crm.MakeCutReport(db,scd_dates,"isura")


#gayan




