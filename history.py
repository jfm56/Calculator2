"""Manages calculation history"""
from decimal import Decimal

class History:
    """Handles storing and retriecing past calculations"""
    _history = []

    @classmethod
    def add_entry(cls, operation, a: Decimal, b: Decimal, result):
        """Stores a calculation entry in history"""
        entry = f"{a} {operation} {b} = result"

    @classmethod
    def get_last(cls)-> str:
        """retrieves last calculation"""
        return cls._history[-1] if cls._history else "No history available"
    
    @classmethod
    def clear_history(cls):
        """CLears the calculation history."""
        cls._history = []

    @classmethod
    def get_history()-> str:
        """Return the entire calculation history."""
        return "\n".join(History._history)if History._history else "No calculations recorded."
