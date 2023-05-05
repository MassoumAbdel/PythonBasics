from datetime import datetime
from time import *
from os import *


def get_date():
    return datetime.today().strftime('%y-%m-%d')


ctime = datetime.today().strftime('%H:%M:%S')
fntimestamp= datetime.today().strftime('%y/%m/%d - %H:%M:%S')

print(f'current date (from function we created)  is : {get_date()}')
print(f'current time is : {ctime}')
sleep(3) # this one give like 3 second then it will execute what is after sleep
print(f'current time is : {fntimestamp}-myapp.log')

current_dir = path.dirname(path.abspath(__file__)) # this will give you your current directory and file
print(f'current dir: {current_dir}')

root_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
print(f'current dir: {root_dir}')
