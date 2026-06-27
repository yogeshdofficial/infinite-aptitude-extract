# Basic HCF LCM

## Overview
This pattern involves finding the Highest Common Factor (HCF) or Least Common Multiple (LCM) of numbers, prime-factorized expressions, or fractions. The central idea is to use prime factorization to identify common factors (for HCF) or all unique factors (for LCM) based on their powers.

---

## Recognition Clues
* **Keywords:** "Find the H.C.F.", "Find the L.C.M.", "Reduce to lowest terms".
* **Given:** Sets of integers, expressions in prime power form (e.g., $2^3 \times 3^2$), or fractions.
* **Asked:** The greatest divisor (HCF) or the smallest common multiple (LCM).

---

## Key Formulas

### [HCF of Prime Factors]
$$
\text{HCF} = \text{Product of lowest powers of common prime factors}
$$
**Variables:** Common prime factors are those present in *every* expression.
**When to use:** When numbers are given as products of prime powers.
**Example:** For $2^3 \times 3^2$ and $2^2 \times 3^5$, common primes are 2 and 3. Lowest powers are $2^2$ and $3^2$. HCF = $2^2 \times 3^2 = 36$.

### [LCM of Prime Factors]
$$
\text{LCM} = \text{Product of highest powers of all prime factors}
$$
**Variables:** All unique prime factors present in *any* expression.
**When to use:** When numbers are given as products of prime powers.
**Example:** For $2^2 \times 3^3$ and $2^3 \times 3^2$, unique primes are 2 and 3. Highest powers are $2^3$ and $3^3$. LCM = $2^3 \times 3^3 = 216$.

---

## Solution Framework
1. **Factorize:** Express all numbers as products of prime powers.
2. **Identify Primes:** List all prime factors involved.
3. **Select Powers:** For HCF, pick the *lowest* power of *common* primes; for LCM, pick the *highest* power of *all* primes.
4. **Multiply:** Calculate the product of the selected powers to get the final result.
5. **Division Method (for large integers):** If numbers are large, use the Euclidean algorithm (repeated division) to find the HCF.

---

## Shortcut Tricks
* **Trick:** For HCF of two numbers, the HCF must be a factor of their difference.
* **Why it works:** If $d$ divides $A$ and $B$, it must divide $(A-B)$.
* **When to use:** When you have two large numbers and need a quick HCF.
* **Example:** HCF of 87 and 145. Difference = $145 - 87 = 58$. Factors of 58 are 1, 2, 29, 58. 29 divides both. HCF = 29.

---

## Common Mistakes
* **Mistake:** Including non-common factors in HCF. **Fix:** Only include primes present in *every* number.
* **Mistake:** Using the highest power for HCF. **Fix:** HCF uses the *lowest* power.
* **Mistake:** Forgetting to include a prime factor in LCM. **Fix:** Ensure every unique prime found in any number is included in the LCM.

---

## Worked Example (Step-by-Step)

**Question:** Find the H.C.F. of 513, 1134 and 1215.

**Solution:**
1. **Step 1 (Division Method):** Divide 1134 by 513. $1134 = 513 \times 2 + 108$.
2. **Step 2:** Divide 513 by 108. $513 = 108 \times 4 + 81$.
3. **Step 3:** Divide 108 by 81. $108 = 81 \times 1 + 27$.
4. **Step 4:** Divide 81 by 27. $81 = 27 \times 3 + 0$. HCF of 513 and 1134 is 27.
5. **Step 5:** Check 1215 with 27. $1215 \div 27 = 45$ (remainder 0).
**Answer:** 27.

---

## Similar Patterns
* **Fraction HCF/LCM:** Use the formula: $\text{HCF} = \frac{\text{HCF of Numerators}}{\text{LCM of Denominators}}$.
* **Decimal HCF/LCM:** Convert to integers by multiplying by powers of 10 (e.g., 0.63, 1.05 $\rightarrow$ 63, 105), find HCF/LCM, then place the decimal back.

---

## Revision Summary
* **Key formula:** HCF = lowest common powers; LCM = highest all powers.
* **Spot it by:** "HCF" or "LCM" keywords in the question.
* **First move:** Prime factorize the numbers.
* **Fastest method:** Use the difference trick for HCF of two numbers.
* **Biggest trap:** Confusing the power rules (lowest for HCF, highest for LCM).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Number** — A number greater than 1 with only two factors: 1 and itself.
* **Prime Factorization** — Breaking a number into a product of prime numbers (e.g., $12 = 2^2 \times 3^1$).

### Terms Used In This Pattern
* **Factor** — A number that divides another exactly.
* **Multiple** — A number that is the product of a given number and an integer.
* **Co-primes** — Two numbers whose HCF is 1.