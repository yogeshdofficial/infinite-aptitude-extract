# Fraction Conversion

## Overview
This pattern involves converting between decimal numbers and fractions, or manipulating decimal expressions using powers of 10. The central idea is to treat the decimal point as a shift in the power of 10, allowing you to move between fractional and decimal forms by counting decimal places or zeros.

---

## Recognition Clues
* **Keywords:** "Convert into vulgar fractions," "decimal form," "place value of," "what decimal of."
* **Given:** A decimal number (e.g., $0.75$), a fraction (e.g., $\frac{42}{10000}$), or a known reciprocal (e.g., $\frac{1}{3.718} = .2689$).
* **Asked:** The equivalent form (fraction to decimal or vice versa), the sum of a simplified fraction's components, or the value of a related expression.

---

## Key Formulas

### [Decimal to Fraction]
$$
\text{Decimal} = \frac{\text{Number without decimal}}{10^n}
$$
**Variables:**
- $n$ = number of digits after the decimal point.

**When to use:** Converting any terminating decimal to a fraction.
**Worked example:** For $0.75$, $n=2$. So, $\frac{75}{100} = \frac{3}{4}$.

### [Fraction to Decimal]
$$
\frac{x}{10^n} = x \times 10^{-n}
$$
**Variables:**
- $x$ = numerator
- $n$ = number of zeros in the denominator.

**When to use:** Converting a fraction with a power-of-10 denominator to a decimal.
**Worked example:** For $\frac{42}{10000}$, $n=4$. Move decimal in $42$ four places left: $0.0042$.

---

## Solution Framework

1. **Identify decimal places/zeros:** Count the digits after the decimal (for fractions) or zeros in the denominator (for decimals).
2. **Shift the decimal:** Move the decimal point to the left (for division by $10^n$) or right (for multiplication by $10^n$).
3. **Simplify:** If converting to a fraction, divide the numerator and denominator by their Greatest Common Divisor (GCD).
4. **Adjust for mixed numbers:** For $A \frac{B}{C}$, treat as $A + \frac{B}{C}$ and convert only the fractional part.

---

## Shortcut Tricks

* **Trick:** To find the value of $\frac{1}{0.000X}$ when $\frac{1}{X}$ is known, count the decimal shift.
* **Why it works:** $\frac{1}{0.000X} = \frac{1}{X \times 10^{-n}} = \frac{10^n}{X} = 10^n \times (\frac{1}{X})$.
* **When to use:** When given a reciprocal value like $\frac{1}{3.718} = .2689$.
* **Example:** $\frac{1}{0.0003718} = 10000 \times \frac{1}{3.718} = 10000 \times 0.2689 = 2689$.

---

## Common Mistakes

* **Miscounting zeros:** Counting the decimal point as a digit or miscounting the number of zeros in $10^n$. **Fix:** Write out the zeros explicitly.
* **Failing to simplify:** Leaving a fraction like $\frac{36}{100}$ instead of reducing to $\frac{9}{25}$. **Fix:** Always check for common factors (2, 5, etc.).
* **Directional error:** Moving the decimal point right when dividing or left when multiplying. **Fix:** Remember: Division makes numbers smaller (left), multiplication makes them larger (right).

---

## Worked Example (Step-by-Step)

**Question:** If $\frac{1}{3.718} = .2689$, find the value of $\frac{1}{.0003718}$.

**Solution:**
1. **Identify the shift:** The denominator $.0003718$ is $3.718$ divided by $10000$.
2. **Rewrite the expression:** $\frac{1}{.0003718} = \frac{1}{3.718 / 10000}$.
3. **Apply reciprocal rule:** This becomes $10000 \times \frac{1}{3.718}$.
4. **Substitute:** $10000 \times 0.2689 = 2689$.

**Answer:** $2689$

---

## Similar Patterns
This pattern is distinct. If you see recurring decimals (e.g., $0.333...$), use the **Recurring Decimal** rules (placing nines in the denominator) instead of the standard power-of-10 method.

---

## Revision Summary
* **Key formula:** $\text{Decimal} = \frac{\text{Number}}{10^n}$.
* **Spot it by:** Looking for decimal-to-fraction conversion or reciprocal shifts.
* **First move:** Count the decimal places or zeros in the denominator.
* **Fastest method:** Use the power-of-10 shift trick for reciprocal questions.
* **Biggest trap:** Forgetting to simplify the final fraction.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Place Value** — The value of a digit based on its position (tenths, hundredths, etc.).
* **GCD (Greatest Common Divisor)** — The largest number that divides two integers without a remainder.
* **Powers of 10** — Understanding that $10^n$ is $1$ followed by $n$ zeros.

### Formulas You Must Know First
$$
\frac{1}{\frac{a}{b}} = \frac{b}{a}
$$
**What it means:** The reciprocal of a fraction is the fraction flipped.
**Example:** $\frac{1}{1/2} = 2$.

### Terms Used In This Pattern
* **Vulgar Fraction** — A common fraction (e.g., $\frac{3}{4}$).
* **Decimal Fraction** — A fraction where the denominator is a power of 10.