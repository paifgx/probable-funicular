import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from app.customer import VIPCustomer

def perform_statistical_analysis(customers):
    # Create DataFrame
    data = {
        "name": [c.name for c in customers],
        "policy_type": [c.policy_type for c in customers],
        "annual_fee": [c.annual_fee for c in customers],
        "is_vip": [isinstance(c, VIPCustomer) for c in customers]
    }
    df = pd.DataFrame(data)

    # Calculate statistics
    avg_fee = df['annual_fee'].mean()
    avg_fee_by_type = df.groupby('policy_type')['annual_fee'].mean()
    std_dev_fee = df['annual_fee'].std()

    # Display results
    print("Average Annual Fee:", avg_fee)
    print("Average Fee by Policy Type:\n", avg_fee_by_type)
    print("Standard Deviation of Fees:", std_dev_fee)

    # Visualizations
    df.groupby('policy_type')['annual_fee'].mean().plot(kind='bar')
    plt.title("Average Annual Fee by Policy Type")
    plt.xlabel("Policy Type")
    plt.ylabel("Average Annual Fee")
    plt.show()
