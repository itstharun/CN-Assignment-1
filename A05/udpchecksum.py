import sys
name=sys.argv[0]#file name
sip= sys.argv[1] #source ip
dip=sys.argv[2]  #destination import import IP
sp=sys.argv[3]   #source port
dp=sys.argv[4]   #destination port
data=sys.argv[5] # data to e sent

n=len(data) #obtaining length of data to be sent
a=sip.split('.')
b=dip.split('.')
c1=format(int(a[0]),'02x')+format(int(a[1]),'02x')
c2=format(int(a[2]),'02x')+format(int(a[3]),'02x')#converts the  source ip to hexa of length 4

s1=format(int(b[0]),'02x')+format(int(b[1]),'02x')
s2=format(int(b[2]),'02x')+format(int(b[3]),'02x')#converts the  destination ip to hexa of length 4

cs=int(c1,16)+int(c2,16)+int(s1,16)+int(s2,16) #checksum of IP's obtained by converting the obtained hexa

sp=format(int(sp),'04x')
dp=format(int(dp),'04x') #converting source and destination port to hexa

cs=cs+int(sp,16)+int(dp,16)+(n+8)+17+(n+8) #updating sum so far.
#adding source port ,destination port ,pseudo header length,udp protocol number,UDP length

def dcs(a):# method to obtain the checksum for the given data
    s=[] #to store 16bit hexadecial from the data
    j=0  #index variable
    for i in range(0,len(a)-1,2):
        s.insert(j,format(ord(a[i]),'02x')+format(ord(a[i+1]),'02x')) #concatenates hexa of 2 consecutive characters
        j=j+1 #updating index
    if((len(a)%2)==1): #padding zeros to obtain 16bit integers
        s.insert(j,format(ord(a[len(a)-1]),'02x')+format(0,'02x'))
        j=j+1
    sum=0
    for i in range(j):
        sum=sum+(int(s[i],16))  #adding the hexa values
    return format(sum,'02x')  #return checksum of the data

datacs=dcs(data)
cs=cs+int(datacs,16) #updating checksum

h=format(cs,'08x') #padding to length 8
h=(int(h[0:4],16)+int(h[4:],16)) #wrap carry and adding to sum obtained

fcs=(65535-h)         #1's complement of obtained checksum
print('The UDP checksum Obtained is:',hex(fcs)) #printing final checksum in hexadecimal
