# General Expressions

## Overview
These questions involve simplifying algebraic expressions containing square roots or evaluating custom-defined mathematical operations. The central idea is to treat the expression as a sequence of operations: simplify roots first, then perform arithmetic according to the order of operations (BODMAS).

---

## Recognition Clues
* **Custom Operators:** Look for symbols like `*` or `#` defined by a specific formula (e.g., $a * b * c = \dots$).
* **Missing Variables:** Equations containing a `?` or $x$ inside or outside a square root.
* **Complex Fractions:** Expressions involving multiple square roots in the numerator and denominator.
* **Goal:** You are asked to "Simplify," "Find the value," or "Find $x$."

---

## Key Formulas

### Custom Operation Formula
$$
a * b * c = \frac{\sqrt{(a + 2)(b + 3)}}{c + 1}
$$
**Variables:** $a, b, c$ are the input numbers provided in the question.
**When to use:** When the question defines a custom operation using a specific symbol.
**Worked example:** For $6 * 15 * 3$, substitute $a=6, b=15, c=3$: $\frac{\sqrt{(6+2)(15+3)}}{3+1} = \frac{\sqrt{8 \times 18}}{4} = \frac{12}{4} = 3$.

### Square Root Equation
$$
\sqrt{f(x)} = k \implies f(x) = k^2
$$
**Variables:** $f(x)$ is the expression under the root, $k$ is the constant on the other side.
**When to use:** To isolate a variable $x$ trapped inside a square root.
**Worked example:** For $\sqrt{5 + x^2} = 3$, square both sides: $5 + x^2 = 9 \implies x^2 = 4 \implies x = 2$.

---

## Solution Framework

1. **Simplify Roots:** Evaluate all perfect square roots immediately to reduce the complexity of the expression.
2. **Substitute:** If a custom formula is given, map the numbers in the question directly to the variables $a, b, c$ in the formula.
3. **Isolate:** If solving for $x$, move all constants to one side and the variable term to the other.
4. **Square Both Sides:** If the variable is under a root, square both sides of the equation to eliminate the radical.
5. **Final Arithmetic:** Perform the remaining multiplication, division, or subtraction to reach the final value.

---

## Shortcut Tricks
* **Trick:** Simplify fractions before multiplying.
* **Why it works:** It keeps the numbers small and prevents overflow errors during manual calculation.
* **When to use:** In expressions like $\frac{112}{\sqrt{196}} \times \frac{\sqrt{576}}{12}$.
* **Example:** Instead of multiplying $112 \times 24 \times 16$, calculate $\frac{112}{14}=8$, $\frac{24}{12}=2$, and $\frac{16}{8}=2$. Then $8 \times 2 \times 2 = 32$.

---

## Common Mistakes
* **Mistake:** Squaring only the variable instead of the whole side of the equation.
* **Why it happens:** Rushing the algebra.
* **Fix:** Always put parentheses around the entire side before squaring: $( \dots )^2$.
* **Mistake:** Miscalculating square roots of decimals (e.g., $\sqrt{0.09} = 0.3$, not $0.03$).
* **Why it happens:** Miscounting decimal places.
* **Fix:** Convert decimals to fractions (e.g., $\sqrt{\frac{9}{100}} = \frac{3}{10} = 0.3$).

---

## Worked Example (Step-by-Step)

**Question:** If $\sqrt{1 + \frac{x}{144}} = \frac{13}{12}$, then find the value of $x$.

**Solution:**
1. **Square both sides:** $1 + \frac{x}{144} = (\frac{13}{12})^2$.
2. **Expand the square:** $1 + \frac{x}{144} = \frac{169}{144}$.
3. **Isolate the fraction:** $\frac{x}{144} = \frac{169}{144} - 1$.
4. **Simplify:** $\frac{x}{144} = \frac{169 - 144}{144} = \frac{25}{144}$.
5. **Solve:** Since denominators match, $x = 25$.

**Answer:** 25

---

## Similar Patterns
**Algebraic Identities:** Distinguish these by the presence of variables like $(a+b)^2$ or $a^2-b^2$ without square roots; General Expressions will always feature radicals or custom-defined operations.

---

## Revision Summary
* **Key formula:** $\sqrt{f(x)} = k \implies f(x) = k^2$.
* **Spot it by:** Custom symbols ($*$) or variables inside square roots.
* **First move:** Evaluate all visible square roots first.
* **Fastest method:** Simplify fractions individually before multiplying.
* **Biggest trap:** Forgetting to square the entire side of an equation.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Square Root** — The value that, when multiplied by itself, gives the original number ($\sqrt{144} = 12$).
* **BODMAS** — The order of operations: Brackets, Orders (roots/powers), Division, Multiplication, Addition, Subtraction.

### Formulas You Must Know First
$$
(a+b)^2 = a^2 + 2ab + b^2
$$
**What it means:** Used to expand squared binomials.
**Example:** $(10+2)^2 = 100 + 40 + 4 = 144$.

### Terms Used In This Pattern
* **Radical:** The symbol $\sqrt{}$ used to denote a root.
* **Constant:** A fixed numerical value that does not change.