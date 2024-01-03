#!/usr/bin/python3
"""validation of utf-8"""


def validUTF8(data):
    """
    Determines if a data set that is given
    represents a valid utf-8 encoding
    """
    n_byt = 0

    rep_1 = 1 << 7
    rep_2 = 1 << 6

    for a in data:

        mask_byte = 1 << 7

        if n_byt == 0:

            while mask_byte & a:
                n_byt += 1
                mask_byte = mask_byte >> 1

            if n_byt == 0:
                continue

            if n_byt == 1 or n_byt > 4:
                return False

        else:
            if not (a & rep_1 and not (a & rep_2)):
                return False

        n_byt -= 1

    if n_byt == 0:
        return True

    return False
