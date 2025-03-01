"""
Command-based Calculator CLI.

Supports basic arithmetic operations, history tracking, and CLI commands.
"""

import importlib
from plugin_loader import _loaded_plugins  # ✅ Keep it as is
from history import History


def calculator_cli():
    """Runs an interactive command-line interface for the calculator."""
    
    history = History()  # Assuming you have a history class

    print("Welcome to the Calculator CLI! Type 'exit' to quit.")

    while True:
        user_input = input("\nEnter command (add, subtract, multiply, divide, history, clear, exit): ").strip().lower()

        if user_input == "exit":
            print("Exiting calculator. Goodbye!")
            break

        elif user_input in ["add", "subtract", "multiply", "divide"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                # ✅ Dynamically load the operation module from `_loaded_plugins`
                module_name = next((m for m in _loaded_plugins if m.endswith(user_input)), None)

                if module_name:
                    module = importlib.import_module(module_name)  # Load the module
                    operation = getattr(module, "operation", None)  # ✅ Retrieve the operation function

                    if operation:
                        result = operation(a, b)
                        print(f"Result: {result}")
                        history.add(user_input, a, b, result)
                    else:
                        print(f"Error: Operation '{user_input}' not found in module {module_name}.")
                else:
                    print(f"Error: No module found for operation '{user_input}'.")

            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif user_input == "history":
            history.display()

        elif user_input == "clear":
            history.clear()

        else:
            print("Invalid command! Please try again.")


if __name__ == "__main__":
    calculator_cli()
