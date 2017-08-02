import hashlib, hashtoascii, lukecsv
import os.path

if os.path.isfile('lukePWM.csv')==False:
    lukecsv.createcsv('lukePWM.csv')

account='Home Ubuntu'
datechanged='7/28/2017'






def writenewentry():
    accountname=input('Please enter the name of the account which you want to create an entry for. \n')
    if lukecsv.entryexists(accountname)==False:
        lukecsv.makeentry(accountname)
    else:
        print('That account appears to already exist. Please update instead.')

def updateentry():
    accountname=input('Please enter the name of the account which you want to create an entry for. \n')
    if lukecsv.entryexists(accountname)==True:
        lukecsv.updateentry(accountname)
    else:
        print('That account does not appear to exist. Please add a new entry instead.')

def outputpw(accountname):
    reminder='You last changed the password for ' +repr (accountname) + ' on ' + datechanged + '.'
    print (reminder)
    masterpw=input('Enter the master password you used on ' + datechanged + ':\n')
    accountpw=getpw(masterpw, accountname, datechanged)
    pwoutput='The password for ' + accountname + " is:\n" + accountpw
    print(pwoutput)
    

def getpw(mpw, account, date, n=12):
    totalinput=mpw+account
    encodedinput=totalinput.encode('utf-8')
    tatersandmeat=hashlib.sha224(encodedinput).hexdigest()
    pw=hashtoascii.hashtoascii(tatersandmeat, n)
    return pw


def takeuserinput():
    selection= input('Type NEW to create a new entry, or UPDATE to update an entry, or enter the account name whose password you need. Otherwise, type exit to close the program.\n')
    if selection.lower()=='new':
        writenewentry()
    elif selection.lower()=='update':
        updateentry()
    elif selection.lower()=='exit':
        global exitflag
        exitflag=True
        print('Goodbye')
    else:
        outputpw(selection)



exitflag=False
while exitflag==False:
    takeuserinput()
    
