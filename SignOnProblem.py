#!/bin/python3

import math
import os
import random
import re
import sys

arr = ["30 1 sign-on", "30 5 sign-out", "1", "50 100 sign-out", "100 20 sign-on", "100 2 sign-out", "50 1 sign-on", "55"]

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan

# I have to do this as a dictionary
num = 0
quick_sort= []
pattern = re.compile("[0-9]+")
results_dict = {}


def processLogs(logs, maxSpan):
    logs.sort()
    print(logs)
    # maxSpan = 0
    # diff_num = 0
    # new = ""
    # results =[]
    # track = 0
    
    for i in range(len(logs)-1):
        log_entry= logs[i].split()
        condition1 = len(log_entry) == 3
        
        # ensures the log entry has three parts a userID a timestamp and a 'sign-on' or 'sign-off'
        if not condition1:
            print(f"Condition 1 skip {log_entry}")
            continue
        user_name = log_entry[0]
        user_name_next = logs[i+1].split()[0]
        user_name_prev = logs[i-1].split()[0]
        time_stamp = int(log_entry[1])

        # ensures that once sorted//which should be 
        # put sign-on and ahead of sign-off with user_id's 
        # equal, it cancels if it gets to an index where 
        # the next is just a single digit.
        condition2 = len(logs[i+1].split()) ==3
        if not condition2:
            print(f"Condition 2 skip {logs[i+1].split()}")
            continue

        time_stamp2 = int(logs[i+1].split()[1])
        action = log_entry[2]

        action_count = 0
        delete_me = False
        cause_code =""
        
       #now that we have variables defined we can process
        condition3= type(pattern.fullmatch(user_name)) != None
        condition4= len(user_name) <= 9
        condition5= list(str(time_stamp))[0] != "0"
        condition6= time_stamp2 > time_stamp
        condition7= 0 < time_stamp <= 10**9
        condition8= action == "sign-in" or action == "sign-out"
        condition9= user_name == user_name_next and user_name != user_name_prev
        condition10= 1<= maxSpan
        condition11= maxSpan <= 10**5

        if not condition3:
            print(f" Condition 3 Failure: {log_entry}")
            continue
        if not condition4:
            print(f" Condition 4 Failure: {log_entry}")
            continue
        if not condition5:
            print(f" Condition 5 Failure: {log_entry}")
            continue
        if not condition6:
            print(f" Condition 6 Failure: {log_entry}")
            continue
        if not condition7:
            print(f" Condition 7 Failure: {log_entry}")
            continue
        if not condition8:
            print(f" Condition 8 Failure: {log_entry}")
            continue
        if not condition9:
            print(f" Condition 9 Failure: {log_entry}")
            continue
        if not condition10:
            print(f" Condition 10 Failure: {log_entry}")
            continue
        if not condition11:
            print(f" Condition 11 Failure: {log_entry}")
            continue
    
        
    #     #Handle USER ID
    #     if pattern.fullmatch(user_name) is not None:
    #         if len(user_name) <=9:
    #             #handle timestamp
    #             if pattern.fullmatch(str(time_stamp)) is not None:
    #                 if list(str(time_stamp))[0] != "0":
    #                     if 0 < time_stamp <= 10**9:
    #                         #handle action statment
    #                         if action == "sign-in" or action == "sign-out":
    #                             if user_name == user_name_next and user_name != user_name_prev:
    #                                 if time_stamp2 > time_stamp:
                                        
    #                                     diff_num = int(logs[i+1].split()[1])- int(logs[i].split()[1])
    #                                     if 1 <= diff_num <= 10**5:
                                        
    #                                         results_dict = {user_name: diff_num}
    #                                 else:
    #                                     deleteme = True
    #                                     cause_code = "Sign out time stamp larger than sign in"
    #                             else:
    #                                 deleteme = True
    #                                 cause_code = "More than 1 user entry"
    #                             # get MaxSpan
    #                             # apply condition  1 
    #                             # apply condition 2
    #                         else:
    #                             deleteme = True
    #                             cause_code = "Sign-In / Sign-Out Wrong Action"
    #                     else:
    #                         deleteme = True
    #                         cause_code = "time stamp value out of range"
    #                 else:
    #                     deleteme = True
    #                     cause_code = "time stamp starts with zero"
    #             else:
    #                 deleteme = True
    #                 cause_code ="time stamp has letters or symbols included"
    #         else:
    #             deleteme = True
    #             cause_code = "User ID has too many digits"
    #     else:
    #         deleteme = True
    #         cause_code = "UserID is alpha numeric or contains symbols"
                            
    # for k in results_dict.keys():
    #     results = list(results_dict.keys())
    # return results_dict
            
processLogs(arr, 1)
   
        
    #     if logs[i].split()[0] == logs[i+1].split()[0]:
    #         if len(logs[i].split()[0])>=10:
    #             print("")
    #         else:
    #             print(logs[i].split()[0] , logs[i+1].split()[0])
                
    #             diff_num = str(int(logs[i+1].split()[1])- int(logs[i].split()[1]))
    #             print(diff_num)
                
    #             quick_sort.append(diff_num + "_" + logs[i].split()[0] )
    #             #print(f"This is: {i} {maxSpan} for user {logs[i].split()[0]}")
    # quick_sort.sort()
    # for i in quick_sort:
    #     track +=1
    #     if track >2:
    #         quick_sort.pop()
    # for i in range(len(quick_sort)):
    #     new = quick_sort[i].split("_",1)[1]
    #     print(new)
    #     results.append(new)
    #     results.sort(reverse=True)
    # return results
            


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     logs_count = int(input().strip())

#     logs = []

#     for _ in range(logs_count):
#         logs_item = input()
#         logs.append(logs_item)

#     maxSpan = int(input().strip())

#     result = processLogs(logs, maxSpan)

#     fptr.write('\n'.join(result))
#     fptr.write('\n')

#     fptr.close()