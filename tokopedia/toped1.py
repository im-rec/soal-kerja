## soal 1
n = input()

for i in range(n):
    print '0 ' * (i) + ' '.join(map(str, range(i + 1, n + 1)))

'''
contoh input -> 5
contoh output ->
1 2 3 4 5
0 2 3 4 5
0 0 3 4 5
0 0 0 4 5
0 0 0 0 5
'''
