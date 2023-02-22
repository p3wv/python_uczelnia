"""Schröder PawełZTPwJP informatyka N II rok L_II_NW_INFI_K7b 
L6 
""" 
# z1

def czyliczba():
    usr_input = input("podaj napis: ")

    napis = []

    for i in usr_input:
        if i.isdigit():
            napis.append(i)

    if len(napis) == len(usr_input):
        print("to jest liczba")
    else:
        print("to nie jest liczba")


# z2

def czyliczba1():
    napis1 = []

    usr_input1 = input("podaj napis: ")

    for i in usr_input1:
        if i.isdigit():
            napis1.append(i)

    wypisz = ", ".join(napis1)

    print("znalezione liczby: ", wypisz)


# z4
def kody_pocztowe():
    user_input = input("Podaj kod: ")

    listed_input = []

    for i in user_input:
        listed_input.append(i)

    if listed_input[0].isdigit() and listed_input[1].isdigit() and listed_input[2] == '-' and listed_input[
        3].isdigit() and listed_input[4].isdigit() and listed_input[5].isdigit():
        print("Kod jest poprawny!")
    else:
        print("#Kod jest niepoprawny#")


# z5

def email():
    adres = input("Podaj adres: ")

    listed_adres = []
    local = []
    domain = []

    for i in adres:
        listed_adres.append(i)

    print(listed_adres)

    for en in listed_adres:
        if en != "@":
            local.append(en)
        else:
            break

    if len(local) > 64:
        raise Exception("too many characters before @!")

    def first_part():
        for m in local:
            if m.isalnum() or m == ["!", "#", "$", "%", "&", "‘", "*", "+", "–", "/", "=", "?", "^", "_", "`", ".", "{",
                                    "|", "}", "~"]:
                if local[0] == "." or local[-1] == ".":
                    print("must not contain a dot at the beginning or end!")
                    return False
                else:
                    return True

    for e in listed_adres:
        if e == "@":
            f = listed_adres.index(e) + 1
            for n in listed_adres[f:]:
                domain.append(n)

    if len(domain) > 255:
        raise Exception("too many characters after @!")

    def second_part():
        for elem in domain:
            if elem.isalnum() or elem == "-":
                if domain[0] == "-" or domain[-1] == "-":
                    print("must not contain hyphen at the beginning or end!")
                    return False
                else:
                    return True

    first_part()
    second_part()

    if first_part() is True:
        if second_part() is True:
            print("Adres jest poprawny.")
        else:
            print("Adres jest niepoprawny.")
    else:
        print("Adres jest niepoprawny.")


