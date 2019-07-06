x = 1.11-1.10
y = 2.11-2.10

print("x = ",x," y = ",y)
#Xủ lí
diff = x-y
if diff<0:
    diff = -diff #Đổi sang số dương
if diff < 0.1: #Sai số cho phép
    print("same")
else:
    print("different")
