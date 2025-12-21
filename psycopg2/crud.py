# pip install psycopg2-binary
# uv add psycopg2-binary

import psycopg2

# Database connection details (must match your Docker container setup)
DB_NAME = "mydatabase"
DB_USER = "myuser"
DB_PASS = "mypassword"
DB_HOST = "localhost"   # or "127.0.0.1"
DB_PORT = "8000"

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)

cur = conn.cursor()

# 1) Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS flowers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        latin_species VARCHAR(100),
        color VARCHAR(30)
    );
""")

# 2) Insert 3 rows
flowers = [
    ("Rose", "Rosa rubiginosa", "Red"),
    ("Sunflower", "Helianthus annuus", "Yellow"),
    ("Lavender", "Lavandula angustifolia", "Purple")
]

cur.executemany(
    # the %s placeholders prevent SQL injection
    "INSERT INTO flowers (name, latin_species, color) VALUES (%s, %s, %s);",
    flowers
)

# Commit the transaction
conn.commit()

# 3) Read them
cur.execute("SELECT * FROM flowers;")
rows = cur.fetchall()

print("🌸 Flowers in database:")
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()
