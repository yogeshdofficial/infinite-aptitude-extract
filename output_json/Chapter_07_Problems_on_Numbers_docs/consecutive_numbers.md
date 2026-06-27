# Consecutive Numbers

## Overview
These problems involve sets of numbers that follow each other in a specific sequence (natural, even, or odd). The central idea is to represent all numbers in the set using a single variable $x$ and solve the resulting equation based on the provided sum, product, or average.

---

## Recognition Clues
* **Keywords:** "Consecutive natural numbers," "successive odd integers," "consecutive even numbers."
* **Given:** The sum, product, or average of the set.
* **Asked:** The value of a specific number (e.g., the largest, the smallest, or a count of primes within the set).

---

## Key Formulas

### [Sum of Consecutive Numbers]
$$
\text{Sum} = n \times \text{Average}
$$
**Variables:**
- $n$ = number of terms in the set
- $\text{Average}$ = the middle value of the set

**When to use:** When the average is given, this instantly provides the total sum to set up your equation.

**Worked example:** For 4 consecutive even numbers with an average of 27: $\text{Sum} = 4 \times 27 = 108$.

---

## Solution Framework

1. **Define the variables:** Assign $x$ to the first number; use $x+1$ for natural, $x+2$ for even/odd.
2. **Form the equation:** Write the sum or product of these variables equal to the given value.
3. **Simplify:** Combine all $x$ terms and constants to isolate $x$.
4. **Solve for $x$:** Perform the arithmetic to find the starting value.
5. **Identify the target:** Calculate the specific number requested (e.g., $x+6$ for the largest of four).

---

## Shortcut Tricks

* **Trick:** For an odd number of consecutive terms, the middle term is always $\frac{\text{Sum}}{n}$.
* **Why it works:** In an arithmetic progression, the average is exactly the middle term.
* **When to use it:** When the number of terms is odd (e.g., 3, 5, 7).
* **Example:** Sum of 7 consecutive numbers is 1617. Middle term = $1617 / 7 = 231$. The numbers are $231-3, 231-2, 231-1, 231, 231+1, 231+2, 231+3$.

---

## Common Mistakes

* **Mistake:** Using $x, x+1, x+2$ for consecutive *even/odd* numbers.
    * **Why it happens:** Confusing "consecutive" with "consecutive natural."
    * **Fix:** Always use $x, x+2, x+4$ for even or odd sequences.
* **Mistake:** Miscounting the number of terms in the sum.
    * **Why it happens:** Forgetting to include the first term $x$ when counting.
    * **Fix:** Write out every term explicitly before summing.
* **Mistake:** Forgetting to divide the entire quadratic equation by a common factor.
    * **Why it happens:** Trying to solve large numbers without simplifying first.
    * **Fix:** Divide the whole equation by the coefficient of $x^2$ before factoring.

---

## Worked Example (Step-by-Step)

**Question:** The sum of seven consecutive natural numbers is 1617. How many of these numbers are prime?

**Solution:**
1. **Define:** Let the numbers be $x, x+1, x+2, x+3, x+4, x+5, x+6$.
2. **Equation:** $x + (x+1) + (x+2) + (x+3) + (x+4) + (x+5) + (x+6) = 1617$.
3. **Simplify:** $7x + 21 = 1617$.
4. **Solve:** $7x = 1596 \Rightarrow x = 228$.
5. **Identify:** The numbers are 228, 229, 230, 231, 232, 233, 234.
6. **Check Primes:** 229 and 233 are prime. (231 is $3 \times 77$).
**Answer:** 2 prime numbers.

---

## Similar Patterns

**Algebraic Word Problems:** Distinguish by checking if the problem specifies "consecutive" or "successive." If it doesn't, it is a general algebraic puzzle (like Ex 1-8 in source).

---

## Revision Summary

* **Key formula:** $\text{Sum} = n \times \text{Average}$.
* **Spot it by:** Looking for "consecutive" or "successive" keywords.
* **First move:** Define terms as $x, x+1$ (natural) or $x, x+2$ (even/odd).
* **Fastest method:** Use the middle term trick for odd-numbered sets.
* **Biggest trap:** Using $x+1$ for consecutive even/odd numbers.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Number** — A number greater than 1 divisible only by 1 and itself.
* **Quadratic Equation** — An equation of the form $ax^2 + bx + c = 0$.
* **Arithmetic Progression** — A sequence where the difference between consecutive terms is constant.

### Formulas You Must Know First
* **Quadratic Formula:** $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ (Used to solve $ax^2 + bx + c = 0$).
* **Expansion:** $(x+a)^2 = x^2 + 2ax + a^2$.

### Terms Used In This Pattern
* **Consecutive** — Following each other continuously in the order of natural numbers.
* **Natural Numbers** — Positive integers $\{1, 2, 3, ...\}$.