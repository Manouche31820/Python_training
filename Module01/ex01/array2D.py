import numpy as np
def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes a list `family`, an integer `start`, and an integer `end` as arguments.
    It returns a slice of the `family` list from the `start` index to the `end` index.
"""
    try:
        if isinstance(family, list) != True or isinstance(start, int) != True or isinstance(end, int) != True:
            raise AssertionError ("Bad type")
        family = np.array(family)
    except AssertionError as msg_err:
        print(msg_err)
    except ValueError as msg_err:
        print(msg_err)
    else:
        print("My shape is :", family.shape)
        family = family[start:end]
        print("My new shape is :", family.shape)
        return (family.tolist())

if __name__ == '__main__':
    from array2D import slice_me
    family = [[1.80, 78.4, 1923],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    # print(slice_me(family, 1, -2))
