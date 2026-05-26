"""
Project 2: Stack-Based Calculator

WHAT DOES IT DO:
Build a calculator that evaluates expressions using stacks.
Supports: +, -, *, /, parentheses

WHICH DSA CONCEPTS:
1. Stack (operator and operand stacks)
2. Parsing (convert infix to postfix)
3. Recursion (evaluate expressions)

HOW TO RUN:
python solution.py

SAMPLE INPUT:
"3 + 5 * 2"        → 13
"(3 + 5) * 2"      → 16
"10 / 2 - 3"       → 2
"""

class StackCalculator:
    """Simple calculator using stacks."""
    
    def __init__(self):
        self.operator_stack = []
        self.operand_stack = []
    
    def precedence(self, op):
        """Return precedence of operator."""
        if op in ['+', '-']:
            return 1
        elif op in ['*', '/']:
            return 2
        return 0
    
    def apply_operator(self, op, b, a):
        """Apply operator to two operands."""
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ValueError("Division by zero")
            return a // b  # Integer division
    
    def evaluate(self, expression):
        """Evaluate mathematical expression."""
        # Tokenize
        tokens = expression.split()
        
        for token in tokens:
            # Operand: push to operand stack
            if token.isdigit():
                self.operand_stack.append(int(token))
            
            # Operator: process based on precedence
            elif token in ['+', '-', '*', '/']:
                while (self.operator_stack and 
                       self.operator_stack[-1] != '(' and
                       self.precedence(self.operator_stack[-1]) >= self.precedence(token)):
                    op = self.operator_stack.pop()
                    b = self.operand_stack.pop()
                    a = self.operand_stack.pop()
                    self.operand_stack.append(self.apply_operator(op, b, a))
                
                self.operator_stack.append(token)
            
            # Left parenthesis: push
            elif token == '(':
                self.operator_stack.append(token)
            
            # Right parenthesis: pop until matching (
            elif token == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    op = self.operator_stack.pop()
                    b = self.operand_stack.pop()
                    a = self.operand_stack.pop()
                    self.operand_stack.append(self.apply_operator(op, b, a))
                
                if self.operator_stack:
                    self.operator_stack.pop()  # Remove (
        
        # Process remaining operators
        while self.operator_stack:
            op = self.operator_stack.pop()
            b = self.operand_stack.pop()
            a = self.operand_stack.pop()
            self.operand_stack.append(self.apply_operator(op, b, a))
        
        return self.operand_stack[0]

# ── Test cases ────────────────────────────

calc = StackCalculator()

test_cases = [
    ("3 + 5", 8),
    ("10 - 2", 8),
    ("3 * 4", 12),
    ("20 / 4", 5),
    ("3 + 5 * 2", 13),  # Precedence test
    ("( 3 + 5 ) * 2", 16),  # Parentheses test
    ("2 * 3 + 4 * 5", 26),  # Multiple operators
]

print("Stack Calculator Tests:")
for expr, expected in test_cases:
    calc = StackCalculator()  # Reset for each test
    try:
        result = calc.evaluate(expr)
        status = "✓" if result == expected else "✗"
        print(f"{status} {expr} = {result} (expected {expected})")
    except Exception as e:
        print(f"✗ {expr} - Error: {e}")

# COMPLEXITY
print("\n=== COMPLEXITY ANALYSIS ===")
print("Time:  O(n) - each token processed once")
print("Space: O(n) - stacks store operands and operators")
