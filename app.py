# create game of stone paper scissor which scores and asks player to play again or quit

#import the random module
import random

#create a list of options for 'stone paper scissor' game
options = ['stone', 'paper', 'scissor']

#set the initial score to 0
player_score = 0
computer_score = 0

while True:
    #take input from computer
    computer_choice = random.choice(options)

    #take input from the user
    user_choice = input("Enter your choice (stone/paper/scissor): ")

    #print the choices made by user and computer
    print("You chose: " + user_choice)
    print("Computer chose: " + computer_choice)
    
    #check for the winner of the game
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == 'stone' and computer_choice == 'scissor':
        print("You win!")
        player_score += 1
    elif user_choice == 'paper' and computer_choice == 'stone':
        print("You win!")
        player_score += 1
    elif user_choice == 'scissor' and computer_choice == 'paper':
        print("You win!")
        player_score += 1
    elif user_choice == 'stone' and computer_choice == 'paper':
        print("You lose!")
        computer_score += 1
    elif user_choice == 'paper' and computer_choice == 'scissor':
        print("You lose!")
        computer_score += 1
    elif user_choice == 'scissor' and computer_choice == 'stone':
        print("You lose!")
        computer_score += 1
    else:
        print("You lose!")
        computer_score += 1
    

    #if player choose something else than stone, paper or scissor
    if user_choice not in options:
        print("Invalid choice!")
        player_score -= 1
        
    #print the score of player and computer
    print("Player score: " + str(player_score))
    print("Computer score: " + str(computer_score))

    while True:

      #ask user if he/she wants to play again
     print('Do you want to play again? (y/n): ')
     user_choice = input('Enter your choice: ')
     if user_choice == 'y':
        break
     elif user_choice == 'n':
        print('You chose to quit')
        exit(0)
     else:
      print('Invalid choice')
     continue