from collections import Counter
from math import log10,floor
def typetall(tall):
    data = Counter(tall).most_common()
    maks = data[0][1]
    tt = []
    for i,j in data:
        if j == maks:
            tt.append(i)
        else:
            break
    return tt

def gjeldende_siffer(tall,gs=3):
    if type(tall)==int:
        return tall
    return round(tall,max(0,gs-floor(log10(tall))))
