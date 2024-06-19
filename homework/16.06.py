import time
import os


zero = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]
one = [
    "      ⬛⬛⬛",
    "      ⬛⬛⬛",
    "      ⬛⬛⬛",
    "      ⬛⬛⬛",
    "      ⬛⬛⬛",
    "      ⬛⬛⬛",
    "      ⬛⬛⬛"
]
two = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛          ",
    "⬛⬛⬛          ",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]
three = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]
four = [
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛"
]
five = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛          ",
    "⬛⬛⬛          ",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]
six = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛          ",
    "⬛⬛⬛          ",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]
seven = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛"
]
eight = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]
nine = [
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛      ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
    "          ⬛⬛⬛",
    "          ⬛⬛⬛",
    "⬛⬛⬛⬛⬛⬛⬛⬛⬛"
]
colon = [
    "   ",
    " ⬛⬛⬛",
    " ⬛⬛⬛",
    "   ",
    " ⬛⬛⬛",
    " ⬛⬛⬛",
    "   "
]

digits = {
    '0': zero,
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
    ':': colon
}

def get_graphical_time(current_time):
    graphical_lines = [""] * 7
    for char in current_time:
        graphical_char = digits[char]
        for i in range(7):
            graphical_lines[i] += graphical_char[i] + "  "  
    return graphical_lines

def display_time():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        current_time = time.strftime("%H:%M:%S")
        graphical_time = get_graphical_time(current_time)
        for line in graphical_time:
            print(line)
        time.sleep(1)

display_time()
