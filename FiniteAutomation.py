import random
"""
lab 8
"""

"""
1a)
Задано множину продукцій у формі Бекуса-Наура:

<E> ::= (<E>) | <E> + <E> | <E> * <E> | <V> | <C>
<V> ::= x | y
<C> ::= 1 | 2

Вивести ланцюжок (для відповідного варіанту з таблиці 1). Намалювати дерево
виведення.
"""

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def infix_to_expression_tree(infix_expression):
    # Пріоритети операторів
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(token):
        return token in precedence

    def higher_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    stack = []
    postfix = []
    tokens = infix_expression.split()

    # Перетворення інфіксного виразу в постфіксний
    for token in tokens:
        if token.isalnum():
            postfix.append(token)
        elif is_operator(token):
            while stack and is_operator(stack[-1]) and higher_precedence(stack[-1], token):
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

    while stack:
        postfix.append(stack.pop())

    stack = []

    # Побудова дерева виразу з постфіксного виразу
    for token in postfix:
        if token.isnumeric():
            stack.append(Node('C', [Node(token)]))
        elif token == 'x' or token == 'y':
            stack.append(Node('V', [Node(token)]))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node('E', [left, Node(token), right]))

    return stack.pop()

def print_expression_tree(root, depth=0, is_left=None):
    if root:
        connector = " └── " if is_left else " ├── " if is_left is not None else ""
        print("  " * depth + connector + str(root.value))
        for i, child in enumerate(root.children):
            print_expression_tree(child, depth + 1, i == len(root.children) - 1)



"""
1b)
Дано граматику G=(V,T,S,P), де V={0,1,S,A,B}, T={0,1}, S -- початковий символ.
Виконати наступні завдання (для відповідного варіанту з таблиці 2):
    1. Побудувати мову, породжену такою граматикою.
    2. Визначити тип граматики;
    3. Побудувати недетермінований скінчений автомат, що допускає мову,
    породжену даною граматикою; задати автомат діаграмою та
    таблицею. (додано у звіті)

"""


def build_language_by_grammar(grammar_array_productions):
    for production in grammar_array_productions:
        for i in range(len(production)):
            if any(char.isalpha() for char in production[i]) and any(char.isdigit() for char in production[i]):
                production[i] = production[i][0] + random.choice(["1", "0"])

    # Print the modified productions
    for production in grammar_array_productions:
        if production[0] == "S":
            print(production[1])

def is_regular_grammar(grammar_array_productions):
    for production in grammar_array_productions:
        # Умова 1: Кожне правило продукції має один символ на лівій стороні
        if len(production[0]) != 1:
            return False

        # Умова 2: Перевірка форми правил продукції
        if len(production) == 3 and production[1] == '->':
            left_symbol = production[0]
            right_sequence = production[2]

            # Перевірка чи правило виглядає як A -> xB або A -> x
            if left_symbol.isupper() and all(char.isalnum() or char in "ε" for char in right_sequence):
                continue  # Перейти до наступного правила
            else:
                return False

        else:
            return False

    # Умови 3-5 можна перевірити з допомогою додаткових перевірок

    # Умова 3: Немає ε-переходів (порожніх правил)
    if any("ε" in production for production in grammar_array_productions):
        return False

    # Умова 4: Немає ліворекурсивних правил
    for production in grammar_array_productions:
        left_symbol = production[0]
        right_sequence = production[2]

        if left_symbol.isupper() and right_sequence.startswith(left_symbol):
            return False

    # Умова 5: Немає вкладених продукцій
    for production in grammar_array_productions:
        right_sequence = production[2]

        if any(char.isupper() for char in right_sequence):
            return False

    return True


def type_of_grammar(grammar_array_productions):
    # Check if the grammar is regular (Type 3)
    if is_regular_grammar(grammar_array_productions):
        return "3 - регулярна"

    # Check if the grammar is context-free (Type 2)
    for production in grammar_array_productions:
        for i in range(len(production)):
            if (production[0] == "A" and production[0] != "B") or (production[0] == "B" and production[0] != "A"):
                return "2 - контекстно вільна"

    # Check if the grammar is context-sensitive (Type 1)
    for production in grammar_array_productions:
        for i in range(len(production)):
            if (production[i][0] in "Λλ") or (len(production[0]) <= len(production[1])):
                return "1 - контекстно залежна"

    # If none of the above conditions are met, the grammar is unrestricted (Type 0)
    return "0 - необмежена"


"""
1c)
Побудувати граматику, яка породжує мову (для відповідного варіанту з таблиці 3).
"""


def build_grammar(lit1, lit2):
    n = random.choice([1, 10])
    return str(lit1) * (2*n) + str(lit2) * (n+1)
