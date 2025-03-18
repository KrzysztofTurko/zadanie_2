#Dodano testy jednostkowe

def is_valid_email(email):
    """
    Sprawdza, czy podany adres e-mail jest poprawny.
    """
    if not email or '@' not in email or '.' not in email:
        return False
    return True

def calculate_area(shape, *args):
    """
    Oblicza pole figury geometrycznej.
    Obsługiwane figury: 'rectangle' (prostokąt), 'circle' (koło), 'triangle' (trójkąt).
    """
    if shape == 'rectangle':
        if len(args) != 2:
            raise ValueError("Prostokąt wymaga dwóch argumentów: długość i szerokość.")
        return args[0] * args[1]
    elif shape == 'circle':
        if len(args) != 1:
            raise ValueError("Koło wymaga jednego argumentu: promień.")
        return 3.14 * (args[0] ** 2)
    elif shape == 'triangle':
        if len(args) != 2:
            raise ValueError("Trójkąt wymaga dwóch argumentów: podstawa i wysokość.")
        return 0.5 * args[0] * args[1]
    else:
        raise ValueError("Nieznana figura geometryczna.")

def filter_even_numbers(numbers):
    """
    Filtruje listę liczb, zwracając tylko parzyste.
    """
    if not isinstance(numbers, list):
        raise TypeError("Oczekiwano listy liczb.")
    return [num for num in numbers if num % 2 == 0]

def convert_date_format(date_str):
    """
    Konwertuje datę z formatu 'YYYY-MM-DD' na 'DD/MM/YYYY'.
    """
    try:
        year, month, day = date_str.split('-')
        return f"{day}/{month}/{year}"
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwano 'YYYY-MM-DD'.")

def is_palindrome(text):
    """
    Sprawdza, czy podany tekst jest palindromem.
    """
    if not isinstance(text, str):
        raise TypeError("Oczekiwano tekstu.")
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]
