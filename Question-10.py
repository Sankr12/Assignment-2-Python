''' Write a python script to display the current date and time. First create variable to store date and time, 
then display date and time in proper format (like: 13-8-2022 and 9:00 PM)'''

import datetime

# Get the current date and time
current_time = datetime.datetime.now()

# Format the date as "DD-MM-YYYY"
format_date = current_time.strftime("%d-%m-%Y")

# Format the time as "HH:MM AM/PM"
format_time = current_time.strftime("%I:%M %p")

# Display the current date and time
print(format_date)
print(format_time)