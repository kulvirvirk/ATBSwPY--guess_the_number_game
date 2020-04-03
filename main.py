# 1. ask the players name and greet them
# 2. generate a random number
# 3. ask player to select the number between 1 to 20
# 4. write a loop to through players input 
# 5. add if statements to compare input with random number 
# 6. add counter to count the tries
# 7. print output with congratulations message and number of tries. 

import random
player_name = input('Hello, what is your name? ')

print('Hi ' + player_name + '!')

#generate random number
random_number = random.randrange(1, 11)

player_guess = int(input('I am thinking of a nubmer between 1 and 20. Take a guess: '))

counter = 0
while player_guess != random_number:
  counter = counter + 1
  if player_guess > random_number:
    player_guess =int(input('Your guess is too high. Take a guess again:'))
  elif player_guess < random_number:
    player_guess =int(input('Your guess is too low. Take a guess again:'))

counter = str(counter)
print('Congratulations, ' + player_name + ', it took you ' + counter + ' tries!')
print('Good job!')

