## soal 2
def naik(n, u, d):
    p = 0
    i = 0
    while p < n:
        p = p + u
        i = i + 1
        if p >= n:
            print(i)
            break
        p = p - d
        i = i + 1

naik(7, 2, 1)
naik(10, 5, 2)
