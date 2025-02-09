#RPS.py
#Name: Brandon Jergensen
#Date: 2/9/25
#Assignment: RPS.py
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  while True: 
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( ["R", "P", "S"])
  
  #Prompt the user for their RPS selection
    player = input("pick your weapon (R, P, S):")

    if player not in ["R", "P", "S"]:
      print("Quit playin' and pick R, P, or S.")

  #Determine winner and state what happened to the user
    if computer =="R":
      print ("Computer Chose Rock")
    elif computer =="P":
      print ("Computer chose Paper")
    else:
      print ("Computer chose Scissors")

    if player == computer:
      print("Tie")
      ties = ties + 1
    if player == "R" and computer == "S":
      print("You win!")
      wins = wins + 1
    if player == "P" and computer == "R":
      print("You win!")
      wins = wins + 1
    if player == "S" and computer == "P":
      print("You win!")
      wins = wins + 1
    if player == "R" and computer == "P":
      print("You lose!")
      losses = losses + 1
    if player == "P" and computer == "S":
      print("You lose!")
      losses = losses + 1
    if player == "S" and computer == "R":
      print("You lose!")
      losses = losses + 1

    play_again = input("Would you like to play again? (Y/N): ").upper()
    if play_again != "Y":
      break
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
