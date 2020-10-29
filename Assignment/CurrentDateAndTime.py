# 1st method
# importing datetime module for now()
import datetime


# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is : "
      , end="")
print(current_time)

# 2nd method
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
#today = date.today()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)