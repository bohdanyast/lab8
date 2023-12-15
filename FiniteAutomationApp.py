import FiniteAutomation as fa


# РЕАЛІЗАЦІЯ 1a
infix_expression = "1 + ( x + y ) * ( x + x )"
expression_tree = fa.infix_to_expression_tree(infix_expression)

print(f"\nЗавдання 1а:\nДерево для виразу {infix_expression} має вигляд\n:")
fa.print_expression_tree(expression_tree)


# РЕАЛІЗАЦІЯ 1b
grammar_array_productions = [
    ["S", "1B"],
    ["S", "0"],
    ["A", "1A"],
    ["A", "0B"],
    ["A", "1"],
    ["A", "0"],
    ["B", "1"]
]

print("Завдання 1b:")
print("-----------------------------")
print("1. Мова породжена граматикою:")
fa.build_language_by_grammar(grammar_array_productions)
print("2. Тип граматики:")
print(fa.type_of_grammar(grammar_array_productions))


# РЕАЛІЗАЦІЯ 1c
build_grammar = fa.build_grammar(12, 20)
print("Завдання 1c:")
print("-----------------------------")
print(build_grammar)


# РЕАЛІЗАЦІЯ 1d
print("-----------------------------")
print("Завдання 1d:")

class FiniteAutomaton:
    def __init__(self):
        self.states = {'Q0', 'Q1', 'Q2'}
        self.alphabet = {'0', '1', '2'}
        self.transitions = {
            'Q0': {'0': 'Q0', '1': 'Q2', '2': 'Q2'},
            'Q1': {'0': 'Q2', '1': 'Q1', '2': 'Q2'},
            'Q2': {'0': 'Q2', '1': 'Q0', '2': 'Q2'}
        }
        self.initial_state = 'Q2'
        self.accepting_states = {'Q0', 'Q1'}
        self.current_state = self.initial_state

    def process_input(self, input_string):
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Invalid symbol '{symbol}' in the input.")
                return None

            self.current_state = self.transitions[self.current_state][symbol]

        return self.get_output()

    def get_output(self):
        if self.current_state in self.accepting_states:
            if self.current_state == 'Q0':
                return '0'
            elif self.current_state == 'Q1':
                return '1'
        return '12'


# Приклад використання
input_sequence = "100110001221121212"
automaton = FiniteAutomaton()

output = automaton.process_input(input_sequence)
print(f"Вихід автомата для входу '{input_sequence}': {output}")


from prettytable import PrettyTable

# Задані умови
input_alphabet = {'0', '1', '2'}
output_alphabet = {'0', '1', '12'}
states = {'Q0', 'Q1', 'Q2'}
initial_state = 'Q2'
accepting_states = {'Q0', 'Q1'}

# Задані переходи
transitions = {
    'Q0': {'0': 'Q0', '1': 'Q2', '2': 'Q2'},
    'Q1': {'0': 'Q2', '1': 'Q1', '2': 'Q2'},
    'Q2': {'0': 'Q2', '1': 'Q0', '2': 'Q2'}
}

# Побудова таблиці переходів
transition_table = PrettyTable()
transition_table.field_names = ['Current State'] + list(input_alphabet)

for state in states:
    row = [state]
    for symbol in input_alphabet:
        next_state = transitions[state].get(symbol, '-')
        row.append(next_state)
    transition_table.add_row(row)

print("Transition Table:")
print(transition_table)

# Побудова таблиці виходів
output_table = PrettyTable()
output_table.field_names = ['Current State', 'Output']

for state in states:
    output = '0' if state == 'Q0' else '1' if state == 'Q1' else '12'
    output_table.add_row([state, output])

print("\nOutput Table:")
print(output_table)
