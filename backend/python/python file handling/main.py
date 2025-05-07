# import os
# # with open('hello.txt') as fayl:
# #     hello = fayl.read()
# #     hello = hello.rstrip()
# #     hello = hello.replace('\n', '')
# #     print(hello)
# #     fayl.close()



# faylnomi = 'new_file.txt'
# ism = 'olijon rahmonov\n'
# tyil = 2009
# # with open (faylnomi,'w') as fayl:
# #     fayl.write(ism)
# #     fayl.write(str(tyil) + '\n')

# # with open (faylnomi,'a') as fayl:
# #     fayl.write("john doe\n")
# #     fayl.write('2000 \n')


# # if os.path.exists('new_file.txt'):
# #     os.remove('new_file.txt')
# #     print('Fayl o\'chirldi')
# # else:
# #     print('Fayl topilms=adi')



# def yozuvni_qoshish(ism,familiya,yosh):
#     with open ("users.txt",'a') as fayl:
#         fayl.write(f"Ism: {ism}, Familiya: {familiya}, Yosh: {yosh}\n")

# def user_getinfo():
#     while True:
#         ism = input("Ismingizn kiriting: ")
#         familiya = input("Familyangizni kiriting: ")
#         yosh = input("Yoshingizni kiriting: ")
#         yozuvni_qoshish(ism,familiya,yosh)

#         savol =  input("ma'lumot qoshishni holaysizmi ha/yo'q: ")
#         if savol.lower() == 'ha':
#             return user_getinfo()
#         else:
#             break
    


# # user_getinfo()

# try:
#     with open ('users2.txt','r') as fayl:
#         malumotlar = fayl.readlines()
#         if malumotlar:
#             print("Fayldagi malumotlar: ")
#             for line in malumotlar:
#                 print(line.strip())
#         else:
#             print("fayl b'osh")
# except FileNotFoundError:
#     print("Fayl topilmadi")

# main.py
# Faylni o'qish va tahrirlash














# with open("main2.py", 'r') as fayl:
#     content = fayl.readlines()  


# for i in range(len(content)):
#     if content[i].startswith("my_list"):
#      \
#         content[i] = "my_list = ['Hello, world!']\n"  


# with open("main2.py", 'w') as fayl:
#     fayl.writelines(content)

with open ("main3.py",'w') as fayl:
    fayl.write("def qoshish(a, b):\n    return a + b\n")
    fayl.write("print(qoshish(5, 10))")