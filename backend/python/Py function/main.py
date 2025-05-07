# # def - define
# def hello():
#     print("Hello World!")


# hello()


# def salom_ber(ism):  # ism = parametr

#     """" Funksiya foydalanuvchiga salom beradi"""
#     print("assalmo aleykum")


# salom_ber("Anvar")  # anvar = argument
# salom_ber(salom_ber.__doc__)

# def fullname(fname,lname):
#     """ Ism va familiya"""
#     print(f"User fname: {fname}")
#     print(f"User lname: {lname}")


# fullname('John','Doe')

# def find_year(age,now=2024):
#     print(f"{now-age}")
# find_year(14)

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# qwe = 2024 - yil
# print(qwe)
# if qwe <= 18:
#     print(f"Siz oqishingiz kerak,chunki siz {qwe} yoshsiz")
# else:
#     print(f"Siz ishlashingiz kerak,chunki siz {qwe} yoshsiz")


# def toliq_ism(ism, familiya, otchestva=""):
#     """Functio return fullname"""
#     tq_ism = f"{ism} {familiya}"
#     return tq_ism


# print(toliq_ism("olim", "olimov"))
# student1 = toliq_ism("olim", "olimov")
# student2 = toliq_ism("rashid", "hakimov", "olimov")

# print(f"Dars kelmagan oquvchilar: {student1}, {student2}")


# def inf(kompaniya, model, rang, karobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rang": rang,
#         "karobka": karobka,
#         "yil": yili,
#         "narh": narhi,
#     }
#     return avto


# avto1 = inf("GM", "Malibu", "Qora", "Avtomat", 2020)
# avto2 = inf("GM", "Gentra", "Oq", "Mehanik", 2020, 12000)
# avtolar = [avto1, avto2]
# # print(avtolar)
# print("onlay bozorada mavjud mashinalar")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "No'malum"
#     print(f"{avto['rang']} {avto['model']}. narh {narh}")

# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar 
# print(oraliq(0,10))

# def baholar(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning kiriting:")
#         baholar[ism] = baholar
#     return baholar


# talabalar = ['ali','olim','hasan','husan']
# baholar = baholar(talabalar)
# print(baholar)

# 7868233
def summa(*sonlar):
    """ KIritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    total = 1
    for son in sonlar:
        total *= son
    return total
print(summa(2,3))
def talaba_haqida(ism, familiya, **kwargs):
    malumotlar = {
        'ism': ism,
        'familiya': familiya
    }
    malumotlar.update(kwargs)
    return malumotlar

# Funksiyani chaqirish misoli:
talaba = talaba_haqida('Ali', 'Valiyev', yosh=21, kurs=3, fakultet='Dasturiy injiniring')
print(talaba)
