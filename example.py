# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:10:30 2021

@author: JimmyChen
"""

import os
import glob

os.chdir('F:\SS21-22\Master thesis\Coding\Coding work\de-simple\datasets\icews14')
dataset_list = glob.glob("*.txt")

# month_to_days = {"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}
month_to_days = {"01": 0, "02": 31, "03": 59, "04": 90, "05": 120, "06": 151, "07": 181, "08": 212, "09": 243,
                 "10": 273, "11": 304, "12": 334}


def takeThird(elem):
    return elem[3]


new_lines_merged = []
for dataset in dataset_list:
    new_lines = []
    with open(dataset, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(sep="\t")
            time = line[-1][:-1]
            times = time.split(sep="-")
            times = [time for time in times]

            # calculate the absolute time
            nr_days = str(int(times[0]) * 365 + month_to_days[times[1]] + int(times[2]))
            # nr_days = times[0]*365 + times[1]*30 + times[2]
            # add the absolute time to each event
            line = [line[0], line[1], line[2], nr_days, line[3]]
            new_lines.append(line)
            new_lines_merged.append(line)

    # sort each line in new_lines by nr_days
    new_lines_glued = []
    glue = '\t'
    new_lines.sort(key=takeThird)
    for line in new_lines:
        line = glue.join(line)
        new_lines_glued.append(line)

    # with open(os.path.join('..\processed_dataset',dataset), encoding = 'utf-8') as f:
    with open(os.path.join(os.getcwd(), "processed_dataset", dataset), 'w', encoding='utf-8') as f:
        for line in new_lines_glued:
            f.write(line)






# merge three files together in chronological order
new_lines_merged_glued = []
glue = '\t'
new_lines_merged.sort(key=takeThird)
for line in new_lines_merged:
    line = glue.join(line)
    new_lines_merged_glued.append(line)

with open(os.path.join(os.getcwd(), "processed_dataset", "dataset.txt"), 'w', encoding='utf-8') as f:
    for line in new_lines_merged_glued:
        f.write(line)




#new functionality added
def split_file():
    pass

#2nd functionality added
def split_file_2():
    pass

#3rd functionality added
def split_file_3():
    pass



