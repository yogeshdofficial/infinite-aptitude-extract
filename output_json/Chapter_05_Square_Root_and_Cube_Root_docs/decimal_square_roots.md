# Decimal Square Roots

## Overview
These questions require finding the square root of numbers containing decimals or fractions. The central idea is to convert the decimal into a fraction with a perfect square denominator (like $100, 10000$) to simplify the calculation.

---

## Recognition Clues
* **Visual:** Look for numbers with decimal points (e.g., $0.0009$) or fractions of decimals (e.g., $\frac{0.289}{0.00121}$).
* **Given:** A decimal number or a fraction involving decimals.
* **Asked:** The square root ($\sqrt{x}$) of the given value.
* **Clue:** If the number of decimal places is odd, you must balance them (e.g., $0.9 \rightarrow 0.90$) to perform long division.

---

## Key Formulas

### Fraction Square Root Property
$$
\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}
$$

**Variables:**
- $a$ = numerator
- $b$ = denominator (must be a perfect square)

**When to use:** When the number is a decimal, convert it to a fraction first, then apply this property.

**Worked example:** For $\sqrt{0.0009}$, write as $\sqrt{\frac{9}{10000}}$. Apply formula: $\frac{\sqrt{9}}{\sqrt{10000}} = \frac{3}{100} = 0.03$.

---

## Solution Framework

1. **Balance Decimals:** Add zeros to the numerator or denominator so both have an even number of decimal places.
2. **Convert to Fraction:** Remove the decimal point by writing the number over the appropriate power of 10 (e.g., $0.25 = \frac{25}{100}$).
3. **Simplify Fraction:** Reduce the fraction if possible to make the numerator and denominator perfect squares.
4. **Extract Roots:** Take the square root of the numerator and denominator separately.
5. **Convert Back:** Divide the resulting numerator by the denominator to return to decimal form.

---

## Shortcut Tricks

* **Trick:** Count the decimal places in the original number and divide by 2.
* **Why it works:** Since $\sqrt{10^{-2n}} = 10^{-n}$, the number of decimal places in the square root is exactly half the number of decimal places in the original perfect square.
* **When to use:** When the number is a perfect square (e.g., $\sqrt{0.0009}$ has 4 places, so the answer must have $4/2 = 2$ places).
* **Example:** $\sqrt{0.0009} \rightarrow 4$ places $\rightarrow$ answer has 2 places $\rightarrow 0.03$.

---

## Common Mistakes

* **Mistake:** Miscounting decimal places (e.g., thinking $\sqrt{0.9} = 0.3$).
* **Why it happens:** Forgetting that $0.9$ is not a perfect square; it must be treated as $0.90$.
* **Fix:** Always ensure the number of decimal places is even before taking the root.
* **Mistake:** Taking the root of the whole number and decimal part separately.
* **Why it happens:** Treating the decimal point as a separator rather than part of the value.
* **Fix:** Always convert to a fraction first.

---

## Worked Example (Step-by-Step)

**Question:** Find the value of $\sqrt{\frac{0.289}{0.00121}}$.

**Solution:**
1. **Balance Decimals:** The numerator has 3 places, denominator has 5. Add two zeros to the numerator: $\frac{0.28900}{0.00121}$.
2. **Convert to Fraction:** Remove decimals: $\frac{28900}{121}$.
3. **Extract Roots:** $\sqrt{\frac{28900}{121}} = \frac{\sqrt{28900}}{\sqrt{121}}$.
4. **Calculate:** $\frac{170}{11}$.

**Answer:** $\frac{170}{11}$ (or $15.45...$)

---

## Similar Patterns

**Integer Square Roots:** Distinguished by the absence of decimal points; use prime factorization or long division directly without balancing decimal places.

---

## Revision Summary

* **Key formula:** $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$.
* **Spot it by:** Decimal points inside a square root symbol.
* **First move:** Convert the decimal to a fraction with an even number of decimal places.
* **Fastest method:** Count decimal places and divide by 2 for perfect squares.
* **Biggest trap:** Assuming $\sqrt{0.x} = \sqrt{x}/10$ (only true if $x$ is a perfect square).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Perfect Squares** — Numbers that are the result of squaring an integer (e.g., $1, 4, 9, 16, 25, 100, 121, 289$).
* **Powers of 10** — Understanding that $10^2=100, 10^4=10000$, etc.

### Formulas You Must Know First
$$
\sqrt{a \times b} = \sqrt{a} \times \sqrt{b}
$$
**What it means:** You can split the square root of a product into the product of individual square roots.

### Terms Used In This Pattern
* **Recurring Decimal** — A decimal that repeats infinitely (e.g., $0.\bar{1} = 1/9$).
* **Improper Fraction** — A fraction where the numerator is greater than the denominator.