from time import clock
from time import sleep
start = clock()
x = input("Enter everything: ")
end = clock()
print("About some thing :))): ",round(end-start,3),"s")

for i in range(1,10):
    print(i)
    sleep(1)
