def first_missing_positive(x):
    x.sort()
    l = len(x)
    i = 0
    res = [ele for ele in x if ele > 0]
    missing_positive = 1
    for j in res:
        if missing_positive == j:
            missing_positive += 1
        elif j > missing_positive:
            return missing_positive
    return missing_positive
