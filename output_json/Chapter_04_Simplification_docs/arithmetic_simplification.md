# Arithmetic Simplification

## Overview
This pattern involves solving expressions containing multiple arithmetic operations (addition, subtraction, multiplication, division) and brackets. The central idea is to strictly follow the **BODMAS** rule to ensure the correct sequence of operations, preventing common calculation errors.

---

## Recognition Clues
* **Keywords:** "Simplify," "What should come in place of the question mark," or long strings of numbers with mixed operators.
* **Given:** An equation or expression with one or more missing values (represented by `?` or $x$).
* **Asked:** The value of the missing variable that satisfies the equation.
* **Visual:** Presence of nested brackets `( )`, `{ }`, `[ ]`, or division signs `÷` in sequence.

---

## Key Formulas

### BODMAS Rule
$$
\text{B} \rightarrow \text{O} \rightarrow \text{D} \rightarrow \text{M} \rightarrow \text{A} \rightarrow \text{S}
$$
**Variables:**
- **B**: Brackets (solve innermost first: `( )`, then `{ }`, then `[ ]`)
- **O**: Of (multiplication)
- **D**: Division
- **M**: Multiplication
- **A**: Addition
- **S**: Subtraction

**When to use:** Every time you see an expression with more than one type of operator.

**Worked example:** $13 \times 252 \div 42 + 170$.
1. Division: $252 \div 42 = 6$.
2. Multiplication: $13 \times 6 = 78$.
3. Addition: $78 + 170 = 248$.

---

## Solution Framework

1. **Identify the missing variable:** Replace `?` with $x$ to treat the expression as a solvable equation.
2. **Clear Brackets:** Solve all operations inside the innermost brackets first, working outward.
3. **Apply BODMAS:** Perform Division and Multiplication (left to right), then Addition and Subtraction (left to right).
4. **Isolate the variable:** Use basic algebraic transposition (moving constants to one side) to solve for $x$.
5. **Verify:** Perform a quick mental check to ensure the result is logical.

---

## Shortcut Tricks

* **Trick:** When you see $a \div b \div c$, rewrite it as $\frac{a}{b \times c}$.
* **Why it works:** Division is the inverse of multiplication; dividing by $b$ then by $c$ is the same as dividing by the product of $b$ and $c$.
* **When to use it:** Whenever multiple division signs appear in a row.
* **Example:** $3456 \div 12 \div 8 \rightarrow \frac{3456}{12 \times 8} = \frac{3456}{96} = 36$.

---

## Common Mistakes

* **Mistake:** Multiplying before dividing in sequences like $a \times b \div c$.
    * **Fix:** Always process division and multiplication from left to right.
* **Mistake:** Incorrectly handling division by a fraction (e.g., $x \div \frac{1}{2} = \frac{x}{2}$).
    * **Fix:** Remember that $x \div \frac{a}{b} = x \times \frac{b}{a}$.
* **Mistake:** Sign errors when moving terms across the equals sign.
    * **Fix:** When moving a term, change its sign (positive becomes negative, negative becomes positive).

---

## Worked Example (Step-by-Step)

**Question:** $3565 \div 23 + 4675 \div ? = 430$

**Solution:**
1. **Identify:** Let $x$ be the missing number: $3565 \div 23 + 4675 \div x = 430$.
2. **BODMAS (Division):** Solve $3565 \div 23 = 155$.
3. **Equation:** $155 + \frac{4675}{x} = 430$.
4. **Isolate:** Subtract $155$ from both sides: $\frac{4675}{x} = 430 - 155 = 275$.
5. **Solve:** $x = \frac{4675}{275} = 17$.

**Answer:** $17$

---

## Similar Patterns
* **Algebraic Identities:** If the expression contains squares or cubes (e.g., $a^2 - b^2$), use algebraic formulas instead of raw arithmetic.

---

## Revision Summary
* **Key formula:** BODMAS (Brackets, Of, Division, Multiplication, Addition, Subtraction).
* **Spot it by:** Mixed operators and brackets in a single expression.
* **First move:** Replace `?` with $x$ and simplify inside brackets.
* **Fastest method:** Process division and multiplication left-to-right.
* **Biggest trap:** Dividing by a fraction as if it were a whole number.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Order of Operations** — The mathematical convention that dictates which part of an expression to solve first.
* **Transposition** — Moving a term from one side of an equation to the other by changing its sign.
* **Fractional Division** — The rule that $a \div \frac{b}{c} = a \times \frac{c}{b}$.

### Formulas You Must Know First
* **Quadratic Formula (for $x^2$ terms):** $(x-a)(x-b) = x^2 - (a+b)x + ab$.

### Terms Used In This Pattern
* **BODMAS:** The acronym for the order of operations.
* **Variable:** The unknown value represented by `?` or $x$.