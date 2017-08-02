import csv, fileinput, hashlib

def createcsv(filename='lukePWM.csv'):
    with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Accountname', 'Datechanged', 'mpwcheck'])
  
def updateentry(accountname, csvfile='lukePWM.csv'):
    with open(csvfile, newline='') as f:
        reader = csv.reader(f)
        accountnamefound=False
        csvcontents=[]
        for row in reader:
            if row[0]==accountname:
                newrow=[]
                newrow=makerow(accountname)
                csvcontents.append(newrow)
                accountnamefound=True
            else:
                csvcontents.append(row)
        if accountnamefound==False:
            print('Accountname not found.\n')
        else:
             with open(csvfile, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(csvcontents)

def makeentry(accountname, csvfile='lukePWM.csv'):
    with open(csvfile, newline='') as f1:
        reader = csv.reader(f1)
        accountnamefound=False
        csvcontents=[]
        for row in reader:
            csvcontents.append(row)
    with open(csvfile, 'w', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerows(csvcontents)
            writer.writerow(makerow(accountname))
    message='New entry added for' + repr(accountname) + '.\n'
    print(message)
    
def entryexists(accountname, csvfile='lukePWM.csv'):
    accountnamefound=False
    with open(csvfile, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]==accountname:
                accountnamefound=True
    return accountnamefound
                        
def makerow(accountname):
    mpw=''
    mpwverify=''
    verified=False
    nvalid=False
    while nvalid==False:
        n=int(input('Enter how many characters long the password should be.\n'))
        if isinstance(n, int):
            nvalid=True
        else:
            print('Sorry, I need you to type an integer and only an integer.')
    while verified==False:
        mpw=input('Enter the master password you wish to use:\n')
        mpwverify=input('Please type the password again to verify.\n')
        if mpw==mpwverify:
            verified=True
    date='08/02/2017'
    saltedpw=mpw+ repr(datesum(date))
    saltedpw=saltedpw.encode('utf-8')
    hashedsaltedmpw=hashlib.sha224(saltedpw).hexdigest()
    rowtowrite=[accountname, date, hashedsaltedmpw]
    return rowtowrite

def datesum (dateslashdelim):
    sum=0
    for char in dateslashdelim:
        if char != '/':
           sum+=int(char)
    return sum
  
