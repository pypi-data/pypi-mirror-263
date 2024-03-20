# This module is tested in the test_calculator.py file.

class Calculator:
    '''

    This is a simple calculator that starts at zero and can perform these functions:
    - addition
    - subtraction
    - multiplication
    - division
    - root

    It also has a reset function that resets the calculator to zero.

    '''

    def __init__(self):
        '''Initializes the memory to 0.'''
        self.memory = 0

    def add(self, user_input):
        ''' Adds the user_input to the memory.'''
        self.memory += user_input
        return self.memory

    def subtract(self, user_input):
        '''Subtracts the user_input from the memory.'''
        self.memory -= user_input
        return self.memory

    def multiply(self, user_input):
        '''Multiplies the memory by the user_input.'''
        self.memory *= user_input
        return self.memory

    def divide(self, user_input):
        '''Divides the memory by the user_input.'''
        if user_input == 0:
            raise ValueError('Cannot divide by zero')
        self.memory /= user_input
        return self.memory

    def root(self, user_input):
        '''Takes the square root of the memory.'''
        self.memory **= 1/user_input
        return self.memory

    def reset(self):
        '''Resets the memory to 0.'''
        self.memory = 0
        return self.memory

