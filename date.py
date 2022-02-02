# wap to input a date and number of days and display the new date 

import date_validity_checker as dv

dd = int(input("DD: "))
mm = int(input("MM: "))
yy= int(input("YYYY: "))

days = int(input("Days to add: "))

nyy = days//365

m31 = [1,3,5,7,8,10,12]

if mm in m31:
    nmm = (days - nyy*365) // 31
    ndd = days - nyy*365 - nmm * 31
else:
    nmm = (days - nyy*365) // 30
    ndd = days - nyy*365 - nmm * 30

dv.check(dd+ndd, mm+nmm, yy+nyy)
