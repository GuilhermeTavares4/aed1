def add_guessed_char(guess):
    if guess not in guessed_letters:
        guessed_letters.append(guess)
        check_guess(guess)
        print(hidden_word)
    else:
        print("jÁ DIGITOU ESSA LETRA.")

def generate_hidden_word():
    hidden_word = ""
    i = 0
    while i < len(word):
        hidden_word += "_"
        i += 1
    return hidden_word

def check_guess(guess):
    global hidden_word
    hidden_word_list = string_to_list(hidden_word)
    correct = False
    i = 0
    while i < len(word):
        if guess == word[i]:
            hidden_word_list[i] = guess
            global correct_guesses
            correct_guesses += 1
            correct = True
        i += 1
    if correct == False:
        global hp
        hp -= 1
    hidden_word = list_to_string(hidden_word_list)
    

def string_to_list(string):
    new_list = []
    for i in string:
        new_list.append(i)
    return new_list



def list_to_string(list_):
    string = ""
    for i in list_:
        string += i
    return string


word = "animal"
hp = 6
correct_guesses = 0
guessed_letters = []
hidden_word = generate_hidden_word()

while correct_guesses < len(word) and hp > 0:
    guess = input(f"Digite uma letra para adivinhar a palavra. Você tem {hp} vidas: ")
    add_guessed_char(guess)

if hp > 0:
    print("Parabéns, você acertou a palavra! 😃")
else:
    print("Lixo porco feio tenha vergonha de sua existência.")