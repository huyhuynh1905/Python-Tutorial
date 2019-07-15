from random import randrange

n = int(input("Enter n: "))
list1 = [0]*n
for i in range(n):
    x = randrange(20,50)
    list1[i] = x

print(list1)

list2 = list1
print(list2)
list2[1] = 10
print(list1)
