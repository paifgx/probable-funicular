class CustomerPolicyManagement:
    def __init__(self):
        self.customer_policies = {}

    def assign_policy_to_customer(self, customer, policy):
        if customer in self.customer_policies:
            raise Exception(f"Customer {customer.name} already has a policy assigned.")
        self.customer_policies[customer] = policy

    def find_customers_by_coverage(self, amount):
        return [customer for customer, policy in self.customer_policies.items() if policy.coverage_amount >= amount]
