#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    bestScore = 0
    winner = None
    for k, v in a_dictionary.items():
        if v > bestScore:
            bestScore = v
            winner = k
    return (winner)
