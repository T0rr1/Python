import random

# your sentence is assigned to the variable
sentence = input().split()
random.seed(43)
# write your python code below
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))
