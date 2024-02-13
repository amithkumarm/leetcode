def calculate_median(num1, num2):
    num3 = num1 + num2
    num3.sort()
    if len(num3) % 2 != 0:
        return float(num3[len(num3) // 2])
    else:
        return (num3[len(num3) // 2] + num3[(len(num3) // 2 - 1)]) / 2
