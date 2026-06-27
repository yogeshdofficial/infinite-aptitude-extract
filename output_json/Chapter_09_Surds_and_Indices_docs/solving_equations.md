# Solving Exponential Equations

## Overview
These questions require finding an unknown variable ($x, y, n$) located in the exponent of an equation. The central strategy is to transform both sides of the equation so they share the same base, allowing you to equate the exponents directly.

---

## Recognition Clues
* **Variable in exponent:** The unknown ($x, y$) appears as a power (e.g., $2^{x-1}$).
* **Base conversion:** The numbers involved are powers of a common small integer (e.g., 2, 3, 5, 17).
* **"Find the value of":** The question explicitly asks for the value of the variable or an expression involving it.
* **Multiple terms:** Equations often involve addition/subtraction of exponential terms (e.g., $2^{x-1} + 2^{x+1} = 1280$).

---

## Key Formulas

### Equality of Exponents
$$
\text{If } a^m = a^n, \text{ then } m = n
$$
**Variables:** $a$ = base, $m, n$ = exponents.
**When to use:** When both sides of the equation are expressed as a single term with the same base.
**Worked example:** If $17^{\frac{1}{x}} = 17^2$, then $\frac{1}{x} = 2$, so $x = 0.5$.

### Product Rule
$$
a^m \times a^n = a^{m+n}
$$
**Variables:** $a$ = base, $m, n$ = exponents.
**When to use:** When multiplying terms with the same base to simplify the equation.
**Worked example:** $x^{\frac{1}{4}} \times x^{\frac{3}{4}} = x^{(\frac{1}{4} + \frac{3}{4})} = x^1$.

---

## Solution Framework

1. **Standardize Bases:** Convert all numbers into powers of the smallest common base (e.g., $8 \to 2^3$, $0.008 \to (\frac{1}{5})^3$).
2. **Simplify Sides:** Use index laws (Product/Power rules) to reduce each side to a single term with the same base.
3. **Factor (if needed):** If terms are added/subtracted, factor out the smallest power (e.g., $2^{x-1}$) to isolate the exponential part.
4. **Equate Exponents:** Once $a^{\text{left}} = a^{\text{right}}$, set the exponents equal to each other: $\text{left} = \text{right}$.
5. **Solve for Variable:** Use basic algebraic manipulation to find the value of the unknown.

---

## Shortcut Tricks

* **Trick:** When you see $a^{x-n} + a^{x+n}$, factor out $a^{x-n}$ immediately.
* **Why it works:** It turns an addition problem into a multiplication problem, allowing you to divide the constant sum by the resulting coefficient.
* **When to use:** Whenever you see multiple exponential terms with the same base separated by $+$ or $-$.
* **Example:** $2^{x-1} + 2^{x+1} = 1280 \to 2^{x-1}(1 + 2^2) = 1280 \to 2^{x-1}(5) = 1280 \to 2^{x-1} = 256 = 2^8 \to x-1=8 \to x=9$.

---

## Common Mistakes

* **Adding Exponents:** Thinking $2^{x-1} + 2^{x+1} = 2^{2x}$. **Fix:** Always factor out the common base term first.
* **Multiplying Exponents:** Calculating $x^{\frac{1}{4}} \times x^{\frac{3}{4}}$ as $x^{\frac{3}{16}}$. **Fix:** Remember $a^m \times a^n = a^{m+n}$.
* **Ignoring the Constant:** Forgetting to divide the total sum by the factored coefficient. **Fix:** Ensure the exponential term is isolated before equating exponents.

---

## Worked Example (Step-by-Step)

**Question:** If $2^{x - 1} + 2^{x + 1} = 1280$, then find the value of $x$.

**Solution:**
1. **Factor:** The smallest power is $2^{x-1}$. Rewrite $2^{x+1}$ as $2^{(x-1)+2} = 2^{x-1} \times 2^2$.
2. **Simplify:** $2^{x-1}(1 + 2^2) = 1280 \to 2^{x-1}(1 + 4) = 1280$.
3. **Divide:** $2^{x-1}(5) = 1280 \to 2^{x-1} = 256$.
4. **Equate:** $256$ is $2^8$. So, $2^{x-1} = 2^8$.
5. **Solve:** $x - 1 = 8 \to x = 9$.

**Answer:** $x = 9$

---

## Similar Patterns
* **Logarithmic Equations:** Distinguished by the presence of "log" notation; these require log properties rather than base-matching.
* **Linear Equations:** Distinguished by the absence of variables in the exponent; these are solved by simple balancing.

---

## Revision Summary
* **Key formula:** $a^m = a^n \implies m = n$.
* **Spot it by:** Variable $x$ appearing in the exponent.
* **First move:** Convert all numbers to the same base.
* **Fastest method:** Factor out the smallest power if terms are added.
* **Biggest trap:** Adding exponents when terms are added (e.g., $2^x + 2^x \neq 2^{2x}$).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Laws of Indices:** Understanding how to manipulate powers (e.g., $a^m \cdot a^n = a^{m+n}$).
* **Fractional Exponents:** Knowing that $a^{\frac{1}{n}} = \sqrt[n]{a}$.
* **Algebraic Balancing:** Moving constants across the equals sign by changing their operation.

### Formulas You Must Know First
* $(a^m)^n = a^{mn}$ (Power of a power rule).
* $a^{-n} = \frac{1}{a^n}$ (Negative exponent rule).

### Terms Used In This Pattern
* **Base:** The number being raised to a power.
* **Exponent:** The power to which a base is raised.
* **Factor:** To extract a common term from an expression.