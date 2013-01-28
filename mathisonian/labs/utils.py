def int_str(val, keyspace):
    """ Turn a positive integer into a string. """
    assert val >= 0
    out = ""
    while val > 0:
        val, digit = divmod(val, len(keyspace))
        out += keyspace[digit]
    return out[::-1]


def str_int(val, keyspace):
    """ Turn a string into a positive integer. """
    out = 0
    for c in val:
        out = out * len(keyspace) + keyspace.index(c)
    return out


def chaffify(val, chaff_val=87953):
    """ Add chaff to the given positive integer. """
    return val * chaff_val


def dechaffify(chaffy_val, chaff_val=87953):
    val, chaff = divmod(chaffy_val, chaff_val)
    if chaff != 0:
        raise ValueError("Invalid chaff in value")
    return val
