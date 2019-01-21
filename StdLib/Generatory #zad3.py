def wypisz_samogloski(napis):
    for litera in napis:
        if litera in "aeiouy":
            yield litera

for litera in wypisz_samogloski("ala ma kota a kot ma ale"):
    print(litera)
