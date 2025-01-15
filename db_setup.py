import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Create the 'users' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL
);
""")

# Insert 10 users into the 'users' table
users = [
    ("Alice", "alice@example.com", 25),
    ("Bob", "bob@example.com", 30),
    ("Charlie", "charlie@example.com", 35),
    ("David", "david@example.com", 40),
    ("Eve", "eve@example.com", 28),
    ("Frank", "frank@example.com", 33),
    ("Grace", "grace@example.com", 29),
    ("Hank", "hank@example.com", 36),
    ("Ivy", "ivy@example.com", 27),
    ("Jack", "jack@example.com", 31),
]
cursor.executemany("""
INSERT INTO users (name, email, age)
VALUES (?, ?, ?)
""", users)

# Create the 'cars' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users (id)
);
""")

# Insert sample cars into the 'cars' table
cars = [
    ("Toyota", "Corolla", 2020, 1),
    ("Honda", "Civic", 2018, 2),
    ("Ford", "Focus", 2019, 3),
    ("Tesla", "Model 3", 2021, 4),
    ("Chevrolet", "Malibu", 2017, 5),
    ("BMW", "X5", 2016, 6),
    ("Audi", "A4", 2022, 7),
    ("Nissan", "Altima", 2020, 8),
    ("Hyundai", "Elantra", 2015, 9),
    ("Kia", "Sorento", 2023, 10),
]
cursor.executemany("""
INSERT INTO cars (make, model, year, owner_id)
VALUES (?, ?, ?, ?)
""", cars)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")

