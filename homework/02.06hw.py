import os
name = input("Введите ваше имя: ")
print ('Здравствуйте,', name, '! Это игра "Кто хочет стать миллионером".')
input("Нажми Enter чтобы продолжить")
input()
os.system('cls||clear')
bank = 0
questions = {"q1" : "столица Франции?", "q2" : "5 + 3 =?", "q3": "что из этого насекомое?"}
answers = {"a1" : "А: Париж, Б: Токио, В: Барселона, Г: Москва", "a2" : "А: 4, Б: 6, В: 8, Г: 12", "a3" : "А: Таракан, Б: Лебедь, В: Медведь, Г: Собака"}  
print(questions["q1"])
print(answers["a1"])
answer_for_q1 = input("Введите ответ ")
if answer_for_q1 == "А" or answer_for_q1 == "а" :
    print("Ответ верный")
    bank += 1000
else :
    print ("Ответ неверный! Игра окончена.")
    print ("твой выигрыш : " + str(bank))
    exit()
os.system('cls||clear')      
print(questions["q2"])
print(answers["a2"])
answer_for_q2 = input("Введите ответ ")
if answer_for_q2 == "В" or answer_for_q2 == "в" :
    print("Ответ верный")
    bank += 10000
else :
    print ("Ответ неверный! Игра окончена.")
    print ("твой выигрыш : " + str(bank))
    exit()
os.system('cls||clear')
print(questions["q3"])
print(answers["a3"])
answer_for_q3 = input("Введите ответ ")
if answer_for_q3 == "А" or answer_for_q3 == "а" :
    bank += 20000
    print("Ответ верный! Твой выигрыш:" + str(bank) )   
else :
    print ("Ответ неверный! Игра окончена.")
    print ("твой выигрыш : " + str(bank))
    exit()
os.system('cls||clear')