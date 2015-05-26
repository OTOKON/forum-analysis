import numpy as np

def dict_cosine(d1, d2):
    intersection = set(d1.keys()) & set(d2.keys())
    numerator = sum([d1[x] * d2[x] for x in intersection])

    sum1 = sum([d1[x]**2 for x in d1.keys()])
    sum2 = sum([d2[x]**2 for x in d2.keys()])
    denominator = np.sqrt(sum1) * np.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator