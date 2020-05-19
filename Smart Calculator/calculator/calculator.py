import re

variables = {}


def var_in_dict(key, value):
    if variables.get(key) is None and variables.get(value) is not None:
        variables[f'{key}'] = variables[f'{value}']
    elif variables.get(key) is None and value.isdigit():
        variables[f'{key}'] = int(value)
    elif variables.get(value) is not None:
        variables[f'{key}'] = variables[f'{value}']
    elif variables.get(key):
        variables[f'{key}'] = int(value)
    elif value == 'a2a':
        print('Invalid assignment')
    else:
        print('Unknown variable')


class SmartCalculator:
    def __init__(self, number):
        self.number = number.replace(' ', '')
        self.operation()

    def operation(self):
        position = list(self.number.split('='))
        if '' == self.number:
            pass
        elif '/' in self.number and re.match('/+\w', self.number):
            print('Unknown command')
        elif '=' in self.number:
            try:
                var_in_dict(position[0], position[-1])
            except ValueError:
                print('Invalid Identifier')
        else:
            try:
                if self.number in variables.keys():
                    print(eval(self.number, variables))
                elif '+' in self.number or '-' in self.number or '*' in self.number or '/' in self.number:
                    print(int(eval(self.number, variables)))
                elif not position[0] in variables:
                    return print('Unknown variable')
            except (SyntaxError, NameError):
                print('Invalid expression')


while True:
    num_input = input()
    try:
        variable = list(num_input.replace(" ", "").split('='))
        if len(variable) > 2:
            print('Invalid assignment')
            continue
        elif '=' in num_input:
            if not variable[0].isalpha():
                print('Invalid identifier')
                continue
            elif variables.get(variable[1]) is not None:
                calc = SmartCalculator(num_input)
                continue
        elif num_input == '/exit':
            print('Bye!')
            break
        elif num_input == '/help':
            print('The program calculates the sum of numbers')
            continue
    except SyntaxError:
        print('Unknown command')
    calc = SmartCalculator(num_input)

# numbers = [x.strip() for x in self.number.split()]
# l_num = [int(num) for num in numbers]
# print(l_num)
# m = re.split('[-+/*]', self.number)
