# from app.customer import Customer, VIPCustomer
# from app.customer_policy_management import CustomerPolicyManagement
# from app.csv_handler import import_customers, export_customers
# from app.report import generate_customer_report
# from app.bonus_analysis import perform_statistical_analysis

# # Create example customers and policies
# customers = [
#     Customer("John Doe", "Private", 400),
#     VIPCustomer("Jane Smith", "Private", 500),
#     Customer("ACME Corp.", "Commercial", 1000)
# ]

# # Example usage of CustomerPolicyManagement
# policy_manager = CustomerPolicyManagement()

# # Example of importing/exporting customers
# import_customers("customers.csv")
# export_customers(customers, "exported_customers.csv")

# # Generate customer report
# generate_customer_report(customers)

# # Perform statistical analysis for the bonus tasks
# perform_statistical_analysis(customers)

from app.customer import Customer

customer = Customer("John Doe", "Private", 400)
customer_question = input("Wie lautet deine Frage? ")
response = customer.get_help(customer_question)

print(f"Frage: {customer_question}")
print(f"Antwort: {response}")