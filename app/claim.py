class CoverageExceededError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Claim:
    def __init__(self, description: str, amount: float):
        self.description = description
        self.amount = amount
        self.processed = False

    def process_claim(self, policy):
        if self.amount > policy.coverage_amount:
            raise CoverageExceededError("Claim amount exceeds policy coverage.")
        self.processed = True

    def is_valid_claim(self, policy):
        return self.amount <= policy.coverage_amount
