# This module is tested in the test_calculator.py file.

class Calculator:
    '''
    This is a simple calculator that starts at zero and can perform these functions:
    - addition
    - subtraction
    - multiplication
    - division
    - root

    User input is validated to ensure it is a number.
    It also has a reset function that resets the calculator to zero.
    '''

    def __init__(self) -> None:
        '''Initializes the memory to 0.'''
        self.memory: float = 0

    def _validate_input(self, user_input) -> float:
        '''Checks if the input is a number. If not, raises a ValueError.'''
        if not isinstance(user_input, (int, float)):
            raise ValueError("Input must be a number, not a string")
        return user_input

    def add(self, user_input) -> float:
        ''' Adds the user_input to the memory after validation.'''
        num = self._validate_input(user_input)
        self.memory += num
        return self.memory

    def subtract(self, user_input) -> float:
        '''Subtracts the user_input from the memory after validation.'''
        num = self._validate_input(user_input)
        self.memory -= num
        return self.memory

    def multiply(self, user_input) -> float:
        '''Multiplies the memory by the user_input after validation.'''
        num = self._validate_input(user_input)
        self.memory *= num
        return self.memory

    def divide(self, user_input) -> float:
        '''Divides the memory by the user_input after validation.'''
        num = self._validate_input(user_input)
        if num == 0:
            raise ValueError('Cannot divide by zero')
        self.memory /= num
        return self.memory

    def root(self, user_input) -> float:
        '''Takes the user_input root of the memory after validation.'''
        num = self._validate_input(user_input)
        if num <= 0:
            raise ValueError("Root must be greater than 0")
        self.memory **= 1/num
        return self.memory

    def reset(self) -> float:
        '''Resets the memory to 0.'''
        self.memory = 0
        return self.memory
