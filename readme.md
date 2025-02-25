Command-Line Calculator 🧮
An extendable, plugin-based command-line calculator implemented in Python. This calculator supports basic arithmetic operations (addition, subtraction, multiplication, division) through a modular architecture, allowing easy expansion and maintainability.

🚀 Features
Modular Plugin System: Easily add or modify operations without altering core logic.
Built-in Operations:
Addition (add)
Subtraction (subtract)
Multiplication (multiply)
Division (divide)
Interactive REPL Interface: Perform calculations interactively via the terminal.
Interactive Menu: User-friendly CLI menu for easy navigation.
Calculation History: Store, retrieve, and clear your calculation history.
Robust Error Handling: Clear input validation and error messages.
📂 Project Structure
graphql
Copy
Edit
Calculator
├── calculator.py            # Main REPL calculator logic
├── operation_base.py        # Abstract base class for operations
├── operations               # Arithmetic operation plugins
│   ├── add.py
│   ├── subtract.py
│   ├── multiply.py
│   ├── divide.py
│   └── operation_mapping.py
├── plugin_loader.py         # Dynamically loads operation plugins
├── history.py               # Manages calculation history
├── menu.py                  # Interactive CLI menu system
├── tests                    # Unit tests and fixtures
│   ├── test_calculator.py
│   ├── test_operations.py
│   ├── test_operation_base.py
│   ├── test_plugin_loader.py
│   ├── test_history.py
│   ├── test_menu.py
│   └── conftest.py          # Pytest fixtures, Faker integration, and dynamic test data
├── requirements.txt         # Python dependencies
└── README.md
🛠️ Technologies Used
Python 3.13
Abstract Base Classes (ABC) for well-defined interfaces.
Pytest for testing, including dynamic parameterization.
Faker to generate realistic, dynamic test data.
Coverage.py to ensure high test coverage (currently 100%).
Pylint to maintain high-quality code standards.
✅ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/command-line-calculator.git
cd command-line-calculator
Create and activate virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚦 Usage
Launching the Interactive Calculator:
bash
Copy
Edit
python calculator.py
You'll see the interactive menu:

markdown
Copy
Edit
========== Calculator Menu ==========
1. Perform Calculation
2. Show Calculation History
3. Show Last Calculation
4. Clear History
5. Exit
=====================================
Enter choice:
Menu Example:

Choose option 1 to calculate:

sql
Copy
Edit
Enter operation (add, subtract, multiply, divide): multiply
Enter first number: 8
Enter second number: 5
Result: 40
Choose option 2 to view history:

yaml
Copy
Edit
Calculation History:
1: multiply 8 5 = 40
Choose option 4 to clear history:

nginx
Copy
Edit
History cleared successfully!
Direct REPL Commands:
You can also enter commands directly in the REPL interface:

shell
Copy
Edit
> add 10 15
Result: 25
> history
1: add 10 15 = 25
> clear
History cleared successfully!
> exit
Goodbye!
🧪 Testing with Pytest and Faker
Tests use Pytest combined with Faker for dynamic data generation, enabling robust testing across various scenarios.

Running Tests
Basic test execution:

bash
Copy
Edit
pytest
Customizable Test Generation (--num_record):
You can dynamically generate more or fewer test cases by providing the --num_record argument:

bash
Copy
Edit
pytest --num_record=10
The default number of generated test cases is 5.
Increasing this number strengthens test coverage and confidence.
Example Output:

arduino
Copy
Edit
tests/test_calculator.py::test_run_operation_valid[add-10-5-15] PASSED
tests/test_calculator.py::test_run_operation_valid[divide-100-10-10] PASSED
Running Tests with Coverage Report
bash
Copy
Edit
pytest --cov=. --cov-report=term-missing --num_record=10
Example coverage summary:

markdown
Copy
Edit
----------- coverage: platform darwin, python 3.13.2 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
calculator.py              49      0   100%
operation_base.py          35      0   100%
operations/*               71      0   100%
plugin_loader.py           23      0   100%
history.py                 14      0   100%
menu.py                    18      0   100%
tests/*                   265      0   100%
-------------------------------------------
TOTAL                     475      0   100%
📈 Extending the Calculator
To add a new operation (e.g., modulus %):

Create operations/modulus.py:

python
Copy
Edit
from operation_base import Operation

class Modulus(Operation):
    """Modulus operation plugin."""
    
    @classmethod
    def execute(cls, a, b):
        return a % b
No additional setup is required; plugins auto-load on startup.

Run updated tests:

bash
Copy
Edit
pytest --num_record=10
💡 Future Enhancements
Additional mathematical operations (exponentiation, roots, logarithms).
Persistent storage of calculation history (database or file-based).
Graphical or Web-based calculator interface.