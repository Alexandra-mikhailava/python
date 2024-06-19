import os

name = input("Введите ваше имя: ")
print('Здравствуйте,', name, '! Это игра "Кто хочет стать миллионером".')
input("Нажми Enter чтобы продолжить")

os.system('cls||clear')
bank = 0

# Define the questions and answers
questions = [
    {"q": "столица Франции?", "a": ["А: Париж", "Б: Токио", "В: Барселона", "Г: Москва"], "correct": "А"},
    {"q": "жук?", "a": ["А: краб", "Б: рыба", "В: дуб", "Г: море"], "correct": "В"},
    {"q": "птица?", "a": ["А: аист", "Б: брест", "В: жук", "Г: ля"], "correct": "Г"},
]

# Loop through each question
for question in questions:
    print(question["q"])
    for answer in question["a"]:
        print(answer)
    
    ans = input("Ваш ответ: ").upper()  # Get the user's answer and convert to uppercase
    
    if ans == question["correct"]:
        bank += 1000  # Add 1000 to the bank if the answer is correct
        print("Ответ верный!")
    else:
        print("Ответ неверный! Игра окончена.")
        print("Твой выигрыш: " + str(bank))
        exit()  # Exit the game if the answer is wrong
    
    input("Нажми Enter чтобы продолжить")
    os.system('cls||clear')

print("Поздравляю! Вы ответили на все вопросы правильно!")
print("Твой итоговый выигрыш: " + str(bank))
