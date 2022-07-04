import random 
number = random.randint(1,10)



breaker = ("-"*93)

title = ("Welcome to the RANDOM NUMBER GUESSING GAME")
title_print = title.center(93)
print(title_print)
print(breaker,"\n")
print("This is a game where players can guess a random number between one and 10, to do this they are given 5 tries. If you take more than 5 tries it's game over\n ")
print(breaker)

chance = 0

while chance <= 5:
  print(number)
  guess = int(input("What number would you like to guess: "))
  chance += 1
  while guess != number:
    print("Sorry but that was incorrect, please try again")
    print(breaker)
    guess = int(input("What number would you like to guess: "))
    chance += 1
    if chance>5 and guess != number: 
      print(breaker)
      print("Sorry you have used all your guesses")
      print("The answer was",number)
      break
  if guess == number: 
    print("Well done, you guessed correctly")


  
  