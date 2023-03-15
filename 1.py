s=input("Taper une chaine ")
n=len(s)
nb=0
for i in range(0,n):
    if(s[i]==s[i+1]):
        nb+=1
print(nb)  