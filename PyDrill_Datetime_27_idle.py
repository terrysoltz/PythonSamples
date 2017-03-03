# Python Ver. 2.7.13
#
# Author: Terry Soltz
#
# Purpose: Drill for Tech Academy to demonstrate use of
# Datetime functionality

import datetime

# Establish instance of datetime object and find current local
# time (Portland)
curTime = datetime.datetime(1, 1, 1)
timePort = curTime.today()

# Establish timedelta objects for NY and London
deltaNY_sec = datetime.timedelta(0, 3600*3)
deltaLon_sec = datetime.timedelta(0, 3600*8)

# Find current times in NY and London
timeNY = timePort + deltaNY_sec
timeLon = timePort + deltaLon_sec

# Define opening and closing hours
openTime = datetime.time(9)
closeTime = datetime.time(21)

# Determine if NY branch is open
if timeNY.weekday() in (5, 6):
    print "New York branch is closed for weekend."
elif timeNY.time() < openTime or timeNY.time() > closeTime:
    print "New York branch is closed: After hours."
else:
    print "New York branch is open."

# Determine if London branch is open
if timeLon.weekday() in (5, 6):
    print "London branch is closed for weekend."
elif timeLon.time() < openTime or timeLon.time() > closeTime:
    print "London branch is closed: After hours."
else:
    print "London branch is open."

