# menghitung Leveinsthein Distance

def measure(str1, str2):
    if len(str1) != len(str2):
        return -1
    else:
        dif = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                dif = dif + 0
            else:
                dif = dif + 1
    return dif

print measure('aku', 'aku')
print measure('michael', 'mikhail')
