from collections import Counter
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
