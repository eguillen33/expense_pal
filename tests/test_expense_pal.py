import unittest
import expense_pal

class TestExpensePal(unittest.TestCase):
    def setUp(self):
        # Resets the global DataFrame before each test
        expense_pal.df = expense_pal.df.iloc[0:0]
        
    def test_add_transaction(self):
        # Check that a transaction is correctly added
        initial_len = len(expense_pal.df)
        expense_pal.add_transaction("2025-01-01", "Groceries", -100)
        self.assertEqual(len(expense_pal.df), initial_len + 1)
        txn = expense_pal.df.iloc[-1]
        self.assertEqual(txn['Date'], "2025-01-01")
        self.assertEqual(txn['Category'], "Groceries")
        self.assertEqual(txn['Amount'], -100)
        
if __name__ == '__main__':
    unittest.main()
        