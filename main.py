import random

class Encryptor:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        encrypted_number = self._perform_operation()
        return f"Encrypted number: {encrypted_number}"

    def _perform_operation(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            return self.number + operand
        elif operation == '-':
            return self.number - operand
        elif operation == '*':
            return self.number * operand
        elif operation == '/':
            return self.number / operand

encryptor = Encryptor(42)

print(encryptor)
