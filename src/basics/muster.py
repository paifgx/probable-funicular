# Aufgabe 1

## Kundendaten
customers: list[dict[str, str | int | float]] = [
    {'customer_id': 101, 'name': 'Max Mustermann', 'policy_type': 'Private', 'annual_fee': 250.0},
    {'customer_id': 102, 'name': 'Erika Beispiel', 'policy_type': 'Business', 'annual_fee': 400.0},
    {'customer_id': 103, 'name': 'Hans Müller', 'policy_type': 'Travel', 'annual_fee': 600.0}
]

## Policen-Kategorien
policy_types: set[str] = {'Private', 'Business', 'Family', 'Travel'}

## Sonderfälle
special_cases = (
    {'customer_id': 999, 'name': 'Special Customer', 'policy_type': 'Special', 'annual_fee': 1000.0},
)

# Aufgabe 2
## Filterung nach Kategorie:
def filter_policies(customers: list[dict], category: str) -> list[dict]:
    """Filtert Kunden nach einer bestimmten Policenkategorie."""
    return [customer for customer in customers if customer['policy_type'] == category]

## Durchschnittlicher Jahresbeitrag pro Kategorie:
def average_fee(customers: list[dict], category: str) -> float:
    """Berechnet den durchschnittlichen Jahresbeitrag für eine Kategorie."""
    filtered_customers = filter_policies(customers, category)
    if not filtered_customers:
        return 0.0
    total_fee = sum(customer['annual_fee'] for customer in filtered_customers)
    return total_fee / len(filtered_customers)

## Kategoriezählung:
def count_by_category(customers: list[dict]) -> dict[str, int]:
    """Zählt die Anzahl der Kunden pro Kategorie."""
    count = {}
    for customer in customers:
        category = customer['policy_type']
        count[category] = count.get(category, 0) + 1
    return count


# Aufgabe 3
## Datenaktualisierung (Mutation):
def update_fee(customers: list[dict], customer_id: int, new_fee: float) -> None:
    """Aktualisiert den Jahresbeitrag eines Kunden basierend auf der customer_id."""
    for customer in customers:
        if customer['customer_id'] == customer_id and customer not in special_cases:
            customer['annual_fee'] = new_fee
            return
    print(f"Kunde mit ID {customer_id} nicht gefunden oder ist ein Sonderfall.")

## Top-Kundenanalyse:
def top_customers(customers: list[dict], n: int) -> list[str]:
    """Findet die n Kunden mit den höchsten Jahresbeiträgen."""
    sorted_customers = sorted(customers, key=lambda customer: customer['annual_fee'], reverse=True)
    return [customer['name'] for customer in sorted_customers[:n]]

## Filtern mit List Comprehension:
high_fee_customers = [customer['customer_id'] for customer in customers if customer['annual_fee'] > 500]
# print(high_fee_customers)

# Aufgabe 4
## Report-Funktion:
def generate_report(customers: list[dict]) -> None:
    """Erstellt einen strukturierten Report über die Kunden."""
    print("Customer Report:")
    total_customers = len(customers)
    total_fee = sum(customer['annual_fee'] for customer in customers)
    
    for customer in customers:
        special_case = " (Special Case)" if customer in special_cases else ""
        print(f"Customer {customer['customer_id']}: {customer['name']}, Policy: {customer['policy_type']}, Annual Fee: {customer['annual_fee']:.2f}€{special_case}")
    
    print(f"\nTotal Customers: {total_customers}")
    print("Total Annual Fees: {:.2f}€".format(total_fee))

generate_report(customers)
