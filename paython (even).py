ans="yes"
while (ans=="yes"):
    print("enter any number")
    x=int(input())
    if(x%2==0):
        print(x,"even")
    else:
        print(x,"is a odd number")
    print("Do you want to contiune(yes/No)")
    ans=input()
exit()
