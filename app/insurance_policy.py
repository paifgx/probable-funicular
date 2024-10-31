class InsurancePolicy:
    def __init__(self, policy_id: int, coverage_amount: float, additional_options=None):
        self.policy_id = policy_id
        self.coverage_amount = coverage_amount
        self.additional_options = additional_options or []

    def add_option(self, option: str):
        if option not in self.additional_options:
            self.additional_options.append(option)
