# Digit Problems

## Overview
These questions involve finding a number based on relationships between its digits (sum, difference, or reversal). The central idea is to represent a number algebraically using its place values (e.g., $10x + y$ for a two-digit number) to create solvable equations.

---

## Recognition Clues
* **Keywords:** "two-digit number," "three-digit number," "sum of the digits," "digits are interchanged," "unit's place," "ten's place."
* **Given:** Relationships between digits (e.g., "unit's digit is 3 more than ten's digit") or operations on the number (e.g., "subtracting 63 reverses the digits").
* **Asked:** The original number.

---

## Key Formulas

### [Two-Digit Number Representation]
$$
\text{Number} = 10x + y
$$
**Variables:**
- $x$ = digit in the ten's place
- $y$ = digit in the unit's place

**When to use:** Whenever the problem mentions a two-digit number and operations on its digits.

**Worked example:** If ten's digit $x=3$ and unit's digit $y=6$, the number is $10(3) + 6 = 36$.

### [Three-Digit Number Representation]
$$
\text{Number} = 100x + 10y + z
$$
**Variables:**
- $x$ = digit in the hundred's place
- $y$ = digit in the ten's place
- $z$ = digit in the unit's place

**When to use:** Whenever the problem involves a three-digit number.

**Worked example:** If $x=2, y=6, z=8$, the number is $100(2) + 10(6) + 8 = 268$.

---

## Solution Framework
1. **Define variables:** Assign $x, y, z$ to the digits based on the given relationships.
2. **Express the number:** Write the number in its expanded form ($10x + y$ or $100x + 10y + z$).
3. **Express the condition:** Write the "interchanged" or "modified" number using the same variables.
4. **Form the equation:** Set up the equation based on the problem statement (e.g., $\text{Original} - 63 = \text{Reversed}$).
5. **Solve for digits:** Solve the linear equation for $x, y,$ or $z$ and reconstruct the number.

---

## Shortcut Tricks
* **Trick:** For two-digit numbers, the difference between the original number and the reversed number is always $9 \times (\text{difference between digits})$.
* **Why it works:** $(10x + y) - (10y + x) = 9x - 9y = 9(x - y)$.
* **When to use:** When the problem gives the difference between the original and reversed numbers.
* **Example:** If the difference is 45, then $9(x-y) = 45 \implies x-y = 5$.

---

## Common Mistakes
* **Mistake:** Representing a two-digit number as $x + y$ instead of $10x + y$.
    * **Why it happens:** Forgetting place value.
    * **Fix:** Always write $10 \times (\text{ten's digit}) + (\text{unit's digit})$.
* **Mistake:** Assuming a unique solution exists when equations are dependent.
    * **Why it happens:** Not checking if the equations provide enough independent information.
    * **Fix:** If you get $0=0$, the number cannot be determined.

---

## Worked Example (Step-by-Step)

**Question:** A number consists of two digits. The sum of the digits is 9. If 63 is subtracted from the number, its digits are interchanged. Find the number.

**Solution:**
1. **Define:** Let ten's digit be $x$. Unit's digit is $(9-x)$.
2. **Original Number:** $10x + (9-x) = 9x + 9$.
3. **Reversed Number:** $10(9-x) + x = 90 - 10x + x = 90 - 9x$.
4. **Equation:** $(9x + 9) - 63 = 90 - 9x$.
5. **Solve:** $9x - 54 = 90 - 9x \implies 18x = 144 \implies x = 8$.
6. **Result:** Ten's digit is 8, unit's digit is $9-8=1$.

**Answer:** 81.

---

## Similar Patterns
**Algebraic Word Problems:** These are broader; distinguish Digit Problems by the specific mention of "digits," "place value," or "interchanging" positions.

---

## Revision Summary
* **Key formula:** $\text{Number} = 10x + y$.
* **Spot it by:** Mentions of "digits," "interchanging," or "place values."
* **First move:** Assign variables to digits and write the number as $10x + y$.
* **Fastest method:** Use the $9(x-y)$ difference rule for reversal problems.
* **Biggest trap:** Writing the number as $x+y$ instead of $10x+y$.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Place Value** — The value of a digit depends on its position (e.g., in 36, 3 is in the ten's place, so it represents $3 \times 10$).
* **Linear Equations** — Solving $ax + b = cx + d$ by isolating $x$.

### Formulas You Must Know First
* No prerequisite formulas — all formulas needed are introduced above.

### Terms Used In This Pattern
* **Ten's digit** — The digit in the second position from the right.
* **Unit's digit** — The digit in the first position from the right.
* **Interchanged** — Swapping the positions of the digits.