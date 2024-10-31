def generate_customer_report(customers):
    report = [f"{customer.name}: Total Premium = {customer.calculate_discounted_fee():.2f}" for customer in customers]
    print("\n".join(report))
