import random, time, os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    guesses = []
    random_number = random.randint(1,10)
    while True:
        try:

            guess = int(input("guess (between 1 and 10): "))
            if guess in guesses:
                print("You've made this prediction before")
                continue
            else:
                if guess == random_number:
                    print("You win Congratulations")
                    time.sleep(transition_time)
                    Welcome_screen()
                    break
                elif guess > random_number:
                    print("make a smaller guess")
                    guesses.append(guess)
                elif guess < random_number:
                    print("make a Bigger guess")
                    guesses.append(guess)
        except ValueError:
            print("wrong choice!")
            time.sleep(transition_time)
            clear_console()
            continue
            
            
def settings_menu():
    clear_console()
    global transition_time
    print("Type the number you want to change the transition time between menus. By default, it is set to 1 second.")
    try:
        transition_time = float(input("Choice (I.E. 0.5): "))
        if transition_time != "":
            Welcome_screen()
    except ValueError:
        print("wrong choice!")
        time.sleep(transition_time)
        settings_menu()
    
def Welcome_screen():
    clear_console()
    print("Welcome to random number guess game ")
    choice = input("Choose one of the following\n1.Next game\n2.Settings\n3.Exit\nchoice: ")
    if choice == "1":
        print("You will be directed to the game menu.")
        time.sleep(transition_time)
        clear_console()
        game()
    elif choice == "2":
        settings_menu()
    elif choice == "3":
        clear_console()
        exit
    else:
        print("wrong choice!")
        time.sleep(transition_time)
        Welcome_screen()

transition_time = 1
Welcome_screen()
