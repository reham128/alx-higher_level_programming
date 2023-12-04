#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    else:
        sLen = len(sentence)
        if sLen > 0:
            return (sLen, sentence[0])
        else:
            return None
