#!/usr/bin/env python3
# KevinIsMyName/PostingScheduleToSlackReminders/parser.py
# Python 3.8.4

# Imports
from os import mkdir
from os.path import isdir
from os.path import join
import shutil

# Config
source_f = "template.txt"
remind_time = "10am"
SLACK_REMINDERS_DIR = "SLACK_REMINDERS"
EVENTS_ARCHIVE_DIR = "EVENTS_ARCHIVE"

# Helper function


def is_date(line):
    return len(line.split("/")) == 2


# Check if folders exist
if not isdir(SLACK_REMINDERS_DIR):
    mkdir(SLACK_REMINDERS_DIR)
if not isdir(EVENTS_ARCHIVE_DIR):
    mkdir(EVENTS_ARCHIVE_DIR)


f_in = open(source_f, "r")
lines = f_in.readlines()
for line in lines:
    if "event title" in line.lower():
        event_title = line.replace("Event Title: ", "").strip()
        f_out = open(join(SLACK_REMINDERS_DIR,
                          event_title.strip()) + "_slack.txt", "w")
    elif is_date(line.split(":")[0]):
        date = line.split(":")[0]
        posters = line.split(":")[1].rstrip().split("@")
        try:
            posters.remove(" ")
        except:
            pass
        for poster in posters:
            poster = poster.strip()
            message = "/remind @" + poster + " \"Please make a post about " + \
                str(event_title) + " today. 11am-2pm are recommended.\" at " + \
                str(remind_time) + " " + str(date)
            print(message)
            f_out.write(message + "\n")
f_in.close()
f_out.close()

# Make copy of template to archive
shutil.copy(source_f, join(EVENTS_ARCHIVE_DIR, event_title.strip()) + ".txt")
