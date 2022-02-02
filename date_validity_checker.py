# input a date and check its validity

import sys
from termcolor import colored, cprint

def check(dd, mm, yy):

    m31 = [1,3,5,7,8,10,12]

    validity = "valid"
    reason = ""

    if dd < 0 :
        validity = "invalid"
        reason = "zero date"
    elif dd > 31:
        validity = "invalid"
        reason = "date more"

    elif mm <1 or mm>12:
        validity = "invalid"
        reason = "month"
    elif yy < 0:
        validity = "invalid"
        reason = "year"

    else:
        if mm not in m31:
            if dd > 30:
                validity = "invalid"
                reason = "date for m30 more"

        if mm == 2:
            if yy % 4 != 0:
                if dd > 28:
                    validity = "invalid"
                    reason = "feb date error nl"

            else:
                if dd > 29:
                    validity = "invalid"
                    reason = "feb date error leap"

    if validity == "invalid":
        correct(reason, dd, mm, yy)
    else:

        text = colored('Red', 'red', attrs=['reverse', 'blink'])
        print(text)
        
        print(f"{dd}/{mm}/{yy}")
        print("Thank you for using Date Adder and Validator.\nBy Dev Anuj Patel")

def correct(reason, dd, mm, yy):

    if reason == "year":
        validity = "valid"

    elif reason == "month":
        while mm > 12:
            yy += 1
            mm -= 12

    elif reason == "feb date error leap":
        while dd > 29:
            mm += 1
            dd -= 29

    elif reason == "feb date error nl":
        while dd > 28:
            mm += 1
            dd -= 28

    elif reason == "date for m30 more":
        while mm > 30:
            mm += 1
            dd -= 30
    elif reason == "date more":
        while dd > 31:
            mm += 1
            dd -= 31
    elif reason == "zero date":
        # date zero or less than zero
        pass

    check(dd, mm, yy)
