#Asciiout is a constant which gives us the legal output characters
Asciiout='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@)'
#takes in a string which encodes hexadecimal and outputs ascii derived from that input. Outputs a string of n characters.

def hashtoascii (hashstr,n=8):
    place=0
    outputstr=''
    zerotofflist=list(map(''.join, zip(*[iter(hashstr)]*2)))
    while len(outputstr)<n:
        if place>=len(zerotofflist):
            place=0
        zeroto63=int(zerotofflist[place],16)//4
        place+=1
        outputstr=outputstr + Asciiout[zeroto63]
    return outputstr


        
        
        
    
    
    
