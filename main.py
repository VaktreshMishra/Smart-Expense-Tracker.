import sqlite3
import datetime

# --- 1. Database Setup ---
DB_NAME = 'expenses.db'
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            category TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()

# --- 2. Core Functions ---
def add_expense(date_str, category, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", 
                   (date_str, category, amount))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()
    conn.close()
    return expenses

# --- 3. Main Interface ---
def main():
    init_db()
    print("--- Smart Expense Tracker ---")
    
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                date_str = input("Date (YYYY-MM-DD): ")
                category = input("Category: ")
                amount = float(input("Amount: "))
                add_expense(date_str, category, amount)
                print("Expense added successfully!")
            except ValueError:
                print("Invalid amount. Please try again.")
        
        elif choice == '2':
            data = view_expenses()
            if data:
                print("\n--- Expense Log ---")
                for row in data:
                    print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ${row[3]:.2f}")
            else:
                print("No expenses recorded.")

        elif choice == '3':
            print("Exiting Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
