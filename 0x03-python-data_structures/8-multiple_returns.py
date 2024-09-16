#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    tuple_sentence = (len(sentence), first_char)
    return (tuple_sentence)
