import math

def abs_to_db(absolute_value):

    """
    :param absolute_value: list or float.
    :return: Convert absolute value to dB.
    """

    return 10*math.log10(absolute_value)

def db_to_abs(db_value):

    """
    :param db_value: list or float.
    :return: Convert dB to absolute value.
    """

    return 10**(db_value/float(10))

def db_to_neper(db_value):
    
    """
    :param db_value: list or float.
    :return: Convert dB to neper value.
    """
    
    return db_value/4.343
    