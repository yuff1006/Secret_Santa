# Secret Santa rules:
# 1. Every player should give one gift to another person other than themselves
# 2. Every player should receive a gift from another person other than themselves
# 3. Selections must be random

import random

players = ["Bill", "Charlie", "Fred", "George", "Ron", "Ginny"]

# generate all possible pairs in tuples
non_repeating_pairs = []
for i in range(len(players)):
    for j in range(len(players)):
        non_repeating_pairs.append((players[i],players[j]))
# in all possible pairs, we don't want any pairs that have the same person, you can't give yourself gifts
non_repeating_pairs = [pairs for pairs in non_repeating_pairs if pairs[0] != pairs[1]]

final_result = []
# we iterate through all players to establish the gifter
for n in range(len(players)):
    # render the pool of giftees for the first gifter
    pool_for_single_gifter = [pairs for pairs in non_repeating_pairs if pairs[0] == players[n]]
    # then choose from these giftees for this gifter
    first_pair = random.choice(pool_for_single_gifter)
    # log the result
    final_result.append(first_pair)
    # after that, the total pool should shrink by eliminating that giftee because they should not be gifted again
    non_repeating_pairs = [pairs for pairs in non_repeating_pairs if pairs[1] != first_pair[1]]

print(final_result)

# this program may have a higher likelihood for traceback the fewer players you have,
# so if it gives out traceback, just run it again
# when it gives traceback, it just means that the program ran out of options given the random choices it made previously, and that's okay!