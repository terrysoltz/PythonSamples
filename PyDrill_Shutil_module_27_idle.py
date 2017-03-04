# Python Ver. 2.7.13
#
# Author: Terry Soltz
#
# Purpose: Drill for Tech Academy to demonstrate use of
# Datetime functionality

import shutil
import os

# Get current directory and contents of subfolder Folder A
current = os.getcwd()
fileList = os.listdir(current + "/Folder A")

# Cycle through files in subfolder, and move .txt files to
# subfolder Folder B, notify console
for fileName in fileList:
    if fileName.endswith(".txt"):
        shutil.move(current + "/Folder A/" + fileName, current + "/Folder B")
        print current + "/Folder A/" + fileName + " moved to " + current + \
        "/Folder B/" + fileName




