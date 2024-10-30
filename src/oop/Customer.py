from abc import ABC, abstractmethod

class Customer(ABC):
    """
    Customer ist eine abstrakte Basisklasse, die grundlegende Funktionen und Eigenschaften
    für Kunden implementiert und als Vorlage für abgeleitete Kundenklassen dient.

    Attribute:
        customer_count (int): Eine Klassenvariable, die die Anzahl der erstellten Kunden speichert.
        _name (str): Der Name des Kunden (öffentlich zugänglich).
        _policy_type (str): Der Typ der Versicherungspolice des Kunden (geschützt).
        __annual_fee (float): Die jährliche Gebühr des Kunden (privat).

    Methoden:
        __init__(name: str, policy_type: str, annual_fee: float):
            Initialisiert die Attribute des Kunden und erhöht die Kundenanzahl.
        get_customer_count() -> int:
            Klassenmethode, die die Anzahl der Kunden zurückgibt.
        annual_fee() -> float:
            Property-Getter für die jährliche Gebühr des Kunden.
        annual_fee(fee: float) -> None:
            Property-Setter für die jährliche Gebühr des Kunden, der sicherstellt,
            dass der Wert positiv ist, ansonsten wird eine ValueError-Exception ausgelöst.
        is_valid_fee(fee: float) -> bool:
            Statische Methode, die überprüft, ob eine Gebühr gültig (nicht negativ) ist.
        get_details() -> str:
            Abstrakte Methode, die in abgeleiteten Klassen implementiert werden muss und
            die Details des Kunden als Zeichenkette zurückgibt.
        greet() -> str:
            Gibt eine Begrüßungsnachricht des Kunden zurück.
    """

    customer_count = 0

    def __init__(self, name: str, policy_type: str, annual_fee: float):
        """
        Initialisiert die Customer-Klasse mit den folgenden Attributen:

        Parameter:
            name (str): Der Name des Kunden.
            policy_type (str): Der Typ der Versicherungspolice.
            annual_fee (float): Die jährliche Gebühr für die Versicherung.
        
        Erhöht die Klassenvariable `customer_count` um 1.
        """
        self._name = name                   # öffentliches Attribut
        self._policy_type = policy_type     # geschütztes Attribut
        self.__annual_fee = annual_fee      # privates Attribut

        Customer.customer_count += 1

    @classmethod
    def get_customer_count(cls) -> int:
        """
        Gibt die Anzahl der erstellten Kunden zurück. Die Methode ist als Klassenmethode
        deklariert, was bedeutet, dass sie auf die Klasse selbst statt auf eine Instanz bezogen ist.
        Der Dekorator `@classmethod` ermöglicht den Zugriff auf Klassenattribute, wie z.B. `customer_count`.

        Rückgabewert:
            int: Anzahl der Kundeninstanzen.
        """
        return cls.customer_count

    @property
    def annual_fee(self) -> float:
        """
        Property-Getter für die jährliche Gebühr des Kunden. Der `@property`-Dekorator
        definiert eine Methode als Property, die aufgerufen werden kann, ohne explizit als Methode zu erscheinen.
        Dies ermöglicht den Zugriff auf `annual_fee` als wäre es ein Attribut, obwohl es eine Methode ist.

        Rückgabewert:
            float: Die jährliche Gebühr des Kunden.
        """
        return self.__annual_fee
    
    @annual_fee.setter
    def annual_fee(self, fee: float) -> None:
        """
        Property-Setter für die jährliche Gebühr des Kunden. Mit dem `@property`-Dekorator
        und der darauf folgenden Setter-Deklaration `@annual_fee.setter` kann auf `annual_fee`
        zugegriffen und es kann modifiziert werden, als wäre es ein Attribut, obwohl intern
        eine Methode aufgerufen wird. Hier wird die Gebühr nur aktualisiert, wenn der neue Wert positiv ist.
        
        Parameter:
            fee (float): Die neue jährliche Gebühr.
        
        Raises:
            ValueError: Wenn die Gebühr negativ ist.
        """
        if fee >= 0:
            self.__annual_fee = fee
        else:
            raise ValueError("Annual fee must be a positive number")
        
    @staticmethod
    def is_valid_fee(fee: float) -> bool:
        """
        Überprüft, ob eine Gebühr gültig ist (nicht negativ). Der `@staticmethod`-Dekorator
        weist darauf hin, dass diese Methode keinen Zugriff auf Instanz- oder Klassenattribute benötigt
        und keine Parameter wie `self` oder `cls` akzeptiert. Dies macht sie ideal für Utility-Funktionen,
        die auf die Klasse bezogen sind, aber keine Attribute ändern.

        Parameter:
            fee (float): Die zu prüfende Gebühr.

        Rückgabewert:
            bool: True, wenn die Gebühr positiv oder null ist, sonst False.
        """
        return fee >= 0
    
    @abstractmethod
    def get_details(self) -> str:
        """
        Abstrakte Methode, die von Unterklassen implementiert werden muss, um die
        Kundendetails als Zeichenkette zurückzugeben. Der Dekorator `@abstractmethod`
        markiert die Methode als abstrakt, was bedeutet, dass die `Customer`-Klasse
        selbst nicht instanziiert werden kann und die Methode in abgeleiteten Klassen
        überschrieben werden muss.

        Rückgabewert:
            str: Die Details des Kunden (muss in der abgeleiteten Klasse definiert werden).
        """
        pass
        
    def greet(self) -> str:
        """
        Gibt eine Begrüßungsnachricht des Kunden zurück.

        Rückgabewert:
            str: Begrüßungsnachricht.
        """
        return "Hello, I am a customer"
