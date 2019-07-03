#String data type
astr = "Hello Word"
print(astr)
print(astr[0])
print(astr[0:5])

#Nummber data type
int_a = 10
float_a = 10.2
complex_a = 3+2j
a_complex = complex(4,5)
print(type(int_a))
print(float_a)
print(type(complex_a))
print(a_complex)

#Set data type
a_a = {"Blue","Red","Blue","Yellow"}
print(a_a)
s_a = set("addadsadsadaavas")
print(s_a) #unique letters in s_a

#list Data type
list = [123, "Huy", 456.5, "d"]
list2 = ["Hello", "World"]
print(list)
print(list[0:2])
print(list2 * 2)
print(list + list2)


#dictionary data type
dic = {'name':'red','age':15}
print(dic)
print(dic['name'])
print(dic.values())
print(dic.keys())

#boolean data type
x = 5
y = 6+3j
t = True
f = False
print(x or y)
print(y.real)
print(y.imag)
print(t)
print(f)
