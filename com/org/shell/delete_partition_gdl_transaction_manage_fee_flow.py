#!/root/python27_env/bin/python
# -*- coding:utf-8 -*- 
"""
name : hushenmin

"""
import os
import sys
from  com.org.utils.dateutil import *
sys.path.append('../../../')

def delete_partition(str,days=7):
    lines = os.popen("/opt/core/hadoop/bin/hadoop fs -ls %s" % str).readlines()
    for lines in lines:
        if(lines.find('items') != -1):
            continue
        hdfs_file_name= lines.strip().split(" ")[-1]
        hdfs_partition_name= hdfs_file_name.split('/')[-1]
        hdfs_datestr_name = hdfs_partition_name.split('=')[-1]
        if(is_ago_date(hdfs_datestr_name,days=days)):
            with open("delete_partition_gdl_transaction_manage_fee_flow.txt",'a+') as file:
                sys.stdout = file
                print hdfs_file_name
delete_partition('/user/hive/jdw/gdl/gdl_transaction_manage_fee_flow/')

