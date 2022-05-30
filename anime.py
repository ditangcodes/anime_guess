import a_functions
title = "bleach"


while True:
    try:
        count = 1

        guess = 'Guess the anime: '
        guess = input(guess)
        if guess == title:
            count += 1
            print('Correct')
            print(f'Attempts were {count}')
            break

        elif guess != title:
            print('Try again here is a hint: ')
            count += 1
            guess2 = str(input("Guess again: "))
            if guess2 == title:
                print("Nice job on the second attempt!")
                print(f'Attempts were {count}')
                break
            elif guess2 != title:
                print("Wrong again homie! ")
                count += 1
                guess3 = str(input("One last try: "))
                if guess3 == title:
                    count += 1
                    print("Well done on the third attempt! ")
                    print(f'Attempts were {count}')
                    break
                else:
                    print("The answer was: ", title)
    except ValueError as ve:
        print("Incorrect input, Error" + str(ve))

