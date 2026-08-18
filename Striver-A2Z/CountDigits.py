#basic extraction of digits
n=1179890
count=0
while(n>0):
    digit=n%10
    n//=10
    count+=1
print(count)