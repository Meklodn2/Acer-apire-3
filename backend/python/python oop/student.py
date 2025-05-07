class Student():
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f" {self.ism} {self.familiya} {self.bosqich}-bosqich talabasi"


    def set_bosqich(self):
        """Talaba kursini yangilovchi metod"""
        self.bosqich = bosqich
    def update_bosqich(self):
        self.bosqich += 1
talaba1 = Student("Anvar" , "Hakimov",2000)

print(talaba1.get_info())

class Fan:
    def __init__(self,): 