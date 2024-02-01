#!/usr/bin/python3
"""
a method that determines if a given data set represents a
valid UTF-8 encoding.
"""


def validUTF8(data):
    """Determines if a given data set represents a valid utf-8 encoding"""
    number_bytes = 0

    for byte in data:
        mask = 1 << 7  # Start with the leftmost bit

        if number_bytes == 0:
            while mask & byte:
                number_bytes += 1
                mask >>= 1  # Shift the mask to the right

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            mask_1 = 1 << 7
            mask_2 = 1 << 6

            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        number_bytes -= 1

    return number_bytes == 0
