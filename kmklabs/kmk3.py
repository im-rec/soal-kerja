"""
sum(18989) -> 1 + 8 + 9 + 8 + 9
"""

def sum(digit):
    digit_str = str(digit)
    output = 0
    for i in digit_str:
        output = output + int(i)
    return output

if __name__ == "__main__":
    print sum(1995)


