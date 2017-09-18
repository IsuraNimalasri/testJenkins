import pandas as pd
import json
import datetime
import query_node as ra
import Report_Format as rf
import os


def MakeCutReport(db,scd_dates,fileName):
    # get data from mongoDB
    featchData = db.plan.aggregate(ra.Cutjob(scd_dates))
    # featchData = db.test.aggregate(ra.Cutjob(scd_dates))
    # Make a Json File to write Reported Data
    fn = str(fileName)+".json"
    cjobfile = open(fn, 'w')
    cjobfile.write('[')
    x = 0
    # Mapped featch data with report format
    for doc in featchData:
        crf = rf.CutJOb_Report
        s1 = doc['style']
        s2 = doc['season']
        s3 = doc['sample_type']
        CompletedJobs = doc['completed']
        to_do = doc['todo_job']
        k = doc
        crf['Job_id'] = (doc['job_id']).replace("+", "_")
        crf['Style'] = s1.replace("+", "-")
        crf['Season'] = s2.replace("+", "-")
        crf['Sample_type'] = s3.replace("+", "-")
        crf['Job_card'] = doc['j_id']
        crf['Model_Sheet'] = doc['msheet']
        if (CompletedJobs == []):
            crf['Last_Completed_Job'] = ""
        else:
            crf['Latest_delay_job'] = CompletedJobs[len(CompletedJobs) - 1]
        if (to_do == []):
            crf['On_Going_Job'] = ""
        else:
            crf['On_Going_Job'] = to_do[0]
        crf['GMT_Name'] = doc['GmtName']
        crf['Mearchent_Name'] = doc['mecheName']
        crf['Scd_date'] = doc['scd']
        crf['Scd_Plan'] = doc['scd_plan']
        crf['Production_Plan'] = doc['production_plan']
        crf['ReportedTime'] = long(datetime.datetime.now().strftime("%s")) * 1000
        # print crf
        # cut_job_list.append(crf)
        cjobfile.write(json.dumps(crf))
        cjobfile.write(',')
        cjobfile.write('\n')
        x = x +1
    cjobfile.write('{}')
    cjobfile.write(']')
    cjobfile.close()


