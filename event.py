## @package Event
#  Klasa Event
#
#  Moduł reprezentuje klasę Event, której zadaniem jest przechowanie wszystkich informacji na temat pojedynczego eventu
#  oraz wymiana ich z bazą danych

class Event():
    
    ##  Konstruktor domyślny 
    #  
    # Inicjuje wartości domyślne zmiennych członkowskich 
    def __init__(self):
        #TODO: 
        # - ustawić wartości domyślne zmiennych członkowskich        
        pass
    
    ##  Konstruktor przeciążony 
    #  
    #  Pobiera Event z bazy danych na podstawie jego ID i wypełnia wszystkie pola
    # @param eventID int - identyfikator eventu
    def __init__(self, eventID):
        #TODO: 
        # - pobrać informacje o evencie z tabeli Events oraz EventContent z bazy danych 
        # - pobrać linki przypisane do tego eventu i wypełnić słownik self.links 
        # - pobrać obrazki przypisane do tego eventu i wypełnić strukturę self.images
        # - pobrać listę tagów i wypełnić listę self.tags
        # - uzupełnić wszystkie pola tej klasy
        # - 
        pass

    ## Konstruktor przeciążony 
    # 
    #  Ustawia wartości wszystkich zmiennych jako parametry wywołania oraz dodaje event do bazy danych
    def __init__(self, name, registrationDate, startDate, endDate, rating, priority, visibility, state, likeAmount, links:list, images:list, tags:list, userRoles:list, title, description):
        self.name = name
        self.registrationDate = registrationDate
        self.startDate = startDate
        self.endDate = endDate
        self.rating = rating
        #TODO: 
        # - dokończyć
        # - dodanie eventu do bazy danych
        
        pass
    
    ## Metoda AddUserRole
    #
    #  @param userID - id użytkownika przypisanego do roli
    #  @roleID - id roli 
    def AddUserRole(self, userID, roleID):
        #TODO: 
        # 1. dodać userID oraz roleID do tablicy self.userRoles 
        #
        pass

    ## Metoda RemoveUserRole
    #
    #  @param userID int - id użytkownika przypisanego do roli
    #  @param roleID int - id roli 
    def RemoveUserRole(self, userID):
        #TODO: 
        # 1. dodać userID oraz roleID do tablicy 
        #
        pass

    ## Metoda Publish
    #  
    #  Sprawdza aktualny stan artykułu oraz poziom użytkownika wywołującego i zmienia stan eventu
    def Publish(self, userID):
        #TODO: 
        # 1. sprawdź stan artykułu 
        # 2. sprawdź poziom użytkownika (czy moderator)
        # 3. jeśli tak - zmień poziom na wyższy
        pass
    ## Metoda UnPublish
    #  
    #  Sprawdza aktualny stan artykułu oraz poziom użytkownika wywołującego i zmienia stan eventu
    def Unpublish(self, userID):
        #TODO: 
        # 1. sprawdź stan artykułu 
        # 2. sprawdź poziom użytkownika (czy moderator)
        # 3. jeśli tak - zmień poziom na niższy
        pass
    
    ## Metoda ModifyEvent
    #
    # metoda modyfikuje parametry eventu
    def ModifyEvent(self, name, registrationDate, startDate, endDate, rating, priority, visibility, state, likeAmount, links:list, images:list, tags:list, userRoles:list, title, description):
        #TODO:
        # - ustwia podane parametry eventu 
        pass

    
    ## Metoda UpdateDB
    #
    #  metoda aktualizuje rekord bazy danych odpowiadający temu eventowi
    def UpdateDB():
        #TODO:
        # 1. aktualizacja/dodanie/usunięcie wierszy tabeli links - wywołanie metody UpdateLinks z modułu teventdb
        # 2. aktualizacja/dodanie/usunięcie wierszy tabeli images - wywołanie metody UpdateImages z modułu teventdb
        # 3. aktualizacja tagów - Wywołanie metody UpdateTags() z modułu teventdb
        # 4. aktualizacja ról -  Wywołanie metody UpdateUserRoles() z modułu teventdb
        # 5. aktualizacja pozostałych parametrów eventu w bazie danych - metoda UpdateEvent modułu teventdb
        pass

    ## Metoda AddEvent
    #  
    #  Dodaje bieżący event do bazy danych
    #  @return int - kod błędu
    def AddEvent():
        # TODO: 
        # 1. dodanie nowego rekordu do tabeli Events - funkcja AddEvent modułu teventdb
        # 2. pobranie ID dodanego eventu
        # 3. aktualizacja powiązanych tabel
        # 
        pass





