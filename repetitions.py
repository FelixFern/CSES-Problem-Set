#https://cses.fi/problemset/task/1069
dna = str(input())
now = 1
maks = 0
for i in range(len(dna)):
    if i == len(dna)-1:
        pass
    elif dna[i] == dna[i+1]:
        now += 1
    else:
        if maks <= now:
            maks = now
            now = 1
        else:
            now = 1
if maks <= now:
    maks = now

print(maks)