# import httplib2
# from googleapiclient.discovery import build
#
# import GoogleDriverAPI
# import json
#
# CRID = GoogleDriverAPI.get_credentials()
# http = CRID.authorize(httplib2.Http())
#
# myDrive = build('drive', 'v3', http=http)
#
# FILES = (
#     ('test.csv','text/csv')
# )
# for f,mtype in FILES:
#     body = {'name':f}
#     if mtype:
#         body['mimeType'] = mtype
#     body = json.dumps(body )
#     res = myDrive.files().create(body =body,media_body = f).execute()
#     f = res['name']
#     mtype = res['mimeType']
#     # fileId =res['id']
#     print ('upload "%s" (%s)'%(f,mtype))
#
#

