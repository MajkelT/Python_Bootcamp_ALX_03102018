from threading import Thread    #to daje nam dostęp do klasy WĄTEK
from time import time, sleep
class MyTread(Thread):
    def __init__(self):
        super().__init__()
        pass
    def run(self):     #metoda, która wystąpi kiedy ten wątek wystartujemy
        sleep(4)
        print("Cześć")

watek = MyTread()
watek.start()

print("Hej")
watek.join()    #zawiesza obecny watek, do momentu kiedy watek sie nie skonczy

po = time()
print(po)

