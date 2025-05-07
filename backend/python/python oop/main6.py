class Avto:
    _num_avto = 0
    def __init__(self,make,model,rang,yil,narx):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        Avto._num_avto += 1
    def GetNumAvto(self):
        print(self._num_avto)
    
    def __repr__(self):
        return f"Avto: {self.rang} {self.make} {self.model}"


    def __str__(self):
        return f" Avtomobil zavodi: {self.make}\nAtomobil modeli: {self.model}"






avto1 = Avto("GM","Cobalt","Oq",2020,40000)
avto2 = Avto("GM","Malibu","Qora",2030,60000)
print(avto2)
print(str(avto2))
print(repr(avto2))