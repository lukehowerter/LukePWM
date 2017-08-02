import csv, fileinput

def createcsv(filename='lukePWM.csv'):
    print ('not yet implemented')
  
def updatecsv(csvfile='lukePWM.csv', accountname):
    with open(csvfile, newline='') as f:
        reader = csv.reader(f)
        accountnamefound=False
        csvcontents=[]
        for row in reader:
            if row[0]==accountname:
                newrow=[]
                newrow=csvwriterow(accountname)
                csvcontents.append(newrow)
                accountnamefound=True
            else:
                csvcontents.append(row)
        if accountnamefound==False:
            print('Accountname not found.\n')
        else:
             with open(csvfile+'1', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(csvcontents)
                
def csvwriterow(accountname):
    mpw=''
    mpwverify=''
    verified=False
    nvalid=False
    while nvalid==False:
        n=int(input('Enter how many characters long the password should be.'))
        if isinstance(n, int):
            nvalid==True
        else:
            print(Sorry, I need you to type an integer and only an integer."
    while verified==False:
        mpw=input('Enter the master password you wish to use:\n')
        mpwverify=input('Please type the password again to verify.\n')
        if mpw==mpwverify:
            verified==True
    date='08/02/2017'
    saltedpw=mpw+datesum(date)
    saltedpw=saltedpw.encode('utf-8')
    hashedsaltedmpw=hashlib.sha224(saltedpw).hexdigest()
    rowtowrite=[accountname, date, hashedsaltedmpw]
    return rowtowrite
                
  
