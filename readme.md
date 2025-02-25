# **Command-Line Calculator with Plugin System**

## **Overview**
This project is a modular command-line calculator supporting arithmetic operations through a **plugin-based architecture**. It allows easy extension by dynamically loading operations as plugins. The calculator includes an **interactive menu**, **history tracking**, and **robust unit tests with 100% coverage**.

## **Features**
✅ **Modular Plugin System** – Dynamically load arithmetic operations  
✅ **Interactive Menu** – Command-line interface with user-friendly options  
✅ **History Tracking** – Retrieve, clear, and manage calculation history  
✅ **Comprehensive Testing** – 100% test coverage with **pytest**, **Faker**, and **parameterized tests**  
✅ **Custom Test Data** – Dynamic test generation with `--num_record` CLI option  
✅ **CI/CD Ready** – Clean, maintainable code with **Pylint** and **pytest-cov** integration  

---

## **Installation**
Ensure you have Python **3.13+** installed. Then, clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/Calculator2.git
cd Calculator2
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

---

## **Usage**
Run the interactive menu to perform calculations:

'''bash
python calculator.py

---

## **Command-line Operations**

You can also run calculations directly:

''bash
python calculator.py add 5 3
# Output: 8

---

## **Interactive Menu**
The calculator supports an interactive REPL (Read-Eval-Print Loop) for seamless calculations:

'''bash
python calculator.py

🔹 Options Available: 
1️⃣ Perform addition, subtraction, multiplication, and division
2️⃣ View calculation history
3️⃣ Retrieve last calculation
4️⃣ Clear calculation history
5️⃣ Exit the application

---

## **Configuration**
Faker-based Test Data
The test suite uses Faker to generate randomized test cases dynamically. You can control the number of records using:

'''bash
pytest --num_record=10

---

## **Testing**
Run the test suite with full coverage:

'''bash
pytest --cov=calculator --cov=operations --cov=plugin_loader --cov=history --cov-report=term-missing

To check code quality:

'''bash
pylint calculator.py operations plugin_loader.py history.py

---

## **Extending the Calculator**

Adding a New Operation
1️⃣ Create a new file in the operations/ directory, e.g., modulus.py
2️⃣ Define a class inheriting from Operation:

'''python
from operation_base import Operation
from decimal import Decimal

class Modulus(Operation):
    """Modulus operation for remainder calculation."""
    @classmethod
    def execute(cls, a, b):
        return Decimal(a) % Decimal(b)

3️⃣ The plugin system will automatically load your operation when the calculator runs.

---

## **Project Structure**

'''bash
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
