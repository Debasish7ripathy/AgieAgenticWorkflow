from flask import Flask, request, render_template
from chatbot import ask_chatbot, calculate_discount, compare_prices
from database import query_product_info, get_order_status

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    
    if "order status" in user_query.lower():
        order_id = extract_order_id(user_query)  # Implement extract_order_id to get order ID from user_query
        status = get_order_status(order_id)
        return f"Order Status: {status}"
    
    elif "discount" in user_query.lower():
        # Extract price and discount values from user_query
        price = extract_price(user_query)
        discount = extract_discount(user_query)
        discounted_price = calculate_discount(price, discount)
        return f"Discounted Price: {discounted_price}"
    
    elif "compare prices" in user_query.lower():
        product_name = extract_product_name(user_query)  # Implement extract_product_name to get product name
        prices = compare_prices(product_name)
        return f"Price Comparison: {prices}"
    
    else:
        response = ask_chatbot(user_query)
        return f"Chatbot Response: {response}"

def extract_order_id(query):
    # Extract order ID from the query (simplified)
    return query.split()[-1]

def extract_price(query):
    # Extract price from the query (simplified)
    return float(query.split()[1])

def extract_discount(query):
    # Extract discount from the query (simplified)
    return float(query.split()[3])

def extract_product_name(query):
    # Extract product name from the query (simplified)
    return query.split()[-1]

if __name__ == '__main__':
    app.run(debug=True)
