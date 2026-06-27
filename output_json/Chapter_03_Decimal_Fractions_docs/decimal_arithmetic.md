# Decimal Arithmetic

## Overview
This pattern involves performing basic arithmetic operations (addition, subtraction, multiplication, division) on numbers containing decimal points. The central idea is to treat decimals as integers by aligning points or counting places, then adjusting the decimal position in the final result.

---

## Recognition Clues
* **Keywords:** "Evaluate," "Find the product," "Find the quotient," or equations with a "?" (unknown variable).
* **Given:** Numbers with varying decimal places (e.g., $5.064$, $.7036$).
* **Asked:** The sum, difference, product, or quotient of these numbers.
* **Visual:** Numbers stacked or presented in a sequence requiring alignment.

---

## Key Formulas

### [Decimal Alignment Rule]
$$
\text{Sum/Difference} = \text{Aligned Column Calculation}
$$
**Variables:**
- $A, B$ = Numbers to be added or subtracted.
**When to use:** Addition or subtraction of decimals.
**Worked example:** For $13 - 5.1967$, write $13$ as $13.0000$ and subtract $5.1967$ to get $7.8033$.

### [Decimal Product Rule]
$$
\text{Total Decimal Places} = \sum (\text{Decimal places in each factor})
$$
**Variables:**
- $n_1, n_2$ = Number of decimal places in factor 1 and factor 2.
**When to use:** Multiplication of decimals.
**Worked example:** $2.68 \times .74$: $2$ places + $2$ places = $4$ total places. $268 \times 74 = 19832 \rightarrow 1.9832$.

---

## Solution Framework

**Step 1: Align/Pad** — For addition/subtraction, align decimal points vertically and add trailing zeros so all numbers have the same number of decimal places.
**Step 2: Calculate** — Perform the operation as if the numbers were integers (ignoring the decimal point).
**Step 3: Place Decimal** — For multiplication/division, count the total decimal places in the factors/dividend and place the decimal point in the result accordingly.
**Step 4: Isolate** — If solving for "?", move known constants to one side using inverse operations ($+$ becomes $-$, $-$ becomes $+$).

---

## Shortcut Tricks

* **Trick:** Multiplying by $10^n$ shifts the decimal point $n$ places to the right.
* **Why it works:** Each power of 10 increases the place value of the digits.
* **When to use:** When the multiplier is $10, 100, 1000,$ etc.
* **Example:** $6.3204 \times 100 = 632.04$ (shift 2 places).

---

## Common Mistakes

* **Mistake:** Misaligning decimal points during addition/subtraction.
    * **Why it happens:** Treating decimals like integers without padding zeros.
    * **Fix:** Always write numbers vertically, aligning the decimal points.
* **Mistake:** Forgetting to count trailing zeros in multiplication.
    * **Why it happens:** Assuming the number of digits in the product is the same as the factors.
    * **Fix:** Always sum the decimal places of all factors first.
* **Mistake:** Incorrectly shifting the decimal point in division.
    * **Why it happens:** Confusing division with multiplication.
    * **Fix:** In division, the result decimal places = (Dividend places - Divisor places).

---

## Worked Example (Step-by-Step)

**Question:** Evaluate $515.15 - 15.51 - 1.51 - 5.11 - 1.11$

**Solution:**
1. **Group:** Use the rule $a - b - c = a - (b + c)$.
2. **Sum:** Add the negative terms: $15.51 + 1.51 + 5.11 + 1.11 = 23.24$.
3. **Subtract:** Perform $515.15 - 23.24$.
4. **Align:** 
   $515.15$
   $- 23.24$
   $= 491.91$

**Answer:** $491.91$

---

## Similar Patterns
* **Fraction Arithmetic:** Distinguish by looking for the "/" symbol; convert fractions to decimals first if the question involves mixed operations.

---

## Revision Summary
* **Key formula:** Total decimal places = Sum of decimal places of factors.
* **Spot it by:** Numbers with varying decimal points and "Evaluate" instructions.
* **First move:** Align decimal points vertically for addition/subtraction.
* **Fastest method:** Multiply as integers, then place the decimal point.
* **Biggest trap:** Miscounting decimal places in the final product.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Place Value** — The value of a digit depending on its position relative to the decimal point.
* **Powers of 10** — Understanding that $10^1=10, 10^2=100$, etc.

### Formulas You Must Know First
* **Algebraic grouping:** $a - (b + c) = a - b - c$.

### Terms Used In This Pattern
* **Dividend** — The number being divided.
* **Divisor** — The number by which the dividend is divided.
* **Vulgar Fraction** — A fraction where both numerator and denominator are integers.