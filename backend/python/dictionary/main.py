# #      dict
# car_0 = {"model": "mers", "rang": "qizil"}
# print(car_0['model'])
# student = {"ism": "Murod Olimov", "year": "2000", "age": "24"}
# print(f"{student['ism']} {student['year']} yilda tugilgan {student['age']} yoshda")

# student["kurs"] = 4

# print(student.items())
# for key, value in student.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value}\n")
# print(student.keys())
# print(student.values())

# mahsulotlar = {
#     "olma": 1000,
#     "anor": 2000,
#     "uzum": 3000,
#     "anjir": 4000,
#     "shaftoli": 4000,
# }

# print("Do'kondagi mahsulotlar")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot not in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")


# #Sort
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# # set
# mahsulotlar_set =set(mahsulotlar.values())
# print(type(mahsulotlar_set))
# lugat = {
#     "Boolen": "mantiqiy son",
#     "Float": "O'nlk son",
#     "For":"Biror amali qayta-qayta bajarish tsikli",
#     "If": "Shartlarni tekshirish amali",
#     "integer":"Butun son"
# }
# for key, value in sorted(lugat.items()):
#         print(f"{key}-{value}")


dunyo_dav = {
    "OZBEKISTON": "TOSHKENT",
    "AQSH": "WASHINGTON D.C.",
    "SINGAPUR": "KUALA - LIMPUR",
    "QIRGIZISTON": "BISHKEK",
    "ROSIYA": "MOSKVA",
    "ITALIYA": "RIM",
    "QOZOQGIZSTON": "ALMATA"
}
# print(f"Dunyo davlatlari:")
# for davlat in sorted(dunyo_dav.keys()):
#     print(davlat.upper())
# print("poytahtlar: ")
# for poytaht in sorted(dunyo_dav.values()):
#     print(poytaht.title())


# davlat_1 = dunyo_dav.get("AQSH")
# print(davlat_1)
# davlatnomi = input("Qaysi davlat poytahtini bilshni hohlaysiz?: ")
# poytaht = dunyo_dav.get(davlatnomi)


# if poytaht == None:
#     print("Kechirasiz, bizda bu haqida malumot yoq")
# else:
#     print(f"{davlatnomi.upper()}ning poytahti {poytaht.title()} shahri")


# def qoshish(*args):
#     for i in qoshish():
#         if i % 2:
#              i += issubclass
#         else:
#             ("Juft son yoq")
#     i.sum()
# qoshish([1,2,3,4]) 






# def qoshish(nums):
#     even_nums = []
#     for i in nums:
#         if i % 2 == 0:
#             even_nums.append(i)
    
#     if even_nums:
#         return sum(even_nums)
#     else:
#         return "juft son yo'q"

# print(qoshish([-2,2]))


def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    

    if total > 0:
        print(total)
    
    else:
        print("juft son yo'q")
print(sum_even_numbers([-2,2]))