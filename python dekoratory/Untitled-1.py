"""
Schröder Paweł
ZTPwJP informatyka N II rok L_II_NW_INFI_K7b

L5

"""

# z1


def hello(f):
    def display():
        print("hello")
        f()

    return display


@hello
def moja_funkcja():
    print("moja funkcja")


moja_funkcja()

# z2
start = perf_counter()


def deco(f):
    def wyraz(*args):
        return f(*args)

    return wyraz


@deco
def tetra(n):
    if n == 3:
        return 2
    elif n == 2 or n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return tetra(n - 1) + tetra(n - 2) + tetra(n - 3) + tetra(n - 4)


print(tetra(8))
end = perf_counter()
print(end - start)

# z3

from time import perf_counter

start1 = perf_counter()


def cache(f):
    wyrazy = {}

    def czy_obecny(*args):
        if args in wyrazy:
            return wyrazy[args]
        wynik = f(*args)
        wyrazy[args] = wynik
        return wynik

    return f


@cache
def tetra_cache(n):
    if n == 3:
        return 2
    elif n == 2 or n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return tetra_cache(n - 1) + tetra_cache(n - 2) + tetra_cache(n - 3) + tetra_cache(n - 4)


print(tetra_cache(8))
end1 = perf_counter()
print(end1 - start1)


# z4


def login_required(f):
    def wrapper(*args, **kwargs):

        login, password = f()

        if login == 'admin' and password == 'password':
            print("poprawnie zalogowano!")
        elif login == 'anonymous' and password == 'anonymous':
            print("witaj, anonymous!")
        else:
            raise Exception("NotLoggedIn")

    return wrapper



@login_required
def authorization():
    adm_login = input("login: ")
    adm_password = input("haslo: ")
    return adm_login, adm_password


@login_required
def anonymous_login():
    a_login = 'anonymous'
    a_password = 'anonymous'

    return a_login, a_password


def main():
    usr_input = int(input("wybierz opcje logowania:\n1. administrator\n2. anonymous\n*wybierz inny, by wyjsc*\n"))

    if usr_input == 1:
        authorization()
    elif usr_input == 2:
        anonymous_login()
    else:
        return 0


if __name__ == '__main__':
    while main():
        pass

