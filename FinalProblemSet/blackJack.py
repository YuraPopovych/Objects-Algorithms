def next_move(cards):
    totalPoints = 0
    cardsPoints = {
        'A': 1,
        'J': 10,
        'Q': 10,
        'K' : 10
    }
    aceRange = list( range(17, 22) )
    cards = cards.upper()
    for card in cards:
        if card.isalpha():
            if card == 'A':
                if totalPoints + 11 in aceRange:
                    totalPoints += 11
                else:
                    totalPoints += cardsPoints[card] 
            else:
                totalPoints += cardsPoints[card]
        else:
            if int(card) == 0:
                totalPoints += 10
            else:
                totalPoints += int(card)
    if totalPoints > 21:
        return "Bust"
    if totalPoints >= 17:
        return "Stay"
    return "Hit" 


print(next_move("90"))
print(next_move("AA305"))




