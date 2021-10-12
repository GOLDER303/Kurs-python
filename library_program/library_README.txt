Program powinien składać się z 4/5 plików:
- Jeden plik główny (odpowiada za uruchomienie całego programu - main.py)
- Paczka (katalog - library_modules), który będzie posiadał 3 pliki - każdy z plików ma posiadać jedną klasę (Biblioteka, Książka, Czytelnik) + 1 plik z dostępnymi komendami (opcjonalnie/można też zamieścić to w main.py), aby można było importować poszczególne pliki/klasy z katalogu library_modules do pliku main.py, należy w katalogu library_modules utworzyć pusty plik __init__.py

Działanie programu:
Należy utworzyć program, który zasymuluje funkcjonowanie biblioteki. 
Biblioteka powinna posiadać adres oraz nazwę. 
Do biblioteki można dodawać książki oraz czytelników.
Każda książka posiada autora, tytuł oraz status wypożyczenia.
Każdy czytelnik posiada imię, nazwisko oraz listę wypożyczonych książek.
Każdemu czytelnikowi można wypożyczyć książkę (czytelnik może mieć wypożyczonych kilka książek), a czytelnik może taką książkę zwrócić do biblioteki.
W bibliotece mamy możliwość również usunięcia wybranej książki oraz wybranego czytelnika z bazy.
Dodatkowo w bibliotece można sprawdzić aktualny status wypożyczenia wybranej książki, a także wypisać listę książek i czytelników.
Program powinien działać w taki sposób by po uruchomieniu przyjmował wybrane komendy, które obsłużą poszczególne akcje w bibliotece.
