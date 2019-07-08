count = sum = 0
while count < 5:
    x = int(input("Enter x: "))
    if x is 5:
        break
    sum = sum +x
    count+=1
else:
    print("Sum = ",sum)

#for same
sum = 0

for n in range(5):
    x = int(input("Enter x: "))
    if x is 5:
        break
    sum = sum+x
    count+=1
else:
    print("Sum = ",sum)
