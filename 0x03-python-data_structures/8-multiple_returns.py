#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        return 0, None
    w = len(sentence)
    x = sentence[:1]
    return w, x
