class Uczen:
    def __init__(self, imie, nazwisko, numer_klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_klasy = numer_klasy
        self.lekcje = []

class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy

class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

def utworz_ucznia():
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    numer_klasy = input("Podaj numer klasy ucznia: ")
    uczen = Uczen(imie, nazwisko, numer_klasy)
    uczniowie.append(uczen)
    print("Uczeń został dodany!")

def utworz_nauczyciela():
    imie = input("Podaj imię nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    przedmiot = input("Podaj przedmiot nauczyciela: ")
    klasy = input("Podaj klasy nauczyciela (oddzielone przecinkami): ").split(',')
    nauczyciel = Nauczyciel(imie, nazwisko, przedmiot, klasy)
    nauczyciele.append(nauczyciel)
    print("Nauczyciel został dodany!")

def utworz_wychowawce():
    imie = input("Podaj imię wychowawcy: ")
    nazwisko = input("Podaj nazwisko wychowawcy: ")
    klasa = input("Podaj klasę wychowawcy: ")
    wychowawca = Wychowawca(imie, nazwisko, klasa)
    wychowawcy.append(wychowawca)
    print("Wychowawca został dodany!")

def zarzadzaj_uzytkownikami():
    print("Proces zarządzania użytkownikami:")
    print("1. Klasa")
    print("2. Uczeń")
    print("3. Nauczyciel")
    print("4. Wychowawca")
    print("5. Powrót do menu głównego" )
    wybor = input("Wybierz opcję (1/2/3/4/5): ")

    if wybor == '1':
        klasa = input("Podaj numer klasy do wyświetlenia: ")
        for uczen in uczniowie:
            if uczen.numer_klasy == klasa:
                print(f"Uczeń: {uczen.imie} {uczen.nazwisko} ({uczen.numer_klasy})")
        for wychowawca in wychowawcy:
            if wychowawca.klasa == klasa:
                print(f"Wychowawca: {wychowawca.imie} {wychowawca.nazwisko}")
    elif wybor == '2':
        imie = input("Podaj imię ucznia: ")
        nazwisko = input("Podaj nazwisko ucznia: ")
        for uczen in uczniowie:
            if uczen.imie == imie and uczen.nazwisko == nazwisko:
                print(f"Uczeń {imie} {nazwisko}: , {uczen.numer_klasy}{', '.join(uczen.lekcje)}")
                for nauczyciel in nauczyciele:
                    for lekcja in uczen.lekcje:
                        if lekcja == nauczyciel.przedmiot:
                            print(f"Nauczyciel: {nauczyciel.imie} {nauczyciel.nazwisko}")
    elif wybor == '3':
        imie = input("Podaj imię nauczyciela: ")
        nazwisko = input("Podaj nazwisko nauczyciela: ")
        for nauczyciel in nauczyciele:
            if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
                print(f"Klasy prowadzone przez nauczyciela {imie} {nazwisko}: {', '.join(nauczyciel.klasy)}")


    elif wybor == '4':
        imie = input("Podaj imię wychowawcy: ")
        nazwisko = input("Podaj nazwisko wychowawcy: ")
        for wychowawca in wychowawcy:
            if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
                uczniowie_w_klasie = [uczen for uczen in uczniowie if uczen.numer_klasy == wychowawca.klasa]
                uczniowie_w_klasie_str = ', '.join([uczen.imie + ' ' + uczen.nazwisko for uczen in uczniowie_w_klasie])
                print(f"Uczniowie prowadzeni przez wychowawcę {imie} {nazwisko} w klasie {wychowawca.klasa}: {uczniowie_w_klasie_str}")
    elif wybor == '5':
        return
    else:
        print("Niepoprawny wybór!")

uczniowie = []
nauczyciele = []
wychowawcy = []

while True:
    print("\nMenu:")
    print("1. Utwórz użytkownika")
    print("2. Zarządzaj użytkownikami")
    print("3. Koniec")
    opcja = input("Wybierz opcję (1/2/3): ")

    if opcja == '1':
        print("\nWybierz typ użytkownika do utworzenia:")
        print("1. Uczeń")
        print("2. Nauczyciel")
        print("3. Wychowawca")
        typ_uzytkownika = input("Wybierz opcję (1/2/3): ")
        if typ_uzytkownika == '1':
            utworz_ucznia()
        elif typ_uzytkownika == '2':
            utworz_nauczyciela()
        elif typ_uzytkownika == '3':
            utworz_wychowawce()
        else:
            print("Niepoprawny wybór!")
    elif opcja == '2':
        zarzadzaj_uzytkownikami()
    elif opcja == '3':
        print("Dziękujemy za korzystanie z programu. Do widzenia!")
        break
    else:
        print("Niepoprawny wybór!")
