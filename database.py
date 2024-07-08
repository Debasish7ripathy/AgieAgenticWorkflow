import sqlite3

def create_connection():
    conn = sqlite3.connect('retail.db')
    return conn

def query_product_info(product_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name=?", (product_name,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_order_status(order_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM orders WHERE id=?", (order_id,))
    result = cursor.fetchone()
    conn.close()
    return result
