#№1
a=5
print(a)
#№2
b=10
b+=10
print(b)
#№3
c=15
c-=5
print(c)
#№4
ai=512
ai-=3
ai+=245
print(ai)
#№5
a2=int(input())
b=a2*4
c=a2/4
print(a2)
#№6
a3=int(input())
#Первый способ
print(a2**3)
#Второй способ
print(pow(a2,3))
#№7
into=int(input())
iutro=int(input())
if(into > 5 and iutro > 5):
    print("Два числа больше пяти")
else:
    print("Минимум одно число меньше или равно пяти")
#№8
lop=int(input())
kol=int(input())
if(lop<0 or kol<0):
    print("True")
else:
    print("False")
#№9
check=int(input())
if(check!=2):
    print("True")
else:
    print("False")
#№10
mal=int(input())
lal=int(input())
print(max(mal,lal))