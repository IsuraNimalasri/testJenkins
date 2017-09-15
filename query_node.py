
#  CutJob
def Cutjob(Date):
    CuttingJobPipline = [{"$match":{"tenant_id" : "mas-nirmaana","factory_id":"nirmaana",
    "planname":{"$exists":True,"$in":["production_plan","scd_plan"]},
  "plan_details.plan_dates.scd":{"$exists":True,"$in":Date},
  # "task_profile.style":{"$exists":True,"$in":[]}
# //  "task_profile.style":{"$exists":True,"$regex":/CW10.*/i}
  }},
{
"$project":{
"job_id":{"$concat":["$task_profile.style","---","$task_profile.season","---","$task_profile.sample_type"]},
"ssd" : "$plan_details.plan_dates.ssd",
"scd" : "$plan_details.plan_dates.scd",
"style": "$task_profile.style",
"season": "$task_profile.season",
"sample_type": "$task_profile.sample_type",
"todo_job" : "$todo_job_functions",
"upcoming_job" : "$upcomming_functions",
"j_id" : {"$ifNull":["Yes","No"]},
"msheet" :{"$ifNull":["Yes","No"]},
"scd_plan":{"$cond":[{ "$eq": [ "$planname", "scd_plan" ]} , "Yes", "No" ]},
"production_plan": {"$cond":[{ "$eq": [ "$planname", "production_plan" ]} , "Yes", "No" ]},
"completed":"$completed_job_functions",
"delayy":"$delay_functions",
"mecheName": "$users.merch_name",
"GmtName": "$users.gmt_tech"
}}
]
    return CuttingJobPipline




jc_pipeline  = [
{"$match":{"plan_upload_ts":{"$gt":1505179830000,"$lte":1505465099000},"factory_id":"nirmaana",
"planname":{"$exists":True,"$in":["production_plan","scd_plan"]}}},
# project new variables
{"$project":{
"job_id":{"$concat":["$task_profile.style","---","$task_profile.season","---","$task_profile.sample_type"]},
"job_card":{"$ifNull": [ "$jobCardId", "Can not find any JobCard" ] },
"style":"$task_profile.style",
"season":"$task_profile.season",
"sample_type":"$task_profile.sample_type",
"planname":"$planname",
"customer_cat":"$customer_category",
"merch_name":"$users.merch_name",
"gmt_name":"$users.gmt_tech",
"scd" :{"$ifNull": [ "$plan_details.plan_dates.scd", "check_planname" ] }
# //ssd :{$ifNull: [ "$plan_details.plan_dates.ssd", "check_planname" ] }
}}
]