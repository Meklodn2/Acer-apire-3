son = 1
while son <= 5:
    print(son)
    son = son + 1

# print("kiritilgan sonni kavadratini qaytaruvchi dastur.")
# savol = "istalgan soni kiriting 'exit'"
# flag = True
# while flag:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         flag = False
#     else:
#         print(float(qiymat) ** 2)

# # breack and contiune

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5 :
#         break
#     print(f"{son} ning kvadrati {son ** 2 } ga teng")

# sonlar2 = list(range(1,11))
# for son in sonlar2:
#     if son == 5 :
#         continue
#     print(f"{son} ning kvadrati {son ** 2 } ga teng")
# while True:
#     print("yusfk")



# print("kiritilgan sonni kavadratini qaytaruvchi dastur.")
# savol = "istalgan soni kiriting 'exit'"

# while True:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break
#     else:
#         print(float(qiymat) ** 2)
# savol = ("Ko'rgan kinoizni kiriting 'stop': ")
# kinolar = []
# while True:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         kinolar.append(qiymat)
# print(kinolar)



def dostlar():
    print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
    friends = []
    count = 1
    while True:
        name = input(f"{count}-do'stingiz ismini kiriting: ")
        friends.append(name)
        add_more = input("Yana ism qo'shasizmi? (ha/yo'q): ").lower()
        if add_more != 'ha':
            break
        count += 1
    return friends


friend_list = dostlar()
print("\nSizning do'stlaringiz ro'yxati:")
for i, friend in enumerate(friend_list, 1):
    print(f"{i}. {friend}")
    
