from threading import Thread
from urllib.request import urlopen
from time import time, sleep

class MyTread(Thread):
    def __init__(self):
        super().__init__()
        pass
    def run(self):
        with urlopen(f"https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
            print(file.read())

przed = time()

watki = []
for i in range(10):
    watek = MyTread()
    watek.start()
    watki.append(watek)    # w tym momencie wystartujemy 10 wątków

for watek in watki:
    watek.join()        # wątki trzeba odbierać (wynika z architektury komputera)

po = time()
print(f"czas: {po - przed}s")

