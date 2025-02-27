import pandas
import matplotlib.pyplot as plot
import tkinter as tk
from tkinter import messagebox

# Init DataFrame
df = pandas.DataFrame(columns=['Date', 'Category', 'Amount'])

# Add txn function
def add_transaction(date, category, amount):
    global df
    df = pandas.concat([df, 
                        pandas.DataFrame([{'Date': date, 
                                           'Category': category, 
                                           'Amount': float(amount)}])], 
                       ignore_index=True)

# Generate report function
def generate_report():
    if df.empty:
        return messagebox.showinfo("No Data", "No transactions available.")
    total_income = df[df['Amount'] > 0]['Amount'].sum()
    total_expenses = df[df['Amount'] < 0]['Amount'].sum()
    summary = f"Total Income: ${abs(total_income)}\nTotal Expenses: ${abs(total_expenses)}\nBalance: ${total_income - total_expenses}"
    messagebox.showinfo("Summary Report", summary)
    # Create pie chart for expenses based on category
    df[df['Amount'] < 0].groupby('Category')['Amount'].sum().abs().plot.pie(autopct='%1.1f%%')
    plot.title('Expenses by Category')
    plot.ylabel('')
    plot.show()
    
# GUI Transaction Handling
def handle_add_transaction():
    try:
        add_transaction(
            entries['date_entry'].get(), 
            entries['category_entry'].get(), 
            float(entries['amount_entry'].get())
        )
        messagebox.showinfo("Success", "Transaction added.")
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")


# Run the script. This allows unit testing by wrapping the Tkinter main loop
# This change allows testing of file import functions without triggering the GUI
if __name__ == "__main__":
    app = tk.Tk()
    # GUI
    entries = {}
    app.title("Expense Pal")
    for label, entry in [("Date (YYYY-MM-DD):", 'date_entry'), ("Category:", 'category_entry'), ("Amount:", 'amount_entry')]:
        tk.Label(app, text=label).pack()
        entries[entry] = tk.Entry(app)
        entries[entry].pack()
    tk.Button(app, text="Add Transaction", command=handle_add_transaction).pack()
    tk.Button(app, text="Generate Report", command=generate_report).pack()
    
    app.mainloop()