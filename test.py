import mysql.connector

try:
    # Connect to MySQL server
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    c = db.cursor()

    # Create a database
    c.execute("CREATE DATABASE IF NOT EXISTS emp_db")
    print("Database 'emp_db' created successfully!")

    # Show all databases
    c.execute("SHOW DATABASES")
    print("Available Databases:")
    for i in c:
        print(i)

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if db.is_connected():
        c.close()
        db.close()
        print("MySQL connection closed.")
