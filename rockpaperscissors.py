from random import randint

#list of play options
play = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = play[randint(0,2)]
print('Computer: {}'.format(computer))

#get the user input
player = input("Rock, Paper, Scissors? ")
print('Player: {}'.format(player))
