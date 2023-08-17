from collections import Counter
values = {"1" : 1, "2" : 2, '3' : 3, '4' : 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, "T" : 10, "J": 11, "Q": 12, "K":13, "A":14}
def evaluate(cards):
    sortedCards = sorted([values[cards[i][0]] for i in range(len(cards))])
    if all(c[1] == cards[0][1] for c in cards):
        if all(sortedCards[i] == sortedCards[i - 1] + 1 for i in range(1, len(sortedCards))):
            if 13 in sortedCards:
                return 10, sortedCards
            return 9, sortedCards
        return 6, sortedCards
    if all(sortedCards[i] == sortedCards[i - 1] + 1 for i in range(1, len(sortedCards))):
        return 5, sortedCards
    if any(sortedCards.count(c) == 4 for c in sortedCards):
        return 8, sortedCards
    if any(sortedCards.count(c) == 3 for c in sortedCards):
        if any(sortedCards.count(c) == 2 for c in sortedCards):
            return 7, sortedCards
        return 4, sortedCards
    if any(sortedCards.count(c) == 2 for c in sortedCards):
        if len(set(sortedCards)) == 3:
            return 3, sortedCards
        return 2, sortedCards
    return 1, sortedCards

def PE054():
    wins = 0
    hands = open("PE054.txt").read().splitlines()
    for game in hands:
        game = game.split(' ')
        p1, p2 = game[:5], game[5: ]
        p1, sortedp1 = evaluate(p1)
        p2, sortedp2 = evaluate(p2)
        sortedp2.reverse()
        sortedp1.reverse()
        if p1 > p2:
            wins += 1
        if p1 == p2:
            if p1 == 1:
                if sortedp1 > sortedp2:
                    wins += 1
            else:
                if int(Counter(sortedp1).most_common(1)[0][0]) > int(Counter(sortedp2).most_common(1)[0][0]):
                    wins += 1
    return wins
print(PE054())