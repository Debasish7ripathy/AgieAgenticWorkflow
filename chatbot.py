import openai
import requests
from database import query_product_info, get_order_status

openai.api_key = 'openai'

def ask_chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def calculate_discount(price, discount):
    return price - (price * discount / 100)

def compare_prices(product_name):
    # Simplified example; in reality, you'd need to scrape or use APIs of other websites.
    response = requests.get(f"https://api.pricecomparison.com/{product_name}")
    return response.json()