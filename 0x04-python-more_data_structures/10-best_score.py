#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return (None)
    top = list(a_dictionary.keys())[0]
    for i in a_dictionary:
        if a_dictionary[i] > a_dictionary[top]:
            top = i;
    return (top)
