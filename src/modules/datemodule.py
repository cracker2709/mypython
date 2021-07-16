from datetime import datetime


def greets():
    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    print(f"Hello today is {date_time}\n\n")

def get_date():
    now = datetime.now() # current date and time
    return now.strftime("%Y%m%d%H%M%S")

def display_date_in_webapp():
    now = datetime.now() # current date and time
    return now.strftime("%d/%m/%Y, %H:%M:%S")

def display_date_from_timestamp(value):
    unix_timestamp = float(value)
    local_time = datetime.fromtimestamp(unix_timestamp)
    return local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z")

