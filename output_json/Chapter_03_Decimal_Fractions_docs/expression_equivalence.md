# Expression Equivalence

## Overview
This pattern involves identifying the relationship between two mathematical expressions by comparing their structure or decimal properties. The central idea is to manipulate the given equation to isolate variables or match the decimal precision of the target expression.

---

## Recognition Clues
* **Keywords:** "is the same as", "value of", "equivalent to".
* **Given:** A complex equation with variables ($A, B, C...$) or a product of decimal numbers.
* **Asked:** The value of a new expression or identifying an equivalent product/fraction.
* **Visual:** Look for decimal numbers with multiple digits or fractions involving variables in the denominator.

---

## Key Formulas

### Place Value Expansion
$$
\text{Number} = \sum (\text{Digit} \times \text{Place Value})
$$
**Variables:**
- $\text{Digit}$ = the numerical value at a specific position.
- $\text{Place Value}$ = the power of 10 corresponding to that position (e.g., $10, 1, 0.1, 0.01$).

**When to use:** When an equation equates a decimal number to a sum of variables (e.g., $4A + \frac{7}{B} + 2C...$).

**Worked example:** $47.25 = 4(10) + 7(1) + 2(0.1) + 5(0.01)$. If $4A = 40$, then $A=10$.

### Decimal Place Equivalence
$$
\text{Net Shift} = (\sum \text{Decimal Places}_{\text{Numerator}}) - (\sum \text{Decimal Places}_{\text{Denominator}})
$$
**Variables:**
- $\text{Decimal Places}$ = count of digits to the right of the decimal point.

**When to use:** To check if two fractions or products are equivalent without calculating the full value.

**Worked example:** For $\frac{5.34 \times 3.2}{3.4}$, Numerator places = $2+1=3$, Denominator = $1$. Net shift = $3-1=2$.

---

## Solution Framework

**Step 1: Analyze the structure** — Determine if the question requires variable extraction (place value) or decimal place counting.
**Step 2: Expand or Count** — If variables are present, expand the decimal into its place value components; if products/fractions are present, count the total decimal places.
**Step 3: Match/Compare** — Align the components of the given expression with the target expression or compare the net decimal shift.
**Step 4: Solve/Verify** — Calculate the final value by substituting the extracted variables or selecting the option with the matching net shift.

---

## Shortcut Tricks

* **Trick:** Count decimal places only.
* **Why it works:** The product of digits remains constant; only the decimal point position changes based on the total count of decimal places.
* **When to use:** When asked which expression is "the same as" a given product or fraction.
* **Example:** $54.327 \times 357.2 \times 0.0057$ has $3+1+4 = 8$ places. Any equivalent option must also have exactly 8 decimal places.

---

## Common Mistakes

* **Mistake:** Miscounting decimal places (e.g., ignoring trailing zeros).
    * **Why it happens:** Rushing the count.
    * **Fix:** Write the number of decimal places for each factor clearly below the expression.
* **Mistake:** Confusing $0.1$ (tenths) with $0.01$ (hundredths).
    * **Why it happens:** Misalignment of place values.
    * **Fix:** Always write the decimal expansion vertically to align place values.
* **Mistake:** Forgetting to subtract denominator decimal places.
    * **Why it happens:** Treating fractions like simple products.
    * **Fix:** Always calculate the "Net Shift" for fractions.

---

## Worked Example (Step-by-Step)

**Question:** If $47.2506 = 4A + \frac{7}{B} + 2C + \frac{5}{D} + 6E$, find $5A + 3B + 6C + D + 3E$.

**Solution:**
1. **Expand:** $47.2506 = 40 + 7 + 0.2 + 0.05 + 0.0006$.
2. **Match:** $4(10) + \frac{7}{1} + 2(0.1) + \frac{5}{100} + 6(0.0001)$.
3. **Extract:** $A=10, B=1, C=0.1, D=100, E=0.0001$.
4. **Substitute:** $5(10) + 3(1) + 6(0.1) + 100 + 3(0.0001) = 50 + 3 + 0.6 + 100 + 0.0003$.
5. **Sum:** $153.6003$.

**Answer:** $153.6003$

---

## Similar Patterns
* **Algebraic Substitution:** Distinguished by the presence of algebraic identities (e.g., $a^2-b^2$) rather than place-value decimal expansion.

---

## Revision Summary
* **Key formula:** $\text{Net Shift} = \sum \text{Num Decimals} - \sum \text{Denom Decimals}$.
* **Spot it by:** Looking for "is the same as" or variable-based decimal equations.
* **First move:** Expand decimals by place value or count total decimal places.
* **Fastest method:** Use the decimal place count shortcut for equivalence questions.
* **Biggest trap:** Miscounting decimal places in fractions by ignoring the denominator.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Place Value** — The value of a digit based on its position (e.g., in $0.25$, $2$ is in the tenths place, $5$ is in the hundredths).
* **Decimal Fractions** — Fractions where the denominator is a power of $10$.

### Formulas You Must Know First
* **Decimal Multiplication Rule:** The number of decimal places in the product is the sum of the decimal places in the factors.
* **Decimal Division Rule:** The number of decimal places in the quotient is the difference between the decimal places in the dividend and the divisor.

### Terms Used In This Pattern
* **Vulgar Fraction** — A fraction written in the form $\frac{a}{b}$.
* **Net Shift** — The difference in decimal places between the numerator and denominator.