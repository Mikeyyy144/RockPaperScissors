import random
is_running = True
while is_running:

    user_response = input("Pick 'R' for Rock, 'P' for Paper, 'S' for Scissors: ")
    rock_paper_scissors = ["R", "P", "S"]
    
    if user_response in rock_paper_scissors:
        True

        computer_response = random.choice(rock_paper_scissors)
        print(f"\nPlayer({user_response}) : CPU({computer_response})\n")

        if user_response == computer_response:
            print(f"Both players selected {user_response}. It's a tie!")
        elif user_response == "R":
            if computer_response == "S":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_response == "P":
            if computer_response == "R":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_response == "S":
            if computer_response == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        
        print("Thanks for playing")
        break

    else:
        print("Invalid response, Enter a valid option: ")
    
