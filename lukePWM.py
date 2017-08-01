import hashlib, hashtoascii

account='Home Ubuntu'
datechanged='7/28/2017'




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
    
