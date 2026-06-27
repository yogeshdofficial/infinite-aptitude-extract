# Recurring Decimals

## Overview
This pattern involves converting decimals with repeating digits (indicated by a bar, e.g., $0.\overline{37}$) into simple fractions (vulgar fractions). The central idea is to use the number of repeating digits to determine the number of 9s in the denominator, and the number of non-repeating digits to determine the number of 0s.

---

## Recognition Clues
* **Visual:** Look for a bar over one or more digits after the decimal point (e.g., $0.\overline{12}$, $0.1\overline{7}$).
* **Phrasing:** Questions explicitly ask to "Express as vulgar fractions" or "Convert to $p/q$ form."
* **Given:** A decimal number with a repeating sequence.
* **Asked:** The equivalent fraction in simplest form.

---

## Key Formulas

### Pure Recurring Decimal
$$
0.\overline{x} = \frac{x}{9...9} \text{ (n nines)}
$$
**Variables:**
- $x$ = the repeating block of digits.
- $n$ = the number of digits in the repeating block.

**When to use:** When every digit after the decimal point repeats.
**Worked example:** For $0.\overline{053}$, $x=053$ (or $53$) and $n=3$. Result: $\frac{53}{999}$.

### Mixed Recurring Decimal
$$
0.a\overline{b} = \frac{(\text{all digits}) - (\text{non-repeating part})}{9...90...0}
$$
**Variables:**
- $9...9$ = as many nines as there are repeating digits.
- $0...0$ = as many zeros as there are non-repeating digits after the decimal.

**When to use:** When some digits after the decimal do not repeat.
**Worked example:** For $0.1\overline{7}$, all digits = $17$, non-repeating = $1$. Result: $\frac{17-1}{90} = \frac{16}{90} = \frac{8}{45}$.

---

## Solution Framework

1. **Separate the Integer:** If the number is $X.\overline{Y}$, write it as $X + 0.\overline{Y}$ to simplify calculation.
2. **Identify Repeating/Non-repeating:** Count how many digits repeat (nines) and how many non-repeating digits follow the decimal (zeros).
3. **Form the Numerator:** Subtract the non-repeating part from the total number formed by all digits after the decimal.
4. **Form the Denominator:** Write the nines followed by the zeros.
5. **Simplify:** Reduce the resulting fraction to its lowest terms by dividing by common factors.

---

## Shortcut Tricks
* **Trick:** For $0.\overline{9}$, the value is exactly $1$.
* **Why it works:** $\frac{9}{9} = 1$.
* **When to use:** When you see a repeating 9 at the end of a decimal sequence.
* **Example:** $0.4\overline{9} = 0.5$.

---

## Common Mistakes
* **Mistake:** Using 100 or 1000 in the denominator.
    * **Why it happens:** Confusing recurring decimals with terminating decimals (e.g., $0.25 = 25/100$).
    * **Fix:** Always use 9s for recurring parts.
* **Mistake:** Including the integer part in the numerator subtraction.
    * **Why it happens:** Misapplying the mixed decimal formula.
    * **Fix:** Only use digits after the decimal point for the numerator calculation.

---

## Worked Example (Step-by-Step)

**Question:** Express $2.5\overline{36}$ as a vulgar fraction.

**Solution:**
1. **Separate:** $2 + 0.5\overline{36}$.
2. **Identify:** Repeating digits = $36$ (two 9s). Non-repeating digits after decimal = $5$ (one 0).
3. **Numerator:** Total digits after decimal is $536$. Non-repeating part is $5$. Numerator = $536 - 5 = 531$.
4. **Denominator:** Two 9s and one 0 = $990$.
5. **Combine:** $2 + \frac{531}{990}$.
6. **Simplify:** Divide $531$ and $990$ by $9$: $\frac{59}{110}$.
7. **Final:** $2\frac{59}{110}$ or $\frac{279}{110}$.

**Answer:** $\frac{279}{110}$

---

## Similar Patterns
* **Terminating Decimals:** These do not have a bar and are converted by placing 1 followed by zeros in the denominator (e.g., $0.25 = 25/100$).

---

## Revision Summary
* **Key formula:** $\frac{\text{Total} - \text{Non-repeating}}{9s \text{ and } 0s}$.
* **Spot it by:** The bar over repeating digits.
* **First move:** Separate the integer part from the decimal part.
* **Fastest method:** Count repeating digits for 9s, non-repeating for 0s.
* **Biggest trap:** Using 10s instead of 9s in the denominator.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Vulgar Fraction** — A fraction where both numerator and denominator are integers.
* **Simplest Form** — A fraction where the numerator and denominator share no common factors other than 1.

### Formulas You Must Know First
* **Division by common factors:** $\frac{a \cdot k}{b \cdot k} = \frac{a}{b}$.
    * **Example:** $\frac{12}{99} = \frac{12 \div 3}{99 \div 3} = \frac{4}{33}$.

### Terms Used In This Pattern
* **Pure Recurring Decimal** — All digits after the decimal point repeat.
* **Mixed Recurring Decimal** — Only some digits after the decimal point repeat.