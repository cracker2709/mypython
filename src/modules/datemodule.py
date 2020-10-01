from datetime import datetime, date

def greets():
    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    print(f"Hello today is {date_time}\n\n")

def get_date():
    now = datetime.now() # current date and time
    return now.strftime("%Y%m%d%H%M%S")