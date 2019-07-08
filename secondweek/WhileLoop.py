x = int(input("Enter x(0-10): "))
while x<0 or x>10:
    x = int(input("Enter x(0-10): "))
print("Value x = ",x)

s=0
i=0
n = int(input("Enter n: "))
while i<=n:
    s+=i
    i+=1
print("Value S = ",s)
