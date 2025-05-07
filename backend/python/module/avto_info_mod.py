def avto_info(kompaniya, model, rang, karobka, yil, narhi=None):
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rang": rang,
        "karobka": karobka,
        "yil": yil,
        "narh": narhi,
    }
    return avto

def avto_sell():
    """ Foydalanuvchi avto_info funksiyasi yordamida bir nechya avtolar haqida
     ma'lumotlarini bita ro'yhatga joylash beruvchi funksiya"""
    avtolar = []
    while True:
        print("\nQuyadagi ma'lumotlarni kiriting: ")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("modeli: ")
        rang = input("rang: ")
        karobka = input("karobka: ")
        yil = input("yil: ")
        narh = input("narhi: ")
        # Foydalanuvchi kiritgan malumotlardan avto_info yordamida 
        # lug'at shakillantirib, har bir lug'atni ro'yhatga qo'shmiz
        avtolar.append(avto_info(kompaniya,model,rang,karobka,yili,narhi))

        javob = input("Yana avto qashasizmi ha/yo'q")
        if javob == "yo'q":
            break
        return avtolar

def info_print(avto_info):
    """ Avtomobillar haqida ma'lumot saqlangan luga'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title() } {avto_info['kompaniya'].upper()} "
    f"{avto_info['model'].upper()}  {avto_info['karobka']} karobka , "
    f"{avto_info['yil']}-yil {avto_info['narh']}$"
    )