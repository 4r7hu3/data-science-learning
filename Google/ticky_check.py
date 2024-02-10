#!/usr/bin/env python3

# libraries
import re
import operator
import csv

# regex and empty dicts
r_user = r'ticky: (ERROR|INFO) [\w \#\[\]]* \(([\w.]*)\)' # caches infos or errors + username
r_error = r'ticky: ERROR ([\w ]*)' # caches only error messages

user = {}
error = {}

# counting and appending
with open('syslog.log', 'r') as filelog:
    file = filelog.readlines()
    
    for row in file:
        t_info = re.search(r_user, row)
        t_error = re.search(r_error, row)
        
        if t_info != None:
            if t_info[2] not in user:
                user[t_info[2]] = {'ERROR':0, 'INFO':0}
                if t_info[1] == 'ERROR':
                    user[t_info[2]]['ERROR'] = 1
                else:
                    user[t_info[2]]['INFO'] = 1
            else:
                if t_info[1] == 'ERROR':
                    user[t_info[2]]['ERROR'] += 1
                else:
                    user[t_info[2]]['INFO'] += 1
                    

        if t_error != None:
            if t_error[1] in error:
                error[t_error[1]] += 1
            else:
                error[t_error[1]] = 1


# sorting the user dict
user = sorted(user.items(), key = operator.itemgetter(0))

# sorting the error dict
error = sorted(error.items(), key = operator.itemgetter(1), reverse = True)

# undoing the dicts and inserting 0-index for users
user = [(i[0], i[1]['INFO'], i[1]['ERROR']) for i in user]
user.insert(0, ('Username', 'INFO', 'ERROR'))

# inserting 0-index for errors
error.insert(0, ('Error', 'Count'))


# creating error_message.csv file
with open('error_message.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(error)


# creating user_statistics.csv file
with open('user_statistics.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(user)
