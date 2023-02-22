
# z1

from multiprocessing import cpu_count
# wyswietlam liczbe procesorow uzywajac funkcji
cpu_count()
cpus = cpu_count()
if __name__ == '__main__':
    print("liczba procesorow: ", cpus)

# z2

import os
from multiprocessing import Process

def print_id(proc_nr):
    print(proc_nr)
    print("pid: ", os.getpid())

def first_process(proc):
    print_id(proc)

if __name__ == '__main__':
    print("proces glowny: ", os.getpid())

# tworze procesy, wyswietlajace swoje id z uzyciem funkcji z biblioteki os

    p1 = Process(target=first_process, args=("pierwszyproces",))
    p2 = Process(target=first_process, args=("drugiproces",))

    p1.start()
    p1.join()

    p2.start()
    p2.join()