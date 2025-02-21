"""Base class for Plugin System"""
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Type

class Operation(ABC):
    """Abstract base class for calculator operations
    
    Attributes:
        registry (dict): A dictionary storing all registered operations.
    """

    registry = {}

    def __init_subclass__(cls, **kwargs):
        """
        Automatically registers subclasses in the operation registry
        
        Args:
            **kwargs: Additional keyword arguments for subclass initialization
        """
        super().__init_subclass__(**kwargs)
        operation_name = cls.__name__.lower()
        if operation_name in Operation.registry:
            raise ValueError(f"Operation '{operation_name}' is already registered.")
        Operation.registry[operation_name]= cls

    @classmethod
    @abstractmethod
    def execute(cls, a: Decimal, b: Decimal)-> Decimal:
        """Abstract method that must be implemented by subclasses.
        Args:

        a (Decimal): First number.
        b (Decimal): Second number.
        Returns:
           Decimal: Result of the operation
             """


    @classmethod
    @abstractmethod
    def validate_numbers(cls, a: Decimal, b: Decimal)-> None:
        """Abstract method for number validation"""


    @classmethod
    def get_operation(cls, name:str) -> Type["Operation"]:
        """
        Retrieve a registered operation class by name.
        
        Args:
            name (str): Name of the operation (case insensitive).
            
        Returns:
            Type Operation: The operation class
            
        Raises:
            KeyError: If the operation is not found.
        """
        operation = cls.registry.get(name.lower())
        if operation is None:
            raise KeyError(f"Operation '{name}' not found in registry.")
        return operation
