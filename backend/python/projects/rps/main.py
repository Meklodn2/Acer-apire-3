import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.(___)
'''

game = [rock,paper,scissors]
userchoise = int(input("Rock: 0, Paper: 1, Scisors: 2:"))
print(game[userchoise])


pc_choise = random.randint(0,2)
print("pc_choise:")
print(game[pc_choise])
if userchoise >= 3 or userchoise < 0:
    print("siz notogri raqam taladingiz!")
elif userchoise == 0 and pc_choise == 2:
    print("harosh")    
elif pc_choise == 0 and userchoise == 2:
    print("e latta bot")    
elif userchoise > pc_choise:
    print("harosh")    
elif pc_choise > userchoise:
    print("e latta bot")   
elif pc_choise == userchoise:
    print("teng")




































# #randint - ключевой соз

# import random

# rand = random.randint(1,100)
# print(f"your random game score:{rand}%")


