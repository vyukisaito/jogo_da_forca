word = 'chute'
chances = 5
chances_parameter = chances
your_guess = []
one_letter = ''


while True:

    for letter in word:
        if letter.lower() in your_guess:
            print(letter, end=' ')
        else:
            print('_ ', end='')
    print()
        
    if one_letter in word:
        chances = chances
    else:
        chances -= 1
        del your_guess[-1]

    if len(your_guess) == len(word):
        print(f"Parabéns você acertou!")
        break

    if chances == 0:
        print(f"Você perdeu! A palavra era {word}")
        break

    print(f"Você tem {chances} chances")
    one_letter = input("Digite uma letra: ")
    your_guess.append(one_letter)

