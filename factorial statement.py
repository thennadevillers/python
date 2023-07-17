n=int(input("enter the no:"))
fact=1
for i in range(1,n+1):
    print(fact,'*',i,"=",(fact*i))
    fact=fact+i
else:
    print("factorial=",fact)
