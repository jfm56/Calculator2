## **Command-Line Calculator with Plugin System**

---

## **📌 Overview**

This modular command-line calculator is designed with a plugin-based architecture, enabling dynamic addition of new arithmetic operations. The system provides an interactive menu, history tracking, and comprehensive testing with 100% coverage.
Built with Python 3.13+, the calculator leverages plugins for operations, pytest for testing, and Faker for dynamic test generation. It also supports custom test records via the --num_record CLI option.
🌟 Features

✅ Plugin-Based System – Easily extendable with dynamically loaded arithmetic operations
✅ Interactive REPL Mode – Menu-driven interface with real-time calculations
✅ History Tracking – View, retrieve, and clear past calculations
✅ Robust Testing Suite – 100% test coverage with pytest, Faker, and parameterized tests
✅ Custom Test Data – Generate test cases dynamically using --num_record=<N>
✅ Code Quality & CI/CD – Linting with Pylint, testing with pytest-cov, and maintainable architecture
✅ Extensible Design – Easily add new arithmetic operations without modifying the core logic

---

## **⚙️ Installation**

Ensure Python 3.13+ is installed. Then, clone the repository and install dependencies:

```bash
git clone https://github.com/jfm56/Calculator2.git
cd Calculator2
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
---

## **🚀 Usage**
**Run the Interactive Menu**
Start the calculator in interactive mode:

```bash
python calculator.py
```
**Perform Direct Command-Line Calculations**

Run operations directly from the terminal:
```bash
python calculator.py add 10 5
# Output: 15
```
```bash
python calculator.py divide 20 4
# Output: 5
```
---

## **📜 Interactive Menu**

The calculator supports an interactive REPL (Read-Eval-Print Loop), allowing users to perform calculations seamlessly.
Run:

```bash
python calculator.py
```
**🔹 Interactive Menu Example:**
```bash
== Welcome to REPL Calculator ==
Type 'menu' for options, or enter calculations (e.g., add 2 3).
>> menu

=== Calculator Menu ===
1. View Available Operations
2. Show Calculation History
3. Show Last Calculation
4. Clear Calculation History
5. Exit Menu

Select an option (1-5): 1

Available Operations:
  - add
  - divide
  - multiply
  - subtract
```

**💡 Example Calculation in REPL Mode:**
```bash
>> add 5 3
Result: 8

>> divide 10 2
Result: 5

>> last
Last Calculation: divide 10 2 = 5

>> history
Calculation History:
1. add 5 3 = 8
2. divide 10 2 = 5

>> clear
History cleared.

>> exit
Exiting calculator...
```
---

## **🛠️ Configuration**

**🎲 Faker-based Test Data**

The test suite uses Faker to generate randomized test cases dynamically.
To control the number of test cases generated:
```bash
pytest --num_record=10
```

---


## **🧪 Testing**

Run the test suite with full coverage:
```bash
pytest --cov=calculator --cov=operations --cov=plugin_loader --cov=history --cov-report=term-missing
```
Check code quality:
```bash
pylint calculator.py operations plugin_loader.py history.py
```
---
## **🔌 Extending the Calculator**

**Adding a New Operation**
To add a new arithmetic operation, follow these steps:
1️⃣ Create a new file in the operations/ directory, e.g., modulus.py
2️⃣ Define a class that inherits from Operation:
```bash
from operation_base import Operation
from decimal import Decimal

class Modulus(Operation):
    """Modulus operation for remainder calculation."""
    @classmethod
    def execute(cls, a, b):
        return Decimal(a) % Decimal(b)
```
3️⃣ The plugin system will automatically load the new operation when the calculator runs.

---
## **📂 Project Structure**
```bash
Calculator2/
│── operations/          # Arithmetic operation plugins
│   ├── add.py
│   ├── subtract.py
│   ├── multiply.py
│   ├── divide.py
│   ├── operation_mapping.py
│── tests/               # Unit tests
│   ├── test_calculator.py
│   ├── test_operations.py
│   ├── test_plugin_loader.py
│   ├── test_history.py
│── calculator.py        # Main CLI program
│── plugin_loader.py     # Plugin system to dynamically load operations
│── history.py           # Tracks calculation history
│── conftest.py          # Test configurations, fixtures, dynamic test generation
│── README.md            # Project documentation
│── requirements.txt     # Dependencies
'''

