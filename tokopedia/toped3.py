inputs = raw_input()
def sim(inputs):
    inputs.lower()
    sum = 0
    k = len(inputs)
    for x in range(k):
        for y in range(x + 1):
            if inputs[(k - 1 - x):][y] == inputs[y]:
                sum = sum + 1
    return sum

print sim(inputs)
