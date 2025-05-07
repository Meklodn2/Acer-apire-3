from art import logo
from random import randint

EASY_LEVEL_TURNs = 10
HARD_LEVEL_TURNs = 5
turns = 0
def check_answer(guess,answer,turns):
    if guess > answer:
        print("Juda baland son")
        return turns - 1
    elif guess < answer:
        print("Juda kichik son")
        return turns - 1
    else:
        print(F"Siz yutdingiz to'g'ri raqam {answer}")    






def set_difficulty():
    level = input("O'yin darajalari easy/hard:")
    if level == 'easy':
        global turns
        return EASY_LEVEL_TURNs
    else:    
        return HARD_LEVEL_TURNs


def game():
    print(logo)
    print("The guues number o'yinga hush kelibsiz!")
    print("1 dan 100gacha raqami o'yladim")
    answer = randint(1,100)
    # print(f"javobi {answer}")
    turns = set_difficulty()
    guess = 0 
    while guess != answer:
        print(f"Raqmi tahmin qilishingiz uchun sizda {turns} ta urunish bor ")
        guess = int(input("Raqamni tahmin qiling: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("sizni tahmin qilsh mkonytiz tugadi ,siz yutqazdingiz!")
            break
        elif guess != answer:
            print("Yana tahmin qiling")    
           
while True:
    game()
    qwe = input("Davom etishni istaysizmi? ha/yo'q: ").lower()
    if qwe != 'ha':
        print("O'yin uchun rahmat! Yana kutamiz.")
        break


