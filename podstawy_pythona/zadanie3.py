def czy_pierwsza(n):
    """Sprawdza czy liczba n jest pierwsza"""

    # BŁĄD 1: było "if n <= 2:" – 2 jest liczbą pierwszą, więc nie może być <= 2
    # Poprawka: liczby < 2 nie są pierwsze
    if n < 2:
        return False

    # BŁĄD 2: sprawdzanie dzielników do n jest błędne
    # Poprawka: sprawdzamy do pierwiastka z n
    from math import sqrt
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# Wczytanie zakresu od użytkownika
dolna = int(input("Podaj dolną granicę zakresu: "))
gorna = int(input("Podaj górną granicę zakresu: "))

print(f"Liczby pierwsze w zakresie {dolna}-{gorna}:")

liczby_pierwsze = []

# BŁĄD 3: było range(dolna, gorna) – zakres nie obejmował górnej granicy
# Poprawka: range(dolna, gorna + 1)
for liczba in range(dolna, gorna + 1):
    if czy_pierwsza(liczba):
        liczby_pierwsze.append(str(liczba))

if liczby_pierwsze:
    print(", ".join(liczby_pierwsze))
else:
    print("Brak liczb pierwszych w podanym zakresie.")