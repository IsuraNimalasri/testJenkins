import pandas as pd
import json
import datetime
import query_node as ra
import Report_Format as rf


def MakeCutReport(db,scd_dates,fileName):
    featchData = db.plan.aggregate(ra.Cutjob(scd_dates))
    fn = str(fileName)+".json"
    CutJobs = []
    df = pd.DataFrame()
    cjobfile = open(fn, 'w')
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
        CutJobs.append(crf)
        cjobfile.write(json.dumps(crf))
        cjobfile.write('\n')
    cjobfile.close()
