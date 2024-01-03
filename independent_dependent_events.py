## Probability of Independent and dependent Events

# Sample Space
totalCards = 52
cardsDrawn = 1

# remaining cards when first drawn and not 
# replaced
remCards = totalCards - cardsDrawn

# calculate the joint probability of drawing a king
# after drawing a queen in the first draw
# with replacement
numOfQueens = 4
numOfKings = 4
probKing_1 = numOfKings / totalCards
probQueen_1 = numOfQueens / totalCards

# probability of intersection of event
prob_king_and_queen1 = probKing_1 * probQueen_1

# print probability to 2dp in %
print(f'Probaility of drawing a king and queen with replacement {prob_king_and_queen1 :.6f}')

# probability of drawing a 
# king after drawing a queen
# in the first draw without replacement

prob_king_2 = numOfKings / remCards
prob_queen_2 = numOfQueens / totalCards

prob_king_and_queen2 = prob_king_2 * prob_queen_2
print(f'Probaility of drawing a king after drawing a queen without replacement {prob_king_and_queen1 :.6f}')