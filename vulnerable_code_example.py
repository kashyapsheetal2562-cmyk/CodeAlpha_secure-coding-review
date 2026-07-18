# 🔒 Vulnerable Code Example
# This file demonstrates insecure coding practices and their secure alternatives.

import sqlite3
import os
import bcrypt

# -------------------------------
# ❌ Insecure Example: Hardcoded Credentials
# -------------------------------
USERNAME = "admin"
PASSWORD = "12345"  # Weak, hardcoded password

def login_insecure(user, pwd):
    if user == USERNAME and pwd == PASSWORD:
        return "Login successful"
    return "Access denied"


# -------------------------------
# ✅ Secure Fix: Environment Variables + Strong Hashing
# -------------------------------
SECURE_USERNAME = os.getenv("APP_USERNAME")
SECURE_PASSWORD_HASH = bcrypt.hashpw(
    os.getenv("APP_PASSWORD").encode("utf-8"), bcrypt.gensalt()
)

def login_secure(user, pwd):
    if user == SECURE_USERNAME and bcrypt.checkpw(pwd.encode("utf-8"), SECURE_PASSWORD_HASH):
        return "Login successful"
    return "Access denied"


# -------------------------------
# ❌ Insecure Example: SQL Injection Risk
# -------------------------------
def get_user_insecure(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Vulnerable: string concatenation allows injection
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    return cursor.fetchall()


# -------------------------------
# ✅ Secure Fix: Parameterized Query
# -------------------------------
def get_user_secure(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Safe: parameterized query prevents injection
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchall()


# -------------------------------
# ❌ Insecure Example: Plaintext Password Storage
# -------------------------------
def store_password_insecure(password):
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")  # Plaintext storage


# -------------------------------
# ✅ Secure Fix: Hashed Password Storage
# -------------------------------
def store_password_secure(password):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    with open("passwords.txt", "a") as f:
        f.write(hashed.decode("utf-8") + "\n")  # Secure storage
