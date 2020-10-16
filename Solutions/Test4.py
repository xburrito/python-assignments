import random

amount = int(input("Enter initial amount: "))
original_amount = amount

# Initialize counters
rounds = 0
count = 0

while(True):
  amount = original_amount
  while(True):
    # Deck initialized in an array with 13 cards per suite (x4)
    # Cards [1, 11, 12, 13] will represent [Ace, Jack, Queen, King] respectively
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
    random.shuffle(deck)

    # Represents the hand picking 4 cards and storing in empty array
    choice_4 = []
    for i in range(4):
      index = random.randint(0, 51)
      choice_4.append(deck[index])
    check = 0

    # Check gets set = 1 when a heart suite is pulled. Otherwise remains 0
    for i in choice_4:
      if(i == 10):
        amount = amount + 1
        check = 1
        break

    # Points decrease 
    if(check == 0):
      amount = amount - 1

    # Game ends when the amount is 2x the original amount
    if(amount >= 2 * original_amount):
      count = count + 1
      break

    # Game ends when amount held = 0
    if(amount == 0):
      count = count + 1
      break
    rounds = rounds + 1
  count = count + 1
  if (count == 1000):
    break

print(rounds/1000)