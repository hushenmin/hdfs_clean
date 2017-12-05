#!/root/python27_env/bin/python
# -*- coding:utf-8 -*- 
"""
name : hushenmin

"""
from datetime import datetime
from datetime import timedelta
#get date on number days ago .default:7days
def get_ago_date(days=7):
    timeago = datetime.now() - timedelta(days=days)
    return  timeago.date()
#str transfer to date
def get_fromstr_date(str):
    try:
        date = datetime.strptime(str,"%Y-%m-%d")
    except ValueError as e:
        try:
            date = datetime.strptime(str, "%Y%m%d")
        except ValueError as e:
            print e
    return  date.date()
#get today date
def get_today_date():
    now = datetime.now().date()
    return now
#get boolean whether is number days ago or not.default 7.
def is_ago_date(str,days=7):
    if (get_today_date()-get_fromstr_date(str=str)).days >=7:
        return True
    return False
#print (get_ago_date(1) - get_today_date()).days
#print (is_ago_date("20171116"))
get_fromstr_date("2017111")




#get_date()
#     return datetime.now() - timedelta(days=days)
# print get_date()