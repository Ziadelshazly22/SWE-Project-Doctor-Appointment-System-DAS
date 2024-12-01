import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
connection = sqlite3.connect('database.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create Users Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        approved INTEGER DEFAULT 0
    )
''')

# Insert an admin user for initial access
cursor.execute('''
    INSERT OR IGNORE INTO users (username, password, role, approved) 
    VALUES ('admin', 'admin123', 'admin', 1)
''')

# Commit and close the connection
connection.commit()
connection.close()

print("Database and table created successfully!")
