import random

USER  = 0
COMPUTER  = 1
DRAW = 2
moves = ["rock", "paper", "scissor"]
computer_points = 0
user_points = 0


def get_winner(user, computer):
  if user == computer:
    return DRAW
  # User plays rock and computer plays scissor
  elif user == 0 and computer == 2:
    return USER
  # User plays paper and computer plays rock
  elif user == 1 and computer == 0:
    return USER
  # User plays scissor and computer plays paper
  elif user == 2 and computer == 1:
    return USER
  else:
    return COMPUTER
  
def play(user_input):
  
  # generates 0 or 1 or 2 
  rand_index = random.randint(0,2);
  print("User played : ", moves[user_input])
  print("Computer played : ", moves[rand_index])
  
  return get_winner(user_input, rand_index);

result = ["User won!", "Computer won!", "It was a draw!"]
def driver(user_played):
 
  user_input = user_played
  user_id = 0;
  if user_input == "rock":
    user_id = 0
  elif user_input == "paper":
    user_id = 1
  elif user_input == "scissor":
    user_id = 2
  else:
    print("Invalid input")
    print("Quitting the game")
    exit()
  
  result_id = play(user_id)
  r = result[result_id]
  print(r)
  return result_id
  
  
while(computer_points < 5 and user_points < 5):

  inp = input("Enter move :")
  r = driver(inp) 
  if r == USER:
    user_points += 1
  elif r == COMPUTER:
    computer_points += 1
  
  print("User : ", user_points, " Computer : ", computer_points, "\n\n")

if user_points == 5:
  print("GAME HAS ENDED USER WON")
else:
  print("AI TOO STRONG")
