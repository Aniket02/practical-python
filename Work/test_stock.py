import unittest
import stock

class TestStock(unittest.TestCase):

    def test_stock_creation(self):
        s = stock.Stock(name='AAPL', shares=10, price=150.0)
        self.assertEqual(s.name, 'AAPL')
        self.assertEqual(s.shares, 10)
        self.assertEqual(s.price, 150.0)

    def test_stock_cost(self):
        s = stock.Stock(name='AAPL', shares=10, price=150.0)
        self.assertEqual(s.cost, 1500.0)

    def test_stock_sell(self):
        s = stock.Stock(name='AAPL', shares=10, price=150.0)
        s.sell(shares=5)
        self.assertEqual(s.shares, 5)

    def test_shares_type(self):
        s = stock.Stock(name='AAPL', shares=10, price=150.0)
        with self.assertRaises(TypeError):
            s.shares = '100'

if __name__ == '__main__':
    unittest.main()