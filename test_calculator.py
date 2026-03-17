import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        self.assertEqual(divide(5, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
```
4. Click **Commit changes** → **Commit directly to main**

---

### Step 3 — Add `requirements.txt`
1. Click **Add file** → **Create new file**
2. Name it: `requirements.txt`
3. Paste:
```
pytest
```
4. Click **Commit changes** → **Commit directly to main**

---

## ⚠️ One Important Fix for Jenkins

Your repo branch is **`main`** but Jenkins is set to **`*/master`**. You need to fix this in Jenkins:

1. Go to your Jenkins Job → **Configure**
2. Scroll to **Branches to build**
3. Change `*/master` → `*/main`
4. Click **Save**

---

After all 3 files are added, your repo should look like:
```
Web_Extension/
├── README.md
├── calculator.py
├── test_calculator.py
└── requirements.txt
