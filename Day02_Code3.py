while True:
 numb=int(input("Enter a number:"))
 if numb<=50:
  for i in range(1,numb+1):
    if i%2==0:
     print(i)
  break
else:
     print("Please enter number below 50")