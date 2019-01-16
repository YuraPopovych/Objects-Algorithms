
def check_horse_winner(players):
    winners = []
    losers = []
    message  = "Players "

    if len(players) == 0:
        return

    for player_index in range( len(players) ):
        player = players[player_index]
        if len(player) == 5:
            losers.append(player_index)
        else:
            winners.append(player_index)
    if len(losers) == 0:
        return "Everyone: keep playing!"
    
    if len(winners) == 1:
        return "Player {0} wins!".format( str(winners[0]) )

    for winner_index in range( len(winners) - 1  ):
        winner = winners[winner_index]
        message += str( winner )  + ", "
    message += str(winners[-1]) + ": keep playing!"

    return message

print(check_horse_winner(("HOR", "HORS", "H", "HO")))
print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))

