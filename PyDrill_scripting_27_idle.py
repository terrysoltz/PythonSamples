# Python Ver. 2.7.13
#
# Author: Terry Soltz
#
# Purpose: Drill for Tech Academy to demonstrate use of
# Datetime functionality

import shutil
import os
import time

# Get current directory and contents of subfolder General
current = os.getcwd()
fileList = os.listdir(current + "/General")

# Get current time
curTime = time.time()

# Set 24-hour lag
dayAgo = curTime - 3600*24

# Cycle through files in subfolder, and check .txt files to see
# if they have been modified in the last day, and if so, copy to
# Home Office subfolder, notify console.
for fileName in fileList:
    if fileName.endswith(".txt"):
        modifiedTime = os.stat(current + "/General/" + fileName).st_mtime
        if modifiedTime > dayAgo:
            shutil.copy(current + "/General/" + fileName, current + "Home Office")
            print "copied: " + fileName


