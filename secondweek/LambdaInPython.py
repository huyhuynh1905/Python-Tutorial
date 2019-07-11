
def checkNumber(f,x,y):
    return f(x,y)

def soChan(number):
    if number%2==0:
        return True
    else:
        return False
def minMax(a,b):
    if a>b:
        return a
    else:
        return b
# kq = checkNumber(lambda x:soChan(x),8)
# print("Use Lambda: ",kq)
# kq = checkNumber(soChan,8)
# print("Non-use Lambda:",kq)
kq = checkNumber(lambda x,y:minMax(x,y),5,6)
print("Use Lambda: ",kq)
kq = checkNumber(minMax,5,6)
print("Non-use Lambda: ",kq)
