import sqlite3

def create_connection():
    return sqlite3.connect('retail.db')

def create_tables(conn):
    cursor = conn.cursor()

    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')

    conn.commit()

def populate_tables(conn):
    cursor = conn.cursor()

    # Insert sample data into products table
    cursor.execute('''
        INSERT INTO products (name, description, price, stock)
        VALUES 
        ('Jeans', 'Comfortable denim jeans', 49.99, 100),
        ('Chinos', 'Casual cotton chinos', 39.99, 150),
        ('T-Shirt', 'Basic white t-shirt', 19.99, 200),
        ('Sneakers', 'Stylish running sneakers', 79.99, 50)
    ''')

    # Insert sample data into orders table
    cursor.execute('''
        INSERT INTO orders (customer_name, product_id, quantity, status)
        VALUES 
        ('John Doe', 1, 2, 'Shipped'),
        ('Jane Smith', 2, 1, 'Processing'),
        ('Alice Johnson', 3, 3, 'Delivered'),
        ('Bob Brown', 4, 1, 'Cancelled')
    ''')

    conn.commit()

def main():
    conn = create_connection()
    create_tables(conn)
    populate_tables(conn)
    conn.close()

if __name__ == '__main__':
    main()
