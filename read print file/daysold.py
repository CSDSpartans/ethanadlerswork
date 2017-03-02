#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta

print('22000 days from today is:')
print(datetime.now() + timedelta(days=22000))

birthday = input("What is your birthday? dd/mm/yyyy \n")

#print('You will be 22000 days old on:')
#print (birthday + timedelta(days=22000))
day=int(birthday[0:2])
month=int(birthday[3:5])
year=int(birthday[6:10])
print("Your birthday is "+str(day)+"/"+str(month)+"/"+str(year)+"?")
#Maybe use an until loop here
if input("(Y/n)") in ("Y","y","",None):
    print(datetime(year,month,day)+timedelta(days=22000))
