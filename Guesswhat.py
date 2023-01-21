def Guess_Game():
    import random
    Num=[20,30,10,34,54,21,34,32,13,32,45]
    c=random.choice(Num)
    int(c)
    att=5
    """
    Scope of improvement:
    1)instead of attempt done try printing chances left
    2)Try printing "Sorry you failed to guess the No. which was {computers guessed no}"
    """
    
    print(f"Welcome To guess the No. Game\n In order to win you need to guess the computers choice of no. ranging from 0-60.\n you will be given 5 attempts for each game then the game will exit automatically you will be guided on each step for your guess enjoy Gaming!.")
    n=int(input("Enter Your Guess:"))
    for i in range(1,att+1):
        if n>c:
            print("The No is less than input")
            print(f"Attempt Done {i}")
            n=int(input("Enter Your Guess:"))
            continue

        elif n<c:
            print("The No is Greater than Input")
            print(f"Attempt Done {i}")
            n=int(input("Enter Your Guess:"))
        elif n==c:
            print("Congratulations you Guessed Right")
            break
Guess_Game()