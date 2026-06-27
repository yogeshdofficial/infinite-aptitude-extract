# Odd One Out

## Overview
This is a classification task where you are given a sequence of numbers and must identify the single value that violates a common property shared by all others. The central idea is to test the sequence against fundamental number properties (parity, primality, squares, cubes, or divisibility) until the outlier is found.

---

## Recognition Clues
* **Keywords:** "Find the odd one out," "Find the wrong number," "Insert the missing number."
* **Given:** A list of 6–10 numbers.
* **Asked:** Identify the number that does not follow the pattern or property of the rest.
* **Visual cues:** Look for a mix of even/odd, a sudden non-square in a list of squares, or a number not divisible by a common factor.

---

## Key Formulas
There are no complex algebraic formulas for this pattern; it relies on identifying properties of numbers.

### [Property Testing]
$$
\text{Property}(n) \in \{ \text{Prime, Even, Odd, Square, Cube, Multiple of } k \}
$$
**When to use:** Apply this to each number in the set to see which one fails the test.

**Worked example:** For the set $\{16, 25, 36, 72, 144\}$, test for "Perfect Square":
- $16=4^2, 25=5^2, 36=6^2, 144=12^2$.
- $72$ is not a perfect square. Therefore, $72$ is the odd one out.

---

## Solution Framework
1. **Scan for obvious properties:** Check if all numbers are even/odd or prime/composite.
2. **Check for powers:** See if most numbers are perfect squares ($n^2$) or cubes ($n^3$).
3. **Check for divisibility:** If no other pattern fits, check if all numbers are multiples of a small prime (3, 5, or 7).
4. **Test for arithmetic progression:** If the numbers are close, check the difference between consecutive terms to see if one breaks the constant gap.
5. **Verify the outlier:** Ensure the identified number is the *only* one that violates the property.

---

## Shortcut Tricks
* **Trick:** Check the last digit first.
* **Why it works:** Divisibility rules for 2 (even/odd), 5 (ends in 0 or 5), and 10 are visible instantly.
* **When to use:** When the list contains large numbers or a mix of even/odd values.
* **Example:** In $\{10, 25, 45, 54, 60\}$, $54$ ends in 4, while all others end in 0 or 5. $54$ is the outlier.

---

## Common Mistakes
* **Mistake:** Assuming the sequence must be an arithmetic progression.
    * **Fix:** Only check for progression if property-based tests (prime, square, etc.) fail.
* **Mistake:** Misidentifying 1 as a prime number.
    * **Fix:** Remember that prime numbers start from 2.
* **Mistake:** Stopping at the first number that looks "different."
    * **Fix:** Always verify that the *other* numbers truly share a common property.

---

## Worked Example (Step-by-Step)
**Question:** 41, 43, 47, 53, 61, 71, 73, 81

**Solution:**
1. **Scan:** These are all odd numbers, so parity doesn't help.
2. **Check Primes:** 41, 43, 47, 53, 61, 71, 73 are all prime (no divisors other than 1 and themselves).
3. **Test Outlier:** Check 81. $81 = 9 \times 9$ or $3 \times 27$. It is composite.
4. **Conclusion:** 81 is the odd one out because it is the only composite number in the set.

**Answer:** 81

---

## Similar Patterns
**Number Series:** In "Number Series," you must find the *next* number in the sequence, whereas in "Odd One Out," you must find the *wrong* number already present in the list.

---

## Revision Summary
* **Key formula:** Test for Prime, Square, Cube, or Divisibility.
* **Spot it by:** Looking for one number that breaks the property of the group.
* **First move:** Check parity (even/odd) or primality.
* **Fastest method:** Use divisibility rules (last digit) for quick elimination.
* **Biggest trap:** Assuming an arithmetic progression when a simple property (like squares) is the actual rule.

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Number** — A number greater than 1 with only two factors: 1 and itself.
* **Composite Number** — A number with more than two factors.
* **Perfect Square** — A number resulting from multiplying an integer by itself ($1, 4, 9, 16, 25...$).
* **Perfect Cube** — A number resulting from multiplying an integer by itself three times ($1, 8, 27, 64, 125...$).
* **Parity** — The property of being even (divisible by 2) or odd (not divisible by 2).

### Formulas You Must Know First
No prerequisite formulas — all logic is based on number properties.

### Terms Used In This Pattern
* **Outlier** — The specific element in a set that does not share the common property of the others.
* **Sequence** — An ordered list of numbers.