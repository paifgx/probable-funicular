from .ai_assistant import assist_customer_query

class Customer:
    def __init__(self, name: str, policy_type: str, annual_fee: float):
        self.name = name
        self.policy_type = policy_type
        self.annual_fee = annual_fee

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def policy_type(self):
        return self._policy_type

    @policy_type.setter
    def policy_type(self, value):
        self._policy_type = value

    @property
    def annual_fee(self):
        return self._annual_fee

    @annual_fee.setter
    def annual_fee(self, value):
        if value <= 0:
            raise ValueError("Annual fee must be positive")
        self._annual_fee = value

    def __str__(self):
        return f"Customer(name={self.name}, policy_type={self.policy_type}, annual_fee={self.annual_fee})"

    def calculate_discounted_fee(self):
        discount = {
            "Private": 0.05,
            "Commercial": 0.10
        }.get(self.policy_type, 0)
        return self.annual_fee * (1 - discount)
    
    def get_help(self, question: str):
        return assist_customer_query(question)

class VIPCustomer(Customer):
    def calculate_discounted_fee(self):
        base_discounted_fee = super().calculate_discounted_fee()
        return base_discounted_fee * 0.85  # Additional 15% discount for VIPs
