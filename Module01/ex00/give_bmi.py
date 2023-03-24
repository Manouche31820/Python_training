import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    try:
        height = np.array(height)
        weight = np.array(weight)
        bmi = list(weight / (height ** 2))
        if (bmi.dtype != np.int64) & (bmi.dtype != np.float64):
            raise AssertionError("Bad type")
        if height.shape != weight.shape:
            raise AssertionError("Bad size")
    except AssertionError as msg_err:
        print(msg_err)
    else:
        return (bmi)
    exit(1)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    return (np.array(bmi) > limit)


if __name__ == '__main__':
    height = [f1, 1.15]
    weight = [165.3, 38.4]

    print(give_bmi(height, weight))
    bmi = give_bmi(height, weight)
    print(apply_limit(bmi, 26))
