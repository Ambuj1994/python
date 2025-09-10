import random
jackpot = random.randint(1, 50)

guess = int(input('Guess the number '))
while(guess != jackpot) :
  
  if(guess < jackpot) :
    print('Guess higher')
  else :
    print('Guess lower')

  guess = int(input('Guess the number '))


print(' correct number is ', jackpot) 
