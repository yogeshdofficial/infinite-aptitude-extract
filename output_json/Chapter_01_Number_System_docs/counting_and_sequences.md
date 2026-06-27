# Counting and Sequences

## Overview
This pattern involves solving for unknown variables in digit-based equations or identifying terms in a sequence. The central idea is to break down the problem into place-value components (units, tens, hundreds) or map the sequence to a linear function.

---

## Recognition Clues
* **Keywords:** "maximum value of", "pronounced by", "sum of", "find the value of".
* **Given:** Equations with missing digits (e.g., $5P9$), sequences of numbers, or sum of squares.
* **Asked:** The value of a specific variable, the intersection point of two counting sequences, or the result of a modified series.

---

## Key Formulas

### [Place Value Summation]
$$ \text{Sum} = \sum (\text{Digit} \times 10^n) $$
**Variables:** $n$ = position (0 for units, 1 for tens, etc.).
**When to use:** When solving for missing variables in addition equations (e.g., $5P9 + 3R7 + 2Q8 = 1114$).
**Worked example:** In $5P9 + 3R7 + 2Q8 = 1114$, units place is $9+7+8 = 24$. Carry $2$ to tens place: $P+R+Q+2 = 11 \implies P+R+Q = 9$.

### [Sequence Mapping]
$$ a_n = a_1 + (n-1)d $$
**Variables:** $a_n$ = $n^{th}$ term, $a_1$ = first term, $d$ = common difference.
**When to use:** To find the $n^{th}$ term of a sequence or identify when two counters meet.
**Worked example:** A counts odd numbers: $1, 3, 5...$ where $a_n = 2n-1$. For $n=11$, $a_{11} = 2(11)-1 = 21$.

---

## Solution Framework

1. **Deconstruct by Place Value:** If given an equation, isolate units, tens, and hundreds columns to create simple linear equations.
2. **Account for Carries:** Always check the sum of the previous column to see if a carry-over affects the current column.
3. **Map Sequences:** If two people are counting, write the general term formula for each and equate them to find the intersection.
4. **Factorize Series:** If given a sum of squares/cubes, factor out common constants to match the provided known sum.
5. **Solve for Variables:** Use substitution or elimination to find the missing values.

---

## Shortcut Tricks

* **Trick:** To maximize a variable in a sum, set all other unknown variables to $0$.
* **Why it works:** Since the sum is fixed, reducing other variables leaves the maximum "room" for the target variable.
* **When to use:** When asked for the "maximum value" of a digit in an equation.
* **Example:** In $P+R+Q=9$, to maximize $Q$, set $P=0, R=0 \implies Q=9$.

---

## Common Mistakes

* **Mistake:** Forgetting the carry-over from the units place to the tens place.
    * **Why it happens:** Focusing only on the digits shown in the column.
    * **Fix:** Always calculate the right-most column first to determine the carry.
* **Mistake:** Failing to square the factor when pulling it out of a sum of squares.
    * **Why it happens:** Treating $(2n)^2$ as $2n^2$ instead of $4n^2$.
    * **Fix:** Remember $(ax)^2 = a^2x^2$.

---

## Worked Example (Step-by-Step)

**Question:** Given $1^2 + 2^2 + \dots + 10^2 = 385$, find $2^2 + 4^2 + \dots + 20^2$.

**Solution:**
1. **Identify the pattern:** The target series is $2^2, 4^2, 6^2, \dots, 20^2$.
2. **Factor out the common term:** Each term is $(2 \times 1)^2, (2 \times 2)^2, \dots, (2 \times 10)^2$.
3. **Apply the square:** This becomes $2^2(1^2) + 2^2(2^2) + \dots + 2^2(10^2)$.
4. **Simplify:** Factor out $2^2 = 4$. The expression is $4 \times (1^2 + 2^2 + \dots + 10^2)$.
5. **Substitute:** $4 \times 385 = 1540$.

**Answer:** 1540

---

## Revision Summary

* **Key formula:** $a_n = a_1 + (n-1)d$ for sequences; place value for digits.
* **Spot it by:** Missing variables in equations or series summation.
* **First move:** Check for carry-overs in equations or factor out constants in series.
* **Fastest method:** Use the "set to zero" trick for maximization problems.
* **Biggest trap:** Forgetting to square the common factor in series problems.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Place Value** — The value of a digit depends on its position (e.g., in $5P9$, $P$ is in the tens place, so its value is $10P$).
* **Arithmetic Progression (AP)** — A sequence where the difference between consecutive terms is constant.

### Formulas You Must Know First
* **Sum of two variables:** $a+b=S$ and $a-b=D \implies a = \frac{S+D}{2}, b = \frac{S-D}{2}$.

### Terms Used In This Pattern
* **Numeral** — A symbol or group of symbols representing a number.
* **Carry** — A digit transferred from one column to the next during addition.