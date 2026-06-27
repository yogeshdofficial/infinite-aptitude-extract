# Custom Operations

## Overview
These questions define a new, non-standard mathematical symbol (like `*`, `@`, or `⊕`) and provide a specific rule for how to calculate it. The central idea is **substitution**: treat the defined rule as a function and replace the variables with the numbers provided in the question.

---

## Recognition Clues
* **Symbol definition:** Look for phrases like "If * is an operation such that..." or "If $x \oplus y = ...$".
* **Given:** A specific rule involving variables (e.g., $x * y = 3x + 2y$).
* **Asked:** The value of an expression using that symbol (e.g., $2 * 3 + 3 * 4$).
* **Nested operations:** Look for parentheses inside the operation, like $3 * (3 * 1)$.

---

## Key Formulas

### Custom Operation Rule
$$
\text{Expression} = \text{Defined Rule}
$$

**Variables:**
- $x, y, a, b$ = placeholders for the numbers provided in the question.

**When to use:** Every time you see a custom symbol.

**Worked example:** Given $x * y = 3x + 2y$. To find $2 * 3$:
Substitute $x=2, y=3 \rightarrow 3(2) + 2(3) = 6 + 6 = 12$.

---

## Solution Framework

1. **Identify the rule:** Write down the formula exactly as given in the question.
2. **Handle parentheses first:** If the expression has nested operations (e.g., $3 * (3 * 1)$), calculate the value inside the inner brackets first.
3. **Substitute carefully:** Replace the variables in the formula with the specific numbers provided, ensuring you don't swap the order of $x$ and $y$.
4. **Simplify:** Perform the arithmetic (multiplication/powers first, then addition/subtraction) to find the result.
5. **Combine:** If the question asks for a sum or combination of multiple operations, add the final results of each part.

---

## Shortcut Tricks
* **No shortcut faster than the standard framework:** Because every question defines a unique rule, you must perform the substitution manually. The "trick" is to write the formula clearly on your scratchpad to avoid mixing up $x$ and $y$.

---

## Common Mistakes
* **Swapping variables:** If the rule is $x * y = 3x + 2y$, calculating $y * x$ instead of $x * y$ will lead to the wrong answer if the coefficients are different.
* **Order of operations:** Forgetting to calculate the inner bracket first in nested expressions like $3 * (3 * 1)$.
* **Arithmetic errors:** Squaring or multiplying incorrectly, especially with negative numbers or fractions.

---

## Worked Example (Step-by-Step)

**Question:** If $x \oplus y = x^2 + 2y$, what is the value of $p$ if $4 \oplus (3 \oplus p) = 50$?

**Solution:**
1. **Inner operation:** Calculate $(3 \oplus p)$ using the rule $x^2 + 2y$. Here $x=3, y=p$.
   $3 \oplus p = 3^2 + 2p = 9 + 2p$.
2. **Substitute back:** The equation becomes $4 \oplus (9 + 2p) = 50$.
3. **Outer operation:** Apply the rule again where $x=4$ and $y=(9 + 2p)$.
   $4^2 + 2(9 + 2p) = 50$.
4. **Simplify:** $16 + 18 + 4p = 50 \rightarrow 34 + 4p = 50$.
5. **Solve for $p$:** $4p = 50 - 34 \rightarrow 4p = 16 \rightarrow p = 4$.

**Answer:** $p = 4$

---

## Similar Patterns
* **Algebraic Simplification:** These are distinct because they use standard operators ($+, -, \times, \div$) rather than custom symbols. If you see a standard symbol, use BODMAS; if you see a custom symbol, use the provided rule.

---

## Revision Summary
* **Key formula:** Substitute given numbers into the provided rule.
* **Spot it by:** A custom symbol like `*`, `@`, or `⊕` defined in the question.
* **First move:** Solve the innermost parentheses first.
* **Fastest method:** Write the rule clearly and substitute values one by one.
* **Biggest trap:** Swapping the order of variables (e.g., using $y$ where $x$ should be).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Order of Operations (BODMAS):** Brackets, Of, Division, Multiplication, Addition, Subtraction.
* **Substitution:** Replacing a variable with a specific numerical value.

### Formulas You Must Know First
* **Basic Algebra:** $(a+b)^2 = a^2 + b^2 + 2ab$ and $(a-b)^2 = a^2 + b^2 - 2ab$. (Useful for simplifying rules involving squares).

### Terms Used In This Pattern
* **Operation:** A mathematical process defined by a rule.
* **Variable:** A placeholder (like $x$ or $y$) that takes on the value of the numbers provided.