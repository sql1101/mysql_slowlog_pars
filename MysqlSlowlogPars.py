#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：xushaohui time:2022/5/27


import re

slow_log_patern =  \
                   '#\s+User@Host:\s+(?P<user>\w+)\[\w+\]\s+@\s+' \
                  '(?P<proxyHost>(\w|\[|\]|\.|\s)+)\s+Id:\s+(?P<threadID>\d+)\n' \
                  '#\s+Schema:\s(?P<Schema>(\w+|\s))\s+' \
                  'Last_errno:\s(?P<lastErrNo>\d+)\s+Killed:\s(?P<KilledErrNo>\d+)\n' \
                  '#\s+Query_time:\s+(?P<queryTime>\w+\.?\w+)\s+' \
                  'Lock_time:\s+(?P<lockTime>\w+\.?\w+)\s+Rows_sent:\s+(?P<rowsSent>\d+)\s+' \
                  'Rows_examined:\s+(?P<rowsExamined>\d+)\s+Rows_affected:\s+(?P<rowsAffected>\d+)\n' \
                  '#\s+Bytes_sent:\s(?P<bytesSent>\d+)\n' \
                  'SET\s+timestamp=(?P<sqlTimestamp>\d+);\n' \
                  '(?P<sqlText>(.|\n)*)'

file = open("/data-c/dbdata/mysqllog/slowlog")

mess = ''
while 1:
    line = file.readline()
    if line:
        match_obj = re.match("# Time:.*", line)
        if match_obj:
            if mess:
                slow_log_regex = re.compile(slow_log_patern)
                match = slow_log_regex.search(mess)
                if match:
                    sql_dict = match.groupdict()
                    print (sql_dict)
                mess = ''
        mess += line

    elif not line:
        slow_log_regex = re.compile(slow_log_patern)
        match = slow_log_regex.search(mess)
        if match:
            sql_dict = match.groupdict()
            print(sql_dict)
        break



file.close()