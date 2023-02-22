
# z1

import threading

lock = threading.Lock()

class thread(threading.Thread):
    def __init__(self, thread_nr):
        self.nr = thread_nr
        threading.Thread.__init__(self)

# tworze klase watku
# definiuje jego dzialanie

    def run(self):
        global lock
        lock.acquire()
        for i in range(9):
            n = 10 * self.nr + i
            numbers.append(n)
        lock.release()

numbers = []

if __name__ == "__main__":

# tworze obiekty klasy

    w0 = thread(0)
    w0.start()

# wlaczam watki

    w1 = thread(1)
    w1.start()

    w2 = thread(2)
    w2.start()

    w3 = thread(3)
    w3.start()

# kazdy watek czeka na skonczenie dzialania poprzedniego

    w0.join()
    w1.join()
    w2.join()
    w3.join()

# drukuje liczby

    print(numbers)

# z2

import threading
from time import sleep
import urllib.request

class download(threading.Thread):

    def __init__(self, urlslist, counted):
        self.urls = []
        self.urls = urlslist
        self.c = []
        self.c = counted
        threading.Thread.__init__(self)

    def run(self):
        t = []

        print("Rozpoczynanie pobierania...")
        for i in self.urls:
            with urllib.request.urlopen(i) as f:
                c = len(f.read())
                t.append(c)
                print("Liczba znaków dla {}: ".format(i), c)

            t = self.c

if __name__ == '__main__':
    urls = []
    new_counted = []

    url1 = input("Podaj URL 1: ")
    url2 = input("Podaj URL 2: ")
    url3 = input("Podaj URL 3: ")
    url4 = input("Podaj URL 4: ")
    url5 = input("Podaj URL 5: ")

    urls.append(url1)
    urls.append(url2)
    urls.append(url3)
    urls.append(url4)
    urls.append(url5)

    d1 = download(urls, new_counted)

    d1.start()

    while download.is_alive(d1):
        sleep(1)
        print("Oczekiwanie na zakończenie pobierania...")
    else:
        print("Wszystko pobrano.")

    d1.join()


# z3

import threading
import uuid
import hashlib

class summed(threading.Thread):

# inicjuje tablice do hashowania

    def __init__(self, hashed):
        self.ha = []
        self.ha = hashed
        threading.Thread.__init__(self)

# konwertuje liste wygenerowanych w glownym watku liczb na bajty dla potrzeb funkcji md5()
# obliczam sumy przedstawien bajtowych i dodaje je do listy

    def run(self):
        for i in uid_list:
            byte = i.encode()
            r = hashlib.md5(byte)
            m = r.hexdigest()
            self.ha.append(m)

if __name__ == '__main__':
    uid_list = []
    new_list = []

# tworze 200 elementow za pomoca funkcji uuid4() z biblioteki uuid
# konwertuje je do typu int dla potrzeb funkcji hex()
# dodaje je do listy

    for n in range(200):
        x = int(uuid.uuid4())
        h = hex(x)
        uid_list.append(h)

    s1 = summed(new_list)

# wlaczam watek

    s1.start()

    s1.join()

# spinam dwie listy

    assigned = zip(uid_list, new_list)

# wyswietlam pary

    for j, (uid_list, new_list) in enumerate(assigned):
        print(uid_list, " - ", new_list)