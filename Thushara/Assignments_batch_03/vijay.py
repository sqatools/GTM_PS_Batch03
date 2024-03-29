a=c=d=h=p=1
b=15
e=20
f=o=0
g=30
k=40
l=2
m=41
n=50
q=60
for i in range(0,9):
    for j in range(0,90):

        if i==a and j==a:
            print("#",end="")
            a+=1
        elif c<=i<9 and j== b:
            print("#",end="")
            c=c+1
            b=b-1
        elif i==d and j==e:
            print("#",end="")
            d=d+1
        elif f<i<8 and j==g:
            print("#",end="")
            f=f+1
        elif i==8 and (24<j<30):
            print("#",end="")
        elif i==7 and j==24:
            print("#", end="")
        elif i==h and j==k:
            print("#",end="")
            h=h+1
            k=k-1
        elif i==l and j==m:
            print("#",end="")
            l=l+1
            m=m+1
        elif i==4 and (37<j<44):
            print("#",end="")
        elif o<i<=5 and j==n:
            print("#",end="")
            n=n+1
            o=o+1
        elif i== p and j==q:
            print("#",end="")
            p=p+1
            q=q-1


        else:
            print(" ", end="")




    print()
