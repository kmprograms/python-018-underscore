# ======================================================================================
# Znak _ przechowuje ostatnio wyliczoną przez interpreter wartość
# ======================================================================================
# >> 10 + 20
# >> _
# >> _ * 2
# >> _

# ======================================================================================
# Znak _ możesz zastosować do separacji cyfr w liczbie
# ======================================================================================
x1 = 1_000_000
x2 = 0b_1_10001_10001

# ======================================================================================
# Możesz zastosować znak _, żeby ignorować pewne elementy / wartości
# ======================================================================================
x, _, y = 1, 2, 3
print(x)
print(y)

# Ignorowanie wielu wartości
x, *_, y = 1, 2, 3, 4, 5
print(x)
print(y)

# Ignorowanie indeksu
for _ in range(4):
    print('ACTION')

# Jeszcze inny przykład ignorowania wartości
people = [
    ('A', 10, 1000),
    ('B', 20, 2000),
    ('C', 30, 3000)
]
for _, a, b in people:
    print(a, b)
[print(a, b) for _, a, b in people]

for *_, b in people:
    print(b)
[print(b) for *_, b in people]

# ======================================================================================
# _ mozesz stosowac w nazwach przykładowo funkcji oraz zmiennych
# ======================================================================================

# Kiedy używasz nazwę zaczynającą się od _, wtedy taki element o takiej nazwie
# będzie traktowany jako prywatny w module i będzie ignorowany podczas używania
# instrukcji:
# from <nazwa modulu> import *

from my_package.variables import *
print(a)
# print(_b)

# from my_package.variables import _b

# PAMIETAJ!
# Python nie wspiera ukrywania składników za pomocą private, tak jak robią to
# inne języki programowania. Dlatego mówimy tutaj bardziej o konwencji niż o prawdziwym
# ukrywaniu składników.

class Person:
    def __init__(self, name):
        self._name = name

    def _format(self):
        return self._name[:3].capitalize()

    def info(self):
        return self._format()

p = Person('Andrzej')
print(p.info())


# ======================================================================================
# Używamy _ na końcu nazwy w celu uniknięcia konfliktu z nazwami słów kluczowych oraz
# bytów wbudowanych
# ======================================================================================
# xx, yy = 10, 20
# sum = xx + yy
# sum_ = xx + yy


# ======================================================================================
# Dodawanie na początku nazwy __ (double underscore)
# ======================================================================================
# Dodanie __ na początku nazwy spowoduje, że interpreter do takiej nazwy podczas
# budowania kodu doda prefix _ClassName.
# Jezeli masz metode __met to finalnie jej nazwa będzie miec postać _ClassName__met
# To podejście jest stosowane, żeby uniknąć konfliku nazw atrybutów pomiędzy różnymi
# klasami.

# Poza tym do takich atrybutow nie mozesz potem odnosic się za pomoca wywołania
# ClassName.__met co traktowane jest jako jeszcze wyższa forma enkapsulacji niż _

class A:
    @staticmethod
    def _met():
        pass

    @staticmethod
    def __met2():
        pass


a = A()
print(A._met())
print(A.__met2()) # BLAD


# ======================================================================================
# Dodawanie na początku i na końcu nazwy __ (double underscore)
# ======================================================================================
# Jest to konwencja stosowana wobec specjalnych zmiennych oraz metod takich jak
# __init__ czy __len__.
# Takie funkcje mają najczęściej specjalne przeznaczenie.
# Użytkownik może na własne potrzeby niekiedy zmieniać zachowanie takich specjalnych
# bytów, co wykorzystujemy np podczas pracy z klasami.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price