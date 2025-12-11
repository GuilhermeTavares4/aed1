from random import randint

def shuffle(deck):
    for i in range(len(deck) - 1, 1, -1):
        random_pos = randint(0, i - 1)
        temp = deck[i]
        deck[i] = deck[random_pos]
        deck[random_pos] = temp


def main():
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = []
    
    for suit in suits:
        for rank in ranks:
            card = {rank: suit}
            deck.append(card)
    
    shuffle(deck)
    for card in deck:
        for key, value in card.items():
            print(f'{key}: {value}')


main()
