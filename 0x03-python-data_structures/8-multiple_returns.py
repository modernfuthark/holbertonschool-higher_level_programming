#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        data = (0, None)
    else:
        data = (len(sentence), sentence[0])
    return (data)
