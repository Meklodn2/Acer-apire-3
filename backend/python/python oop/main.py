# class Student():
#     def __init__(self,fname,lname,b_year):
#         self.fname = fname 
#         self.lname = lname
#         self.b_year = b_year

#     def get_name(self):
#         return self.fname

#     def get_lastname(self):
#         return self.lname

#     def full_nmae(self):
#         return f"{self.fname} {self.lname}"

#     def get_age(self,now):
#         return now - self.b_year

#     def tanishtirsh(self):
#         print(f"Ismim {self.fname} {self.lname} {self.b_year} yilda tug'ilgan")


# student1 = Student("John","Doe",2000)
# student2 = Student("Will","Smith",1999)

# # print(student1.fname)
# # print(student2.fname)

# # student1.tanishtirsh()
# # student2.tanishtirsh()
# print(student1.full_nmae())
# print(student1.get_age(2024))














# class User:

#     def __init__(self, full_name, username, email, age=None):
#         self.full_name = full_name
#         self.username = username
#         self.email = email
#         self.age = age

#     def get_info(self):
#         return f"Foydalanuvchi: {self.username}, ismi:{self.full_name}, email:{self.email}"



# user1 = User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com", age=29)
# user2 = User("Aziza Karimova", "azizakarimova", "azizakarimova@gmail.com")

# print(user1.get_info())
# print(user2.get_info())

class Avto():
    def __init__(self,model,rang,karobka,narh,probeg=None):
        self.model = model
        self.rang = rang
        self.karobka = karobka 
        self.narh = narh
        self.probeg = probeg
    def get_info(self):
        return f"{self.model} {self.rang} {self.karobka} {self.narh} {self.probeg}"

avto1 = Avto("Malibu", "Qora", "Avtomat", "37000$" ,"yo'q")
avto2 = Avto("Gentra", "Oq", "Mehanik", "10000$", 12000)

print(avto1.get_info())
print(avto2.get_info())