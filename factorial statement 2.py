n=int(input("enter the no"))
fact=1
for i in range(1,n+1,1):
      print(fact,'+',i,"=",(fact*1))
      fact=fact+i
else:
    print("factorial=",fact)
