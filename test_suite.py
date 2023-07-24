```python
import unittest
from PythoniZerAI import PythoniZerAI

class TestPythoniZerAI(unittest.TestCase):

    def setUp(self):
        self.pythonizer = PythoniZerAI()

    def test_run_script(self):
        script = "print('Hello, World!')"
        output = self.pythonizer.run_script(script)
        self.assertEqual(output, 'Hello, World!')

    def test_nlp(self):
        query = "print a greeting"
        code = self.pythonizer.generate_code(query)
        self.assertEqual(code, "print('Hello, World!')")

    def test_nlu(self):
        query = "create a function that adds two numbers"
        code = self.pythonizer.generate_code(query)
        self.assertEqual(code, "def add(a, b):\n    return a + b")

    def test_pricing_tiers(self):
        self.assertEqual(self.pythonizer.get_tier_features('free'), ['Android', 'web'])
        self.assertEqual(self.pythonizer.get_tier_features('premium'), ['limited resources', 'secure environment'])
        self.assertEqual(self.pythonizer.get_tier_features('enterprise'), ['regulated environment', 'AI chatbot'])

if __name__ == '__main__':
    unittest.main()
```