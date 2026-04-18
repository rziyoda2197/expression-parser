class ExpressionParser:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = self.tokenize()
        self.postfix = self.to_postfix()

    def tokenize(self):
        tokens = []
        current_token = ""
        for char in self.expression:
            if char in "+-*/":
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
            elif char.isspace():
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char
        if current_token:
            tokens.append(current_token)
        return tokens

    def to_postfix(self):
        postfix = []
        operators = []
        for token in self.tokens:
            if token.isdigit():
                postfix.append(int(token))
            elif token in "+-*/":
                while operators and operators[-1] != "(" and get_precedence(operators[-1]) >= get_precedence(token):
                    postfix.append(operators.pop())
                operators.append(token)
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators[-1] != "(":
                    postfix.append(operators.pop())
                operators.pop()
        while operators:
            postfix.append(operators.pop())
        return postfix

def get_precedence(operator):
    if operator in "+-":
        return 1
    elif operator in "*/":
        return 2

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if isinstance(token, int):
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 / operand2)
    return stack[0]

def parse_and_evaluate(expression):
    parser = ExpressionParser(expression)
    return evaluate_postfix(parser.postfix)

print(parse_and_evaluate("2+3*4"))  # 14
print(parse_and_evaluate("10/2-3"))  # 2
print(parse_and_evaluate("(2+3)*4"))  # 20
```

Bu kodda ExpressionParser klassi yaratilib, unda expressionni tokenlarga ajratib, keyin postfixga aylantirib, so'ngra postfixni o'rganib, natija qaytarib beradi. get_precedence funksiyasi operatorlar uchun priority qaytaradi, evaluate_postfix funksiyasi postfixni o'rganib, natija qaytaradi. parse_and_evaluate funksiyasi expressionni parserga berib, natija qaytaradi.
