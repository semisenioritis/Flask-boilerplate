import sqlite3
import hashlib

# Connect to database or create it if it doesn't exist
conn = sqlite3.connect('users.db')

# Create a table for storing user data
conn.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                user_type INTEGER NOT NULL);''')

# Register a new user
def register(username, password, email, user_type):
    # Hash the password for secure storage
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Insert the new user into the database
    try:
        conn.execute("INSERT INTO users (username, password, email, user_type) VALUES (?, ?, ?, ?)", (username, hashed_password, email, user_type))
        conn.commit()
        print("User registered successfully!")
        return True
    except:
        print("Username or email already exists")
        return False

# Login an existing user
def login(username, password):
    # Hash the password to compare it to the stored password
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Check if the user exists and the password matches
    cursor = conn.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    if cursor.fetchone() is not None:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password")
        return False


# Example usage
register("john", "password123", "john@example.com", 1) # admin user
register("jane", "password456", "jane@example.com", 0) # customer user
login("john", "password123")