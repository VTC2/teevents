
## Moduł obsługi bazy danych
#
#  Funkcje przydatne do obsługi bazy danych Tevent
import sqlite3
from event import Event


class TeventDB():
    
    ## Konstruktor
    def __init__(self, dbname):
        self.dbname = dbname

    ## Metoda Connect
    #  
    #  Inicjuje połączenie z bazą danych\
    #  @return - zwraca uchwyt połączenia
    def Connect(self):
        #TODO: obsłuzyć wyjątek błędnego połączenia z bazą
        self.conn = sqlite3.connect(self.dbname)    
        pass
    
    ## Metoda Connect
    #  
    #  Inicjuje połączenie z bazą danych\
    #  @return - zwraca uchwyt połączenia    
    def Cursor(self):
        #TODO: zwraca kursor połączenia z bazą
    
    ## Metoda Close
    #
    #  Zamykanie połaczenia z bazą
    def Close(self):
        #TODO: zamknięcie bieżącego połączenia z bazą
        pass
    
    # 1. aktualizacja/dodanie/usunięcie wierszy tabeli links - wywołanie metody UpdateLinks z modułu teventdb
    def UpdateLinks(self, eventID, links:list):
        #TODO:
        # 1) pobrać listę linków dla danego eventID z bazy
        # 2) sprawdzamy, czy w bazie istnieją linki, które nie mają odpowiedników w przekazanej tablicy. Jeśli tak, usuwamy je
        # 3) dla każdego przekazanego linku sprawdzić, czy w bazie istnieje jego odpowiednik. Jeśli nie, dodajemy do bazy
        # 3) 

    # 2. aktualizacja/dodanie/usunięcie wierszy tabeli images - wywołanie metody UpdateImages z modułu teventdb
    def UpdateImages(self, eventID, images: list):
        #TODO: podobnie jak przy linkach

    # 3. aktualizacja tagów - Wywołanie metody UpdateTags() z modułu teventdb
    def UpdateTags(self, eventID, tags: list):
        #TODO: 
        # - sprawdzić, czy w tabeli tags istnieją tagi przekazane do funkcji, jeśli nie, dodać je do tabeli Tags
        # - sprawdzić, czy w tabeli eventTag istnieją powiązania tagID z eventID, jeśli nie - dodać powiązania

    # 4. aktualizacja ról -  Wywołanie metody UpdateUserRoles() z modułu teventdb
    def UpdateRoles(self, eventID, userRoles: list):
        #TODO: 
        # - sprawdzić, czy w tabeli EventsRoles istnieją powiązania, które nie występują w userRoles, jeśli tak - usunąć je
        # - sprawdzić, czy w userRoles istnieją powiązania, które nie występują w tabeli EventsRoles, jeśli tak - dodać je
    
    # Dodanie eventu do bazy
    def AddEvent(self, event: Event):
        # TODO: ustawić wszystkie parametry eventu

        #

    


