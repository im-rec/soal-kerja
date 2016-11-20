# memutar kata

'''
input -> "The quick brown fox jumped over the lazy dog."
output -> "dog. lazy the over jumped fox brown quick The"
'''

def reverse(stc):
    wd = stc.split()
    stc_rev = ''
    for i in range(len(wd)):
        stc_rev = wd[i] + ' ' + stc_rev
    return stc_rev

print reverse("The quick brown fox jumped over the lazy dog.")
