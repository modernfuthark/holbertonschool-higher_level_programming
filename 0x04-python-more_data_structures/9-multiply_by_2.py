#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictionary = a_dictionary.copy()
    for i in newDictionary:
        newDictionary[i] *= 2
    return (newDictionary)
