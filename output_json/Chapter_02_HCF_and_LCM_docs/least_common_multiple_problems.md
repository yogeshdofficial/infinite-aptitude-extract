# Least Common Multiple Problems

## Overview
These questions ask for the smallest number that satisfies specific divisibility conditions. The central idea is to calculate the Least Common Multiple (LCM) of the given divisors and then adjust that value to account for remainders or constraints.

---

## Recognition Clues
* **Keywords:** "Least number," "Smallest number," "Exactly divisible," "Leaves a remainder."
* **Given:** A set of divisors (e.g., 12, 15, 18) and sometimes a remainder or a range (e.g., "five-digit number").
* **Asked:** The specific number that satisfies the divisibility rule.

---

## Key Formulas

### [Standard LCM Adjustment]
$$
\text{Required Number} = \text{LCM}(\text{divisors}) \pm \text{Adjustment}
$$

**Variables:**
- $\text{LCM}$ = The smallest number divisible by all given divisors.
- $\text{Adjustment}$ = The remainder to be added, or the difference to be subtracted.

**When to use:** When the question specifies a remainder or a "number increased/decreased by X."

**Worked example:** For divisors 6, 7, 8, 9, 12 with remainder 1: $\text{LCM} = 504$. $\text{Required} = 504 + 1 = 505$.

---

## Solution Framework

1. **Find the LCM:** Use the division method to find the smallest number divisible by all given divisors.
2. **Handle Remainders:** If the question says "leaves remainder $R$," add $R$ to the LCM.
3. **Handle "Increased/Decreased":** If "increased by $X$," subtract $X$ from the LCM; if "decreased by $X$," add $X$ to the LCM.
4. **Handle Range Constraints:** If looking for a "greatest/smallest $N$-digit number," divide the $N$-digit limit by the LCM, find the remainder, and adjust the limit to make it perfectly divisible.

---

## Shortcut Tricks
* **Trick:** Use the "Highest Power" method for prime factorization.
* **Why it works:** The LCM must contain every prime factor present in the divisors at its highest exponent.
* **When to use:** When numbers are small or easily factorable (e.g., 12, 15, 18).
* **Example:** $12=2^2 \times 3$, $15=3 \times 5$, $18=2 \times 3^2$. $\text{LCM} = 2^2 \times 3^2 \times 5 = 180$.

---

## Common Mistakes
* **Mistake:** Adding the remainder when the question says "increased by X."
    * **Fix:** If the number *increased by X* is divisible, the number itself is $LCM - X$.
* **Mistake:** Subtracting the remainder from the $N$-digit limit instead of adding the difference.
    * **Fix:** For the smallest $N$-digit number, add $(Divisor - Remainder)$ to the limit.
* **Mistake:** Calculating HCF instead of LCM.
    * **Fix:** HCF is for "greatest number that divides," LCM is for "least number divisible by."

---

## Worked Example (Step-by-Step)

**Question:** Find the smallest number of five digits exactly divisible by 16, 24, 36 and 54.

**Solution:**
1. **Find LCM:** Prime factors: $16=2^4$, $24=2^3 \times 3$, $36=2^2 \times 3^2$, $54=2 \times 3^3$.
   $\text{LCM} = 2^4 \times 3^3 = 16 \times 27 = 432$.
2. **Divide Limit:** Smallest 5-digit number is 10000. $10000 \div 432 = 23$ with remainder $64$.
3. **Adjust:** To find the next multiple, add the difference: $432 - 64 = 368$.
4. **Final Result:** $10000 + 368 = 10368$.

**Answer:** 10368

---

## Similar Patterns
**HCF Problems:** Distinguished by keywords like "greatest number that divides" or "largest size/capacity."

---

## Revision Summary
* **Key formula:** $\text{Required} = \text{LCM} \pm \text{Adjustment}$.
* **Spot it by:** "Least number" or "Smallest number" divisible by a set.
* **First move:** Calculate the LCM of the given divisors.
* **Fastest method:** Prime factorization using highest powers.
* **Biggest trap:** Confusing "increased by" (subtract) with "remainder" (add).

---

## Appendix: Prerequisites

### Concepts You Must Know
* **Prime Factorization** — Breaking a number into a product of prime numbers (e.g., $12 = 2^2 \times 3$).
* **Divisibility** — A number $A$ is divisible by $B$ if $A \div B$ leaves a remainder of 0.

### Formulas You Must Know First
* **LCM Definition** — The smallest positive integer that is divisible by each of the numbers in a set.

### Terms Used In This Pattern
* **Divisor** — The number by which another number is divided.
* **Remainder** — The amount left over after division.