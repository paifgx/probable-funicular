import unittest
from .Customer import Customer

class ConcreteCustomer(Customer):
    """
    ConcreteCustomer ist eine konkrete Implementierung der abstrakten Basisklasse Customer.
    Sie überschreibt die abstrakte Methode `get_details`, um eine Zeichenkette mit den
    Kundeninformationen zu liefern.

    Methoden:
        get_details() -> str: Gibt eine formatierte Zeichenkette mit den Details des Kunden zurück,
        einschließlich Name, Versicherungsart und Jahresgebühr.
    """
    
    def get_details(self) -> str:
        return f"Name: {self._name}, Policy: {self._policy_type}, Fee: {self.annual_fee}"

class CustomerTests(unittest.TestCase):
    """
    CustomerTests enthält eine Sammlung von Unit-Tests für die Klasse Customer und
    die konkrete Implementierung ConcreteCustomer. Die Tests überprüfen die korrekte
    Funktionalität der Initialisierung, Getter und Setter, Methoden sowie abstrakte
    Basisklassen-Bedingungen.
    
    Methoden:
        setUp(): Initialisiert eine ConcreteCustomer-Instanz für die Verwendung in den Tests.
        test_initialization(): Überprüft die korrekte Initialisierung der Attribute.
        test_customer_count(): Prüft, ob der Kunden-Count nach Hinzufügen eines neuen
            Kunden korrekt erhöht wird.
        test_annual_fee_getter(): Überprüft den Getter für die `annual_fee`.
        test_annual_fee_setter_valid(): Testet den Setter für `annual_fee` mit einem gültigen Wert.
        test_annual_fee_setter_invalid(): Testet den Setter für `annual_fee` mit einem
            ungültigen Wert und erwartet eine ValueError-Exception.
        test_is_valid_fee(): Testet die is_valid_fee-Methode, um sicherzustellen,
            dass positive Gebühren als gültig und negative als ungültig bewertet werden.
        test_greet(): Überprüft die Begrüßungsmethode `greet`.
        test_get_details(): Testet die `get_details`-Methode und vergleicht die Rückgabe
            mit dem erwarteten Zeichenkettenformat.
        test_abstract_class_instantiation(): Prüft, ob eine Instanz der abstrakten
            Basisklasse Customer eine TypeError-Exception auslöst.
    """

    def setUp(self):
        """Initialisiert eine ConcreteCustomer-Instanz zur Nutzung in den Tests."""
        self.customer = ConcreteCustomer("Max Mustermann", "Krankenversicherung", 1000.0)

    def test_initialization(self):
        """Testet, ob die Attribute bei der Initialisierung korrekt gesetzt wurden."""
        self.assertEqual(self.customer._name, "Max Mustermann")
        self.assertEqual(self.customer._policy_type, "Krankenversicherung")
        self.assertEqual(self.customer.annual_fee, 1000.0)

    def test_customer_count(self):
        """
        Testet, ob der Kunden-Count nach Hinzufügen eines neuen Kunden korrekt erhöht wird.
        Erstellt eine zweite ConcreteCustomer-Instanz und vergleicht den Kunden-Count.
        """
        initial_count = Customer.get_customer_count()
        ConcreteCustomer("Erika Musterfrau", "Lebensversicherung", 1500.0)
        self.assertEqual(Customer.get_customer_count(), initial_count + 1)

    def test_annual_fee_getter(self):
        """Überprüft, ob der Getter für die `annual_fee` den korrekten Wert zurückgibt."""
        self.assertEqual(self.customer.annual_fee, 1000.0)

    def test_annual_fee_setter_valid(self):
        """
        Überprüft, ob der Setter für `annual_fee` einen gültigen Wert korrekt setzt.
        Der Test setzt die Gebühr auf 1200.0 und prüft den neuen Wert.
        """
        self.customer.annual_fee = 1200.0
        self.assertEqual(self.customer.annual_fee, 1200.0)

    def test_annual_fee_setter_invalid(self):
        """
        Überprüft, ob der Setter für `annual_fee` bei einem ungültigen Wert (z. B. -500.0)
        eine ValueError-Exception auslöst.
        """
        with self.assertRaises(ValueError):
            self.customer.annual_fee = -500.0

    def test_is_valid_fee(self):
        """
        Testet die statische Methode `is_valid_fee`, um sicherzustellen,
        dass positive Werte als gültig und negative als ungültig eingestuft werden.
        """
        self.assertTrue(Customer.is_valid_fee(100.0))
        self.assertFalse(Customer.is_valid_fee(-50.0))

    def test_greet(self):
        """Testet die Begrüßungsmethode `greet`, die eine Willkommensnachricht zurückgibt."""
        self.assertEqual(self.customer.greet(), "Hello, I am a customer")

    def test_get_details(self):
        """
        Überprüft, ob die Methode `get_details` eine formatierte Zeichenkette mit den
        Kundeninformationen zurückgibt, die den erwarteten Werten entspricht.
        """
        expected = "Name: Max Mustermann, Policy: Krankenversicherung, Fee: 1000.0"
        self.assertEqual(self.customer.get_details(), expected)

    def test_abstract_class_instantiation(self):
        """
        Testet, ob die abstrakte Basisklasse `Customer` nicht instanziiert werden kann.
        Erwartet, dass eine TypeError-Exception ausgelöst wird, wenn versucht wird,
        eine `Customer`-Instanz direkt zu erstellen.
        """
        with self.assertRaises(TypeError):
            Customer("Test", "Test", 100.0)

if __name__ == '__main__':
    unittest.main()
