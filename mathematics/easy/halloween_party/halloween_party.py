def halloweenParty(k):
    # For an even k, split the cuts equally between horizontal and vertical.
    if k % 2 == 0:
        cuts_per_side = k // 2
        return cuts_per_side ** 2

    # For an odd k, one direction gets one extra cut to maximize the pieces.
    return ((k // 2) + 1) * (k // 2)