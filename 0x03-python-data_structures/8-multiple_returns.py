#!/usr/bin/python3
def multiple_returns(sentence):
    sLen = len(sentence)
    if not sentence:
        return (sLen, None)
    else:
        if sLen > 0:
            return (sLen, sentence[0])
        else:
            return None
