# Project 2: Stack-Based Calculator

## What does it do?

A calculator that evaluates math expressions with proper operator precedence and parentheses support.

**Real-world use**:
- Excel, calculators evaluate formulas
- Compilers parse expressions
- Programming language interpreters

## Which DSA concepts does it use?

1. **Stack** - Manage operators and operands
2. **Operator precedence** - * before +
3. **Parsing** - Convert expression to tokens
4. **Recursion** - Nested parentheses

## How to run it

```bash
python solution.py
```

## Sample input and output

**Input**: `"3 + 5 * 2"`  
**Output**: `13` (not 16, because * has higher precedence)

**Input**: `"( 3 + 5 ) * 2"`  
**Output**: `16` (parentheses force addition first)

**Input**: `"20 / 4 - 2"`  
**Output**: `3`

## What I learned

1. **Stacks manage precedence** - Operators arranged by precedence
2. **Operator precedence matters** - * before +
3. **Parentheses override precedence** - Use stack to handle nesting
4. **Tokenization is key** - Parse before evaluating
5. **Error handling** - Division by zero, unmatched parentheses

## Variations to try

1. **Support exponentiation**: Add ^ operator
2. **Negative numbers**: Handle - as unary and binary
3. **More functions**: Add sin(), cos(), sqrt()
4. **Decimal numbers**: Not just integers
5. **Better error messages**: Tell user where error is

## Algorithm: Shunting Yard

We used the Shunting Yard algorithm (Dijkstra's):
- Two stacks: one for numbers, one for operators
- Process tokens in order
- Apply operators based on precedence
- Parentheses control grouping
