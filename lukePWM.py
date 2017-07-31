import hashlib

account='Home Ubuntu'
datechanged='7/28/2017'



print 

def datesum (dateslashdelim):
    sum=0
    for char in dateslashdelim:
        if char != '/':
            sum+=int(char)
    return sum

def writenewentry():
    print ('Oops. this is not implemented yet.\n')

def updateentry():
    print ('Oops. this is not implemented yet.\n')

def getpw(mpw, account, date):
    totalinput=mpw+account
    encodedinput=totalinput.encode('utf-8')
    tatersandmeat=hashlib.sha224(encodedinput).hexdigest()
    pw=''
    for i in range(8):
        pw+=tatersandmeat[i]
    return pw



accountname= input('Type NEW to create a new entry, or UPDATE to update an entry, or enter the account name whose password you need,\n')
if accountname.lower()=='new':
    writenewentry()
elif accountname.lower()=="update":
    updateentry()
else:
    reminder='You last changed the password for ' +repr (accountname) + ' on ' + datechanged + '.'
    print (reminder)
    masterpw=input('Enter the master password you used on ' + datechanged + ':\n')
    accountpw=getpw(masterpw, accountname, datechanged)
    pwoutput='The password for ' + accountname + " is:\n" + accountpw
    print(pwoutput)
    
