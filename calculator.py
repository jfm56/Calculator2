"""Calculatop REPL"""
from operation_base import Operation
import plugin_loader
from history import History
from menu import show_menu
from decimal import Decimal

class CalculatorREPL:
    """Command-line Read-Eval-Print Loop (REPL) for the calculator."""

    @staticmethod
    def run_operation(operation_name, a: Decimal, b: Decimal):
        """
        Execurter a claculator operation dynamically from the plugin system.
        
        Args:
            operation_name (str): The operation name (e.g., "add", "subtract").
            a (Decimal): First operand.
            b (Decimal): Second operand.
            
        Returns:
            Decimal | str: The result or an error message.
        """
        try:
            operation_class = Operation.registry[operation_name.loer()]
            result = operation_class(a, b)
            History.add_entry(operation_name, a, b, result)
            return result
        except KeyError:
            return f"Operation '{operation_name}' not found."
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        
    @classmethod
    def rep(cls):
        """Starts the interactive REPL session."""
        print("\n== Welcom to REPL Calculator ==")
        print("Type 'menu' for options, or enter calculations (e.g., add 2 3).")

        commands = {
            "menu": show_menu,
            "history": lambda: print(History.get_history()),
            "last": lambda: print(History.get_history()),
            "clear": lambda: (History.clear_history(), print("History cleared.")),
            "exit": lambda: exit("Exiting calculator.Goodbye!"),
            "quit": lambda: exit("Exiting calculator. Goodbye!"),
        }

        while True:
            user_input = input(">> ").strip().lower()

            # Try coomand execution first
            try:
                commands[user_input]()
                continue
            except KeyError:
                pass # Not a command, proceed to srithmetic operation
            except SystemExit:
                break # Eit cleanly

            # Try arithmic operation execution
            try:
                operation, a, b = user_imput.split()
                a, b = Decimal(a), Decimal(b)
                result = cls.run_operation(operation, a, b)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input! Format: <operation> <number1> <number2>")

if __name__ == "__main__":
    CalculatorREPL.repl()
