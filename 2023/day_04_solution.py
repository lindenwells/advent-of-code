from get_input import get_input
from collections import defaultdict

score = 0
for line in get_input(2023, 4):
    cards = line.split(": ")[1]
    winners, cards_i_have = cards.split(" | ")
    winners = set(map(int, winners.split()))
    cards_i_have = set(map(int, cards_i_have.split()))
    how_many_winners = len(winners.intersection(cards_i_have))

    if how_many_winners == 0:
        continue
    else:
        score += 2 ** (how_many_winners - 1)

cards = defaultdict(int)
for i, line in enumerate(get_input(2023, 4)):
    cards[i + 1] += 1

    for _ in range(cards[i + 1]):
        all_cards = line.split(": ")[1]
        winners, cards_i_have = all_cards.split(" | ")
        winners = set(map(int, winners.split()))
        cards_i_have = set(map(int, cards_i_have.split()))
        how_many_winners = len(winners.intersection(cards_i_have))

        for card_number in range(i + 2, how_many_winners + 1):
            cards[card_number] += 1

def scratch_cards()


print(score)

print(sum(cards.values()))
