## Calculating probability of events
##Frequentist Approach

# Sample Space
numOfCards = 52

# Favorable Outcomes
numOfAces = 4

numOfHearts = 13
numOfDiamonds = 13


# P(x) = favorable outcomes / sample space
probAce = numOfAces / numOfCards

probRedCard = (numOfHearts + numOfDiamonds) / numOfCards

# Print probability rounded to 2dp
print(f'The probability of getting an ace = {round(probAce, 3)}')
print(f'The probability of getting a red card = {round(probRedCard, 3)}')

# probability in %
probAce_ = probAce * 100
probRedCard_ = probRedCard * 100
print(f"Proabiility of an Ace in % : {probAce_:.2f}%")
print(f"Proability of a Red card in %: {probRedCard_:.2f}%")