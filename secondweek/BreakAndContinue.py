#Break
while True:
    x = int(input("Enter x: "))
    if x is 5:
        break
print("X = ",x)

#continue
s=0
for n in range(10):
    if n is 3 or n is 5: #1+2+4+6+7+8+9 = 37
        continue
    s=s+n
print("S = ",s)
