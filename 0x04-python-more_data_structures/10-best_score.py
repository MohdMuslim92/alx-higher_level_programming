#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_dictionary = dict(sorted(a_dictionary.items(), key=lambda x: x[1]))
    keys_list = list(sorted_dictionary.keys())
    best = keys_list[-1]
    return best
