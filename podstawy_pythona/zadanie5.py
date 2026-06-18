def rail_fence_encrypt(text, rails): # Usuwanie spacji
    text = text.replace(" ", "")
    
    fence = [""] * rails # Tworzenie listy pustych "szyn"

    current_rail = 0
    direction = 1  # Ustawienia szyn

    for char in text:
        fence[current_rail] += char

        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1

        current_rail += direction # Zmiana kierunku na końcach

    return "".join(fence) 

message = "PODSTAWY PYTHONA"
num_rails = 3

encrypted = rail_fence_encrypt(message, num_rails)

print("Oryginalna wiadomość:", message)
print("Liczba szyn:", num_rails)
print("Zaszyfrowana wiadomość:", encrypted)