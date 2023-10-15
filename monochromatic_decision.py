import numpy as np

def decide_if_monochromatic(avarage_values: list[np.array]) -> bool:
    """
    Function expects list of np.array object which has values 
    of avarage pixel in given clothing.

    It will take under consideration only 2 first objects supplied.
    """
    tolerance = 25
    obj1, obj2 = avarage_values
    if ((obj1[0]-obj2[0])**2 + (obj1[1]-obj2[1])**2 + (obj1[2]-obj2[2])**2) <= tolerance**2:
        return True
    return False
