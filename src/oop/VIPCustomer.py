from .Customer import Customer
from .Person import Person

class VIPCustomer(Customer, Person):
    """
    VIPCustomer ist eine erweiterte Version der Customer-Klasse und implementiert
    zusätzlich die Funktionalität für VIP-Kunden.

    Attribute:
        _vip_level (int): Die VIP-Stufe des Kunden.

    Methoden:
        __init__(name: str, policy_type: str, annual_fee: float, vip_level: int):
            Initialisiert ein VIPCustomer-Objekt mit Namen, Versicherungstyp, Jahresgebühr
            und VIP-Level.
        get_details() -> str:
            Gibt eine formatierte Zeichenkette zurück, die die Details des VIP-Kunden enthält.
    """

    def __init__(self, name: str, policy_type: str, annual_fee: float, vip_level: int):
        """
        Initialisiert ein VIPCustomer-Objekt mit den folgenden Attributen:

        Parameter:
            name (str): Der Name des Kunden.
            policy_type (str): Der Typ der Versicherungspolice.
            annual_fee (float): Die jährliche Gebühr für die Versicherung.
            vip_level (int): Die VIP-Stufe des Kunden.
        """
        super().__init__(name, policy_type, annual_fee)
        self._vip_level = vip_level

    def get_details(self) -> str:
        """
        Gibt eine formatierte Zeichenkette zurück, die die Details des VIP-Kunden
        enthält, einschließlich Name, Policentyp, Jahresgebühr und VIP-Level.

        Rückgabewert:
            str: Eine Zeichenkette mit den Details des VIP-Kunden.
        """
        return f"VIP Customer: {self._name}, Policy Type: {self._policy_type}, Annual Fee: {self._Customer__annual_fee}, VIP Level: {self._vip_level}"
    
    def __str__(self) -> str:
        return self.get_details()
