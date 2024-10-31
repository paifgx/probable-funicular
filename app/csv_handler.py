import csv
from .customer import Customer

def import_customers(filename: str):
    customers = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            customers.append(Customer(row[0], row[1], float(row[2])))
    return customers

def export_customers(customers, filename: str):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "policy_type", "annual_fee"])
        for customer in customers:
            writer.writerow([customer.name, customer.policy_type, customer.annual_fee])
