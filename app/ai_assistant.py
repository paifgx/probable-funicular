import openai
import os

from dotenv import load_dotenv

load_dotenv()

client = openai.Client(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_chatgpt_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Your are an insurance assistant. Your output should always be in german."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.5,
    )

    # Stream response example
    # stream = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "Your are an insurance assistant."},
    #         {"role": "user", "content": prompt},
    #     ],
    #     max_tokens=150,
    #     temperature=0.5,
    #     stream=True,
    # )

    return response.choices[0].message.content

def assist_customer_query(customer_query: str) -> str:
    prompt = f"A customer asked {customer_query}. Provide a response sutiable for an insurance company."
    return get_chatgpt_response(prompt)

def process_claim_with_assistant(claim_description: str, claim_amount: int) -> str:
    prompt = f"A claim was filed with the description: '{claim_description}' and amount: {claim_amount}. Provide guidance on processing this claim."
    return get_chatgpt_response(prompt)

def insurance_advice(policy_type: str) -> str:
    prompt = f"Provide advice on the {policy_type} insurance policy for a customer, including general benefits and any conditions they should be aware of."
    return get_chatgpt_response(prompt)