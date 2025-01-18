# Open the file cards.py, and write a function that takes as arguments 
# a list of suits and a list of ranks. Inside the function create the 
# list of the deck and return a random group of 4 cards.
# The output should be in the format of <rank>-<suit>, e.g Jack-Hearts

# Add imports here
import random
import numbers

# Complete the function
def cards_sample(suits, ranks):
    result = []
    for s in suits:
        for r in ranks:
          mychoiceRank = random.choice(ranks)
          if isinstance(mychoiceRank, numbers.Number):
            continue
          else:
            test = mychoiceRank + "-" + s
            if test not in result:
                result.append(test)
                break
    return result

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ['Jack', 'Queen', 'King']

print(cards_sample(suits, ranks))
