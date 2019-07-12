numStr = "09872581236"

print(numStr.startswith("098"))
print(numStr.endswith("2367"))

s = "hello;hcode;function;thanks watching!"

s1 = s.split(";")
for str in s1:
    print(str)
s2 = " "
s2 = s2.join(s1)
print(s2)

print(s2[2:-10])
