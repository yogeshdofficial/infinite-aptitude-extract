# Unit Digit and Remainder Patterns

## Overview
These questions ask for the last digit of a large product/power or the remainder of a large number when divided by a specific divisor. The central idea is to use **cyclicity** for powers and **digit summation** or **factor analysis** for products and divisibility.

---

## Recognition Clues
* **"Unit's digit"**: The question explicitly asks for the last digit of a product or power.
* **"Remainder"**: The question asks for the remainder when a large number or expression is divided by a small integer (like 8 or 9).
* **Large Exponents**: Bases like $(2467)^{153}$ or $(264)^{102}$ indicate a need for cyclicity.
* **Consecutive Sequences**: Numbers written side-by-side (e.g., 123...29) or products of consecutive numbers (e.g., 81 to 89).

---

## Key Formulas

### [Cyclicity of Powers]
$$
\text{Unit digit of } a^n = \text{Unit digit of } a^{n \pmod 4}
$$
*(Note: If $n \pmod 4 = 0$, use power 4).*

**Variables:**
- $a$ = the base number
- $n$ = the exponent

**When to use:** When finding the unit digit of a number raised to a large power.

**Worked example:** For $(2467)^{153}$, take base 7 and exponent $153 \pmod 4 = 1$. Result: $7^1 = 7$.

### [Divisibility by 9]
$$
\text{Remainder of } N \div 9 = \text{Remainder of } (\text{Sum of digits of } N) \div 9
$$

**Variables:**
- $N$ = the large number formed by concatenating digits.

**When to use:** When a long string of numbers is divided by 9.

---

## Solution Framework

1. **Isolate the Unit Digit:** Ignore all digits except the unit digit of the base.
2. **Check for Factors:** If it's a product, check if 2 and 5 are present (result is 0).
3. **Apply Cyclicity:** For powers, divide the exponent by 4 and use the remainder as the new exponent.
4. **Sum Digits:** For divisibility by 9, sum all individual digits of the sequence.
5. **Final Reduction:** Perform the final operation (addition/multiplication) on the simplified digits to find the result.

---

## Shortcut Tricks

* **Trick:** If a product contains 2 and 5, the unit digit is always 0.
* **Why it works:** $2 \times 5 = 10$, and any multiple of 10 ends in 0.
* **When to use:** Products of consecutive numbers or large sets of numbers.
* **Example:** $81 \times 82 \times \dots \times 89$ contains 82 and 85 (or 82 and 85), so unit digit is 0.

* **Trick:** Powers of 4: Odd power ends in 4, Even power ends in 6.
* **Example:** $(264)^{102}$ (even) $\rightarrow$ 6; $(264)^{103}$ (odd) $\rightarrow$ 4. Sum = 10 $\rightarrow$ unit digit 0.

---

## Common Mistakes

* **Mistake:** Using the full number instead of just the unit digit.
* **Fix:** Always truncate the base to its last digit immediately.
* **Mistake:** Using 0 as the exponent when $n$ is divisible by 4.
* **Fix:** If $n \pmod 4 = 0$, use 4 as the exponent.
* **Mistake:** Forgetting to sum digits of the sum (e.g., 165 $\rightarrow$ 1+6+5 = 12 $\rightarrow$ 1+2 = 3).
* **Fix:** Keep summing until you get a single digit.

---

## Worked Example (Step-by-Step)

**Question:** Find the unit's digit in $(2467)^{153} \times (341)^{72}$.

**Solution:**
1. **Isolate:** Focus on $7^{153} \times 1^{72}$.
2. **Cyclicity:** $153 \div 4$ leaves remainder 1. So, $7^1 = 7$.
3. **Power of 1:** $1$ raised to any power is $1$.
4. **Multiply:** $7 \times 1 = 7$.

**Answer:** 7

---

## Similar Patterns
* **Divisibility Rules:** Often confused with unit digit problems; check if the question asks for the *last digit* (Unit Digit) or *divisibility* (Remainder).

---

## Revision Summary
* **Key formula:** $a^n \rightarrow a^{n \pmod 4}$.
* **Spot it by:** Large powers or long sequences of numbers.
* **First move:** Reduce bases to their unit digits.
* **Fastest method:** Use cyclicity (4) for powers; sum digits for 9.
* **Biggest trap:** Using 0 as an exponent for powers divisible by 4.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Cyclicity** — The repeating pattern of unit digits when a number is raised to increasing powers.
* **Sum of Digits Rule** — A number is congruent to the sum of its digits modulo 9.

### Terms Used In This Pattern
* **Unit's Digit** — The rightmost digit of a number.
* **Base** — The number being raised to a power.
* **Exponent** — The power to which a base is raised.