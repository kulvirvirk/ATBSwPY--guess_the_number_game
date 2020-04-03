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

# instructor's solution 
print('Now with instructor\'s solution')
print ('Hello, what is your name?')
name = input()
secret_number = random.randint(1,20) #randint gives you int range including both end points
print('Hello, ' + name +  ', I am thinking of a nubmer between 1 and 20. Take a guess: ')

#only give player 6 tries
for guesses_taken in range(1,7):
  print('take a guess:')
  guess = int(input())
  if guess < secret_number:
    print ('your guess is too low.')
  if guess > secret_number:
    print ('your guess is too high.')
  else: break

if guess == secret_number:
  print ('Good job, ' + name + '! you guessed my number in ' + str(guesses_taken) + ' guesses.')
else:
  print('Nope. The number I was thinking of was ' + str(secret_number))