# Klondike Solitaire (Pasjans)

Tekstowa implementacja klasycznej gry karcianej Pasjans Klondike w języku Python.



## Opis projektu

Ten projekt to implementacja klasycznej gry karcianej Pasjans Klondike w interfejsie tekstowym. Gra została napisana w języku Python i oferuje pełną funkcjonalność standardowego pasjansa, włącznie z rozgrywką za pomocą poleceń tekstowych.

## Wymagania

- Python 3.6 lub nowszy
- Nie są wymagane dodatkowe biblioteki (wszystkie wykorzystane moduły są częścią standardowej biblioteki Python)

## Sposób uruchomienia projektu

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/IgnacyO1/Python.git
   ```
2. Przejdź do katalogu projektu:
   ```
   cd Python
   ```
3. Uruchom grę za pomocą polecenia:
   ```
   python main.py
   ```

## Instrukcja rozgrywki

### Układ początkowy gry
- Siedem kolumn z kartami, gdzie w każdej kolumnie odkryta jest tylko ostatnia karta:
  - Pierwsza kolumna: 1 karta
  - Druga kolumna: 1 karta zakryta, 1 odkryta
  - Trzecia kolumna: 2 karty zakryte, 1 odkryta
  - ...itd.
- Stos kart do dobierania (reszta talii)
- Cztery puste stosy finalne, po jednym dla każdego koloru (kiery, kara, piki, trefle)

### Cel gry
Celem gry jest przeniesienie wszystkich kart na stosy finalne (po jednym dla każdego koloru), układając je od asa do króla.

### Dostępne polecenia

Podczas rozgrywki możesz używać następujących poleceń:

| Polecenie | Opis |
|-----------|------|
| `move c1 c2` | Przenieś wierzchnią kartę z kolumny 1 do kolumny 2 |
| `c1 final` | Przenieś wierzchnią kartę z kolumny 1 na odpowiedni stos finalny |
| `draw c1` | Przenieś aktualną kartę ze stosu dobierania do kolumny 1 |
| `draw final` | Przenieś aktualną kartę ze stosu dobierania na odpowiedni stos finalny |
| `move c1 c2 3` | Przenieś 3 karty z kolumny 1 do kolumny 2 |
| `next` | Dobierz następną kartę ze stosu dobierania |
| `reshuffle` | Przetasuj odrzucone karty i dodaj je z powrotem do stosu dobierania |
| `quit` | Wyjdź z gry |
| `help` | Wyświetl pomoc |
| `restart` | Rozpocznij nową grę |

### Zasady przenoszenia kart:
- Na pustą kolumnę można położyć tylko króla (K)
- Na kartę można położyć tylko kartę o przeciwnym kolorze (czarna na czerwoną lub czerwona na czarną) i wartości o jeden mniejszej
- Karty można układać w sekwencji malejącej (K, Q, J, 10, 9, ..., 2, A)
- Na stos finalny można kłaść karty tego samego koloru w kolejności od asa (A) do króla (K)
- Po przeniesieniu odkrytej karty z kolumny, zakryta karta pod nią zostaje automatycznie odkryta

### Warunki zakończenia gry:
- **Wygrana**: Wszystkie karty zostały przeniesione na stosy finalne
- **Przerwanie gry**: W dowolnym momencie można zakończyć grę poleceniem `quit` lub rozpocząć od nowa poleceniem `restart`

## Struktura projektu i opis modułów

### [`Card.py`]
- Klasa `Card` - reprezentuje pojedynczą kartę w grze
  - Atrybuty: wartość, kolor, figura, widoczność
  - Metody: `flip()` - odwraca kartę, `__str__()` - zwraca tekstową reprezentację karty

### [`column.py`]
- Klasa `Column` - reprezentuje kolumnę kart na stole
  - Metody: `add_card()`, `remove_top_card()`, `get_top_card()`, `is_empty()`
- Klasa `Final_Column` - reprezentuje stos finalny dla danego koloru
  - Dodatkowa logika dla sprawdzania poprawności dodawania kart
- Klasa `Draw_Column` - reprezentuje stos dobierania kart
  - Metody: `next_card()`, `remove_card()`, `reshuffle()`

### [`deck.py`]
- Klasa `Deck` - reprezentuje talię kart
  - Metody: `shuffle()` - tasuje karty, `deal()` - rozdaje karty

### [`engine.py`]
- Zawiera logikę gry i funkcje sprawdzające poprawność ruchów:
  - `column_to_column()` - przenosi kartę między kolumnami
  - `column_to_final()` - przenosi kartę z kolumny na stos finalny
  - `draw_to_column()` - przenosi kartę ze stosu dobierania do kolumny
  - `draw_to_final()` - przenosi kartę ze stosu dobierania na stos finalny
  - `sequence_column_to_column()` - przenosi sekwencję kart między kolumnami

### [`enviroment.py`] / [`color_enviroment.py`]
- Funkcje inicjalizacji gry i wyświetlania stanu gry
  - `initialize_game()` - przygotowuje stan początkowy gry
  - `display_game()` - wyświetla aktualny stan rozgrywki

### [`ui_moves.py`]
- Interfejs użytkownika i przetwarzanie poleceń
  - `ask_for_move()` - pobiera polecenie od użytkownika
  - `proces_move()` - przetwarza polecenie i określa jego typ
  - `execute_move()` - wykonuje ruch o ile jest poprawny
  - `display_help()` - wyświetla pomoc
  - `check_victory()` - sprawdza warunek zwycięstwa
  - `victory_message()` - wyświetla komunikat zwycięstwa

### [`main.py`]
- Główny moduł gry, inicjalizuje rozgrywkę i obsługuje główną pętlę gry

## Architektura projektu

Projekt został zorganizowany zgodnie z zasadami dobrego programowania (SOLID, DRY):
- Modularny design z jasno określonymi odpowiedzialnościami klas
- Separacja logiki gry od interfejsu użytkownika
- Czytelne i opisowe nazwy funkcji i zmiennych
- Użycie klas do reprezentacji obiektów gry (karty, kolumny, talia)

## Przykład rozgrywki

1. Uruchom grę: `python main.py`
2. Wyświetl dostępne ruchy: wpisz `help`
3. Dobierz kartę ze stosu: wpisz `next`
4. Przenieś kartę z kolumny 1 do kolumny 2: wpisz `move c1 c2`
5. Przenieś kartę ze stosu dobierania do kolumny 3: wpisz `draw c3`
6. Przenieś asa na stos finalny: wpisz `c4 final` (jeśli as jest na wierzchu kolumny 4)

## Autor

IgnacyO1 - [GitHub](https://github.com/IgnacyO1)

Powodzenia w rozgrywce!