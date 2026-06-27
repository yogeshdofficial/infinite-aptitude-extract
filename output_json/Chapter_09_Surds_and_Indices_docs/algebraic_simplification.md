# Algebraic Simplification

## Overview
This pattern involves simplifying complex algebraic expressions, often containing negative exponents, fractional powers, or multiple variables linked by equality. The central idea is to transform all terms into a common base or a common denominator to allow for cancellation or equating of exponents.

---

## Recognition Clues
* **Negative Exponents:** Look for terms like $x^{-1}$ or $a^{-n}$.
* **Equality Chains:** Look for expressions like $2^x = 3^y = 6^{-z}$.
* **Variable Substitution:** Look for cyclic equations like $x=y^a, y=z^b, z=x^c$.
* **Complex Fractions:** Look for expressions requiring simplification of division involving variables.

---

## Key Formulas

### Law of Indices (Negative Exponents)
$$
x^{-n} = \frac{1}{x^n}
$$
**Variables:** $x$ = base, $n$ = exponent.
**When to use:** When you see negative exponents in a fraction.
**Worked example:** $x^{-1} - 1 \rightarrow \frac{1}{x} - 1 = \frac{1-x}{x}$.

### Equating Exponents
$$
\text{If } k^a = k^b, \text{ then } a = b
$$
**Variables:** $k$ = common base, $a, b$ = exponents.
**When to use:** When you have an equality chain (e.g., $2^x = 3^y = 6^{-z}$).
**Worked example:** If $k^{1/x} \times k^{1/y} = k^{-1/z}$, then $\frac{1}{x} + \frac{1}{y} = -\frac{1}{z}$.

---

## Solution Framework

1. **Standardize Bases:** Convert all terms to a common base (e.g., $x^{-1} \rightarrow 1/x$) or a common constant $k$.
2. **Simplify Numerators/Denominators:** Find common denominators to combine terms into a single fraction.
3. **Factorize:** Look for common binomials (like $(x-1)$) to cancel out terms.
4. **Equate Exponents:** If dealing with an equality chain, express all terms as powers of $k$ and use exponent laws to relate the variables.

---

## Shortcut Tricks

* **Trick:** For $2^x = 3^y = 6^{-z}$, the relation is $\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 0$.
* **Why it works:** Because $2 \times 3 = 6$, so $k^{1/x} \times k^{1/y} = k^{-1/z}$.
* **When to use:** Whenever you see a product of two bases equaling the third base in an equality chain.
* **Example:** $2^x = 3^y = 6^{-z} \rightarrow \frac{1}{x} + \frac{1}{y} = -\frac{1}{z}$.

---

## Common Mistakes

* **Mistake:** Simplifying $\frac{1-x}{x-1}$ as $1$.
    * **Fix:** Recognize that $(1-x) = -(x-1)$, so the result is $-1$.
* **Mistake:** Forgetting the negative sign in $6^{-z}$ when equating exponents.
    * **Fix:** Always write out the constant $k$ substitution explicitly.
* **Mistake:** Multiplying before dividing in BODMAS expressions.
    * **Fix:** Strictly follow the order: Division, then Multiplication.

---

## Worked Example (Step-by-Step)

**Question:** If $2^x = 3^y = 6^{-z}$, find the value of $(\frac{1}{x} + \frac{1}{y} + \frac{1}{z})$.

**Solution:**
1. **Set to constant:** Let $2^x = 3^y = 6^{-z} = k$.
2. **Isolate bases:** $2 = k^{1/x}$, $3 = k^{1/y}$, $6 = k^{-1/z}$.
3. **Use relationship:** Since $2 \times 3 = 6$, substitute the $k$ values: $k^{1/x} \times k^{1/y} = k^{-1/z}$.
4. **Apply exponent law:** $k^{(1/x + 1/y)} = k^{-1/z}$.
5. **Equate:** $\frac{1}{x} + \frac{1}{y} = -\frac{1}{z} \Rightarrow \frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 0$.

**Answer:** $0$

---

## Similar Patterns
* **Surds and Indices:** This pattern is a subset of Surds and Indices; distinguish it by the presence of algebraic variables ($x, y, z$) rather than just numerical bases.

---

## Revision Summary
* **Key formula:** $x^{-n} = \frac{1}{x^n}$ and $a^m \cdot a^n = a^{m+n}$.
* **Spot it by:** Negative exponents or equality chains ($a^x = b^y = c^z$).
* **First move:** Set the entire expression equal to a constant $k$.
* **Fastest method:** Use the shortcut $\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 0$ for product-based chains.
* **Biggest trap:** Treating $(1-x)/(x-1)$ as $1$ instead of $-1$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **BODMAS:** The order of operations (Brackets, Orders, Division, Multiplication, Addition, Subtraction).
* **Exponent Laws:** $a^m \times a^n = a^{m+n}$ and $(a^m)^n = a^{mn}$.

### Formulas You Must Know First
$$
a^m \times a^n = a^{m+n}
$$
**What it means:** When multiplying terms with the same base, add the exponents.
**Example:** $2^3 \times 2^2 = 2^5 = 32$.

### Terms Used In This Pattern
* **Quotient:** The result of a division.
* **Base:** The number being raised to a power.