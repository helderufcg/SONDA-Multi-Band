import math

def abs_to_db(absolute_value):

    """
    :param absolute_value: list or float.
    :return: Convert absolute value to dB.
    """

    db_value = 10*math.log10(absolute_value)
    return db_value

def db_to_abs(db_value):

    """
    :param db_value: list or float.
    :return: Convert dB to absolute value.
    """

    absolute_value = 10**(db_value/float(10))
    return absolute_value 

def db_to_neper(db_value):
    
    """
    :param db_value: list or float.
    :return: Convert dB to neper value.
    """
    
    np_value = db_value/4.343
    return np_value
    