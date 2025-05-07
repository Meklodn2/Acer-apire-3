"""
t = (" Salom John"," salom Smith"," salomDoe")#tuple
z = "Hello" # str -> string
num3  = 10 # int ->Integer 
num4 = 10.5 # float
rost3 = True #bool -> boolen
# index 0      1      2


q = ["kettu", "gooo","пошли","olim"]

for name in q:
    print("Salom",name)
print("Kod",str(len(q)),"" + "mavjud ")

sonlar = list(range(1,11))
print(sonlar)
for son in sonlar:
    print(son)

for i in range (1,11):
    print(f"{i} ning kvadrati {i ** 2} ga teng")   

for i in range (1,11):
    print(f"{i} ning kvadrati {i ** 3} ga teng")   
sonlar = list(range(1,11))
sonlar2 = []
for son in sonlar:
    sonlar2.append(son ** 2)
print(sonlar)
print(sonlar2)
dasturlash_tillari = []
print("5 ta dasturlash tilini kirting.")
for n in range(5):
    dasturlash_tillari.append(input(f"{n+1}-dastulash tilini kiriting: "))
print(dasturlash_tillari)
n_dasturlash = int(input("nechta dasturlash tilini bialsiz?:"))

for n in range(n_dasturlash):
    dasturlash_tillari.append(input(f"{n+1}-dastulash tilini kiriting: "))
print(dasturlash_tillari)
avtolar = ['bmw','mers','audi']
for avto in avtolar:
    if avto == "bmw":
        print(avto.upper())
    elif avto == "mers":
        print(avto.lower())
    else:
        print(avto.title())

tenglama = int(input("12 * 6 nechiga teng"))
if tenglama != 72:
    print("javob hato")
 
login = input("Yangi login kiritingg")
if  len(login) <= 5:
    print("login 5 harftdan koproq bolish shart")
Yengi_cars = ['bmw','mers','audi','hyudai','gm']
for avto in Yengi_cars:
    if avto == "gm":
       print(avto.upper())
    else:
        print(avto.title())


for avto in Yengi_cars:
    if avto != "gm":
       print(avto.title())
    else:
        print(avto.upper())

login = input("login kiriting")
if login == "admin" or login == "ADMIN":
    print("Hush kelibsiz, Admin")
else:
    print("hush kelibsiz {foydalanuvchi ismi}")

x = input("son kiriting")
y = input("son kiriting")
if x == y:
    print("Sonlar teng")
 
son = int(input("son kiriting"))
x = 0
if son <= x :
    print("Manfiy son")
else:
    print("musbat son")


print(10 - 5)
print(5 + 3)
print(5**4)
print(5*2)
print(20/4)
# print(22/4, %)
fname = "john"
lname = "Doe"
print(fname,lname)
print(fname + ' ' + lname)
print(f"{fname} {lname}")
print("{0} {1}")
"""

# print("hello\tworld")
# print("Hello\nworld")
# print("G\'ildirak")
# print("""hello
# world""")


"""
hello = "hello world!"
print(hello.upper())
print(hello.lower())
print(hello.title())
print(hello.capitalize())

day = int(input("Tufilgan yilizni kiriting:"))
print(f"sizning yoshingiz {2024 - day} da ekan")

day = int(input("yoshizni kiriting:"))
print(f"sizning tugilgan ylingiz {2024 - day} ekan")

usernum = int(input("istlagan sonni kiriting:"))
print(usernum ** 2, usernum ** 3)

usernumb = int(input("istlagan sonni kiriting:"))
usernumbe = int(input("istlagan sonni kiriting:"))

print(usernumb + usernumbe)
print(usernumb - usernumbe)
print(usernumb * usernumbe)
print(usernumb / usernumbe)

#            0        1        2           3
mevalar = ['olma', 'anjir', 'shoptoli','o\'rik']
print("brinnchi meva",mevalar[0])
print("ikkinchi mava", mevalar[1])
mevalar.append("tarvuz")
print(mevalar[-1])
mevalar.insert(1,"qovun")
print(mevalar)
del mevalar [3]
mevalar.remove("olma")
print(mevalar)
yoqotildi = mevalar.pop(3)
print(mevalar)
print(yoqotildi)


Yengi_cars = ['bmw','mers','audi','hyudai','gm']
Yengi_cars.sort(reverse=True)
print(Yengi_cars)
nums = [12,234,56,789]
nums.sort()
nums.reverse()
print(nums)
print(len(nums))

nums = [12,-45,46,-50,1000,43]
kotta = max(nums)
kischik = min(nums)
sonlar = list(range(120,1201,2))
print(sonlar)

qw = sum(sonlar)
print(qw)
kotta = max(sonlar)
kichik = min(sonlar)
print(kotta - kichik)
print(len(sonlar))
print(sonlar[:20])
print(sonlar[20:])
print(sonlar[20:20])
"""
# tar

# # Tuples - ozgarmas ozgaruvchi(list)

# vehicles = ("Bus", "car", "cycle", "boat")
# vehicles = list(vehicles)
# vehicles.append("ship")
# vehicles.remove("Bus")
# vehicles[1] = "Train"
# vehicles = tuple(vehicles)
# # print(vehicles)


# # for loop

# ismalr = ["ali", "hoji", "fyzi", "yusuf", "orif"]
# for ism in ismalr:
#     print(ism)

# sonal = list(range(1, 12))
# for n in sonal:
#     print(n)

# for ism2 in ismalr:
#     print(f"salom {ism2}")
# print(f"kod {len(ismalr)} marta takrorlandi")


# n_people = int(input("how many peoples do you speak:"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-you had spoken"))
# print(ismlar)


cars = ["bmw", "mers", "audi", "hyudai", "gm"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())


# ask = input("ismingiz nima?")

# if ask.lower() == "ali":
#     print("salom Ali")
# else:
#     print(f"Uzr, {ask} biz Alini kutyapmiz")

# misol = int(input("12*6="))
# if misol == 72:
#     print("To'gri")
# else:
#     print("Javob xato")

# login = input("yangi login kiriting:")
# if len(login) >= 5:
#     print(login)
# else:
#     print("login 5 harfdan koproq bo'lishi shart!")


# import math

# for avto in cars:
#     if avto != "gm":
#         print(avto.title())
#     else:
#         print(avto.upper())
# son1 = int(input("enter number:"))
# son2 = input("enter number:")
# if son1 == son2:
#     print("your number is equal")
# if son1 >= 0:
#     print("Musbat son")
# else:
#     print("manfiy son")
# if son1 > 0:
#     print(math.sqrt(son1))
# else:
#     print("manfiy son")

# kun = input("Bugin qanday kun?:")
# if kun == "shanba" "yakshanba":
#     print("dam olish kuni")
# else:
#     print("bugun ish kuni")
# son = int(input("jufn son kiring:"))
# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("bu son juft emas")
    
# son1 = int(input("Birinchi sonni  kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# if son1 > son2:
#     print(f"{son1}>{son2}")
# elif son1 == son2:
#     print(f"{son1}={son2}")
# else:
#     print(f"{son1}<{son2}")
# ismlar = ['anvar','bosit','yusuf','dilshod','hojiaakbar']
# login = input("Yangi login kiriting: ")
# if login in ismlar:
#     print("Login band,yangi login kiriting!")
# else:
#     print("Hush kelibsiz!")
