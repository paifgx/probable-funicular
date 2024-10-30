import pytest
from abc import ABC
from .VIPCustomer import VIPCustomer
from .Customer import Customer
from .Person import Person

def test_vip_customer_init():
    """
    Testet die Initialisierung eines VIPCustomer-Objekts.
    Überprüft, ob die Attribute _name, _policy_type, annual_fee und _vip_level
    korrekt gesetzt sind.
    """
    vip_customer = VIPCustomer("Alice", "Health", 1000.0, 3)

    assert vip_customer._name == "Alice"
    assert vip_customer._policy_type == "Health"
    assert vip_customer.annual_fee == 1000.0
    assert vip_customer._vip_level == 3

def test_get_details():
    """
    Testet die `get_details`-Methode von VIPCustomer.
    Überprüft, ob die zurückgegebene Zeichenkette den erwarteten Kundeninformationen entspricht.
    """
    vip_customer = VIPCustomer("Alice", "Health", 1000.0, 3)
    
    details = vip_customer.get_details()
    expected_details = "VIP Customer: Alice, Policy Type: Health, Annual Fee: 1000.0, VIP Level: 3"
    
    assert details == expected_details

def test_annual_fee_setter():
    """
    Testet den Setter für das Attribut `annual_fee` bei VIPCustomer.
    Setzt die Jahresgebühr auf einen neuen Wert und überprüft die Aktualisierung.
    """
    vip_customer = VIPCustomer("Alice", "Health", 1000.0, 3)
    vip_customer.annual_fee = 2000.0

    assert vip_customer.annual_fee == 2000.0

def test_invalid_annual_fee():
    """
    Überprüft, ob das Setzen einer ungültigen `annual_fee` bei VIPCustomer
    eine ValueError-Exception auslöst.
    """
    vip_customer = VIPCustomer("Alice", "Health", 1000.0, 3)
    
    with pytest.raises(ValueError):
        vip_customer.annual_fee = -500.0

def test_static_method():
    """
    Testet die statische Methode `is_valid_fee`, die prüft, ob eine Gebühr gültig ist.
    Überprüft, ob positive Werte als gültig und negative Werte als ungültig bewertet werden.
    """
    assert VIPCustomer.is_valid_fee(1000.0) is True
    assert VIPCustomer.is_valid_fee(-1000.0) is False

def test_mro():
    """
    Testet die Method Resolution Order (MRO) der VIPCustomer-Klasse.
    Überprüft, ob die MRO die erwartete Reihenfolge hat: VIPCustomer, Customer, ABC, Person, object.
    """
    expected_mro = (VIPCustomer, Customer, ABC, Person, object)
    assert VIPCustomer.__mro__ == expected_mro
