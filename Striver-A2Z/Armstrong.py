n=int(input())
original=n
add=0
s=str(n)
count=len(s)
while(n>0):
    lastdigit=n%10
    add=add+(lastdigit**count)
    n//=10
if(original==add):
    print(True)
else :
    print(False)